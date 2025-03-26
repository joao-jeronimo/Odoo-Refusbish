from odoo.tests.common import TESTCASE_FATHER_CLASS, Form
from odoo.exceptions import UserError, ValidationError
import odoo_module_writers_lib as omwl

class TestSocialPost(TESTCASE_FATHER_CLASS, omwl.testing.AssertLib):
    """
    Testcase for the social.post model.
    """
    
    def test_skel(self):
        """
        Make sure the payslips were fetched correctly.
        """
        self.assertFalse(True)
    
    #######################################################################
    #######################################################################
    #######################################################################
    @classmethod
    def setUpClass(self):
        super(TestSocialPost, self).setUpClass()
        # Companies:
        self.main_company = self.env.ref('base.main_company')
