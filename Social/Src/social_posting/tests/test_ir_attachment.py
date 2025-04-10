import odoo_module_writers_lib as omwl, odoo, datetime, multimedia_assert, base64
from odoo.tests.common import TESTCASE_FATHER_CLASS, Form
from odoo.addons.base_testing.tests.common import IrAttachmentTestingMixin
from odoo.exceptions import UserError, ValidationError

class TestSocialPost(TESTCASE_FATHER_CLASS, omwl.testing.AssertLib, IrAttachmentTestingMixin, multimedia_assert.MultimediaAssert):
    """
    Testcase for the social.post model.
    """

    def test_render_pdf_pages(self):
        """
        Method render_pdf_pages() must return a recordset of attachments
        containing PDF pages.
        """
        pdfpages = self.attach_pdf_both.render_pdf_pages()
        # There should be both two of them:
        self.assertLength(pdfpages, 2)
        # Each with it's own legitimate dimms:
        self.assertImageDataDimms(
            base64.b64decode(pdfpages[0].with_context(bin_size=False).datas),
            (378, 756),  0.0014)
        self.assertImageDataDimms(
            base64.b64decode(pdfpages[1].with_context(bin_size=False).datas),
            (756, 1134), 0.0006)

    #######################################################################
    #######################################################################
    #######################################################################
    @classmethod
    def setUpClass(self):
        super(TestSocialPost, self).setUpClass()
        self.testcase_filepath = __file__
        # Attachments:
        self.attach_pdf_both = self.aux_create_attachment_from_file(self, "fixtures/both.pdf")
