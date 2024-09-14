# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    photo_of_equipment_id = fields.Many2one("refurb.equipment", string="Equipment photo")

class Equipment(models.Model):
    _name = 'refurb.equipment'
    
    name = fields.Char("Name", required=True)
    details = fields.Html("Details")
    
    photos_ids = fields.One2many("ir.attachment", inverse_name="photo_of_equipment_id", string="Equipment photos")

