# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    photo_of_socpost_id = fields.Many2one("social.post", string="Post")

class SocialPost(models.Model):
    _name = 'social.post'
    _rec_name = "subject"
    
    subject = fields.Char("Subject", required=True)
    post_body = fields.Text("Body", required=True)

    publish_date = fields.Date("Publish date")
    photos_ids = fields.One2many("ir.attachment", inverse_name="photo_of_socpost_id", string="Post photos")
    publish_notes = fields.Text("Publish notes")

    def button_was_published_today(self):
        """
        Sets a post as having being published today.
        """
        for post in self:
            if post.publish_date:
                raise UserError(_("Post «%(subject)s» was published on %(publish_date)s.") % {
                    'subject'       : post.subject,
                    'publish_date'  : post.publish_date,
                    })
            post.publish_date = fields.Date.today()

    def unlink(selves):
        """
        Sets a post as having being published today.
        """
        if any(selves.filtered(lambda self: self.publish_date)):
            raise UserError(_("One cannot delete published posts. Clear the publish date if you really need to delete such a post."))
        super(SocialPost, selves).unlink()
