# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class Equipment(models.Model):
    _name = 'refurb.equipment'
    
    name = fields.Char("Name", "required=True)
    details = fields.Html("Details")

