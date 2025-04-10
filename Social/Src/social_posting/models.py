# -*- coding: utf-8 -*-
import base64, io
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from pdf2image import convert_from_path, convert_from_bytes

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'
    
    photo_of_socpost_id = fields.Many2one("social.post", string="Post")

    def button_render_pdf_pages(self):
        """
        Render pages of a PDF.
        """
        self.render_pdf_pages()

    def render_pdf_pages(self):
        """
        Creates a PNG attachment for each PDF page.
        """
        self.ensure_one()
        # Get the data:
        source_pdf_data = base64.b64decode(self.with_context(bin_size=False).datas)
        # Split PDF in pages and get the wanted page:
        pdf_pages = convert_from_bytes(source_pdf_data, dpi = 96)
        # Process each page:
        gened_pages = self.env['ir.attachment']
        for pagei in range(len(pdf_pages)):
            # Get the page:
            wanted_page = pdf_pages[pagei]
            # Save the page in a fake file and get it's contents:
            fakefile = io.BytesIO()
            wanted_page.save(fakefile, 'PNG')
            page_bytes = fakefile.getvalue()
            # Create our attachment:
            gened_pages += self.env['ir.attachment'].create({
                'photo_of_socpost_id' : self.photo_of_socpost_id.id,
                'name'      : "%s Page %d.png" % (self.name, pagei),
                'datas'     : base64.b64encode(page_bytes),
                })
        return gened_pages

class SocialPost(models.Model):
    _name = 'social.post'
    _rec_name = "subject"

    company_id = fields.Many2one("res.company", required=True, string="Company", default=lambda self: self.env.user.company_id.id)
    
    subject = fields.Char("Subject", required=True)
    post_body = fields.Text("Body", required=True)

    publish_date = fields.Date("Publish date")
    photos_ids = fields.One2many("ir.attachment", inverse_name="photo_of_socpost_id", string="Post photos")
    publish_notes = fields.Char("Publish notes")

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
