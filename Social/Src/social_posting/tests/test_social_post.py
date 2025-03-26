import odoo_module_writers_lib as omwl, odoo, datetime
from odoo.tests.common import TESTCASE_FATHER_CLASS, Form
from odoo.exceptions import UserError, ValidationError

class TestSocialPost(TESTCASE_FATHER_CLASS, omwl.testing.AssertLib):
    """
    Testcase for the social.post model.
    """

    def test_button_was_published_today_sets_the_date(self):
        """
        Method button_was_published_today() sets the publish date as baing
        today, as the name suggests.
        """
        self.assertFalse( self.post_musp_congress_nr15.publish_date )
        self.post_musp_congress_nr15.button_was_published_today()
        self.assertEqual( self.post_musp_congress_nr15.publish_date, self.date_real_today )

    def test_button_was_published_today_refuses_to_modify_already_posted(self):
        """
        Method button_was_published_today() raises exception if called over
        a published post.
        """
        self.post_musp_congress_nr15.publish_date = self.date_2023_06_02
        with self.assertRaises(UserError):
            self.post_musp_congress_nr15.button_was_published_today()
    
    #######################################################################
    #######################################################################
    #######################################################################
    @classmethod
    def setUpClass(self):
        super(TestSocialPost, self).setUpClass()
        # Dates:
        self.date_real_today = odoo.fields.Date.today()
        self.date_2023_06_02 = datetime.date(year=2023, month=6, day=2)
        # Companies:
        self.main_company = self.env.ref('base.main_company')
        # Posts:
        self.post_musp_congress_nr15 = self.env.ref('social_posting.demo_musp_congress_nr15')
