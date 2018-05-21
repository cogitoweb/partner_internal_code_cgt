# -*- coding: utf-8 -*-
from odoo import models, fields, api


class partner(models.Model):
    _inherit = 'res.partner'

    _sql_constraints = {
        ('internal_code_uniq', 'unique(internal_code)', 'Internal Code must be unique!')
    }

    # new fields
    internal_code = fields.Char('Internal Code', index=True, copy=False)


    @api.model
    def create(self, vals):

        if not vals.get('internal_code', False):
            sq = self.env['ir.sequence'].next_by_code('partner.internal.code')

            while self.env['res.partner'].search_count([('internal_code', '=', sq)]):
                # code already used, request another one
                sq = self.env['ir.sequence'].next_by_code('partner.internal.code')

            vals['internal_code'] = sq
        return super(partner, self).create(vals)
