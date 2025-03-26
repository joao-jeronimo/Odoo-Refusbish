# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    photo_of_socpost_id = fields.Many2one("social.post", string="Post")

class SocialPost(models.Model):
    _name = 'social.post'
    
    name = fields.Char("Name", required=True)
    details = fields.Text("Details")
    
    photos_ids = fields.One2many("ir.attachment", inverse_name="photo_of_socpost_id", string="Post photos")
