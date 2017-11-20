# -*- coding: utf-8 -*-
from odoo import models, fields, api


class partner(models.Model):
    _inherit = 'res.partner'

    internal_code = fields.Char('Internal Code', index=True)


    @api.model
    def create(self, vals):
        if not vals.get('internal_code', False):
            # vals['internal_code'] = self.env['ir.sequence'].get('partner.internal.code') or '/'
            # vals['internal_code'] = self.env['ir.sequence'].next_by_code('partner.internal.code') or '/'

            sq = self.env['ir.sequence'].next_by_code('partner.internal.code')
            while self.env['res.partner'].search_count([('internal_code', '=', sq)]):
                ## code already used, request another one
                sq = self.env['ir.sequence'].next_by_code('partner.internal.code')

            vals['internal_code'] = sq
        return super(partner, self).create(vals)


    _sql_constraints = {
        ('internal_code_uniq', 'unique(internal_code)', 'Internal Code must be unique!')
    }
