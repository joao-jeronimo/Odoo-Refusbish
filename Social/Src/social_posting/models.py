# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    photo_of_socpost_id = fields.Many2one("social.post", string="Post")

class SocialPost(models.Model):
    _name = 'social.post'
    _rec_name = "subject"
    
    subject = fields.Char("Subject", required=True)
    details = fields.Text("Details")

    publish_date = fields.Date("Publish date")
    
    photos_ids = fields.One2many("ir.attachment", inverse_name="photo_of_socpost_id", string="Post photos")
