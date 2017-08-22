# -*- coding: utf-8 -*-
from odoo import models, fields, api


class partner(models.Model):
    _inherit = 'res.partner'

    internal_code = fields.Char('Internal Code', index=True)


    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        res = []
        if name:
            recs = self.search([('internal_code', operator, name)] + args, limit=limit, context=context)
            res = self.name_get(recs)
        res += super(partner, self).name_search(name, args, operator=operator, limit=limit)
        return res


    @api.model
    def create(self, vals):
        if not vals.get('internal_code', False):
            vals['internal_code'] = self.env[
                'ir.sequence'].get('partner.internal.code') or '/'
                # 'ir.sequence'].next_by_code('partner.internal.code') or '/'
        return super(partner, self).create(vals)


    _sql_constraints = {
        ('internal_code_uniq', 'unique(internal_code)', 'Internal Code mast be unique!')
    }
