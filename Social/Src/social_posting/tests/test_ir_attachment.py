import odoo_module_writers_lib as omwl, odoo, datetime
from odoo.tests.common import TESTCASE_FATHER_CLASS, Form
from odoo.addons.base_testing.tests.common import IrAttachmentTestingMixin
from odoo.exceptions import UserError, ValidationError

class TestSocialPost(TESTCASE_FATHER_CLASS, omwl.testing.AssertLib, IrAttachmentTestingMixin):
    """
    Testcase for the social.post model.
    """

    def test_render_pdf_pages(self):
        """
        Method render_pdf_pages() must return a recordset of attachments
        containing PDF pages.
        """
        self.assertFalse( True )

    #######################################################################
    #######################################################################
    #######################################################################
    @classmethod
    def setUpClass(self):
        super(TestSocialPost, self).setUpClass()
        self.testcase_filepath = __file__
        # Attachments:
        self.attach_pdf_both = self.aux_create_attachment_from_file(self, "fixtures/both.pdf")
