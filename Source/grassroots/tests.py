from django.test import TestCase

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a sample Person instance
        self.person = self.person.objects.create(
            userID=1,
            username='john_doe',
            password='secure_password',
            name='John Doe',
            phone='1234567890',
            address='123 Main St'
        )

        # Create a sample Grant instance
        self.grant = self.grant.objects.create(
            grantID=1,
            grantName='Education Grant',
            grantAmount=1000.00,
            description='Supporting education'
        )

        # Create a sample SpecialAward instance
        self.special_award = self.special_award.objects.create(
            awardID=1,
            awardName='Special Recognition',
            description='Special recognition award',
            eligibility='Outstanding achievements',
            detail='Details about the award',
            status='Active'
        )

        # Create a sample Customer instance
        self.customer = self.customer.objects.create(
            userID=2,
            username='jane_doe',
            password='another_secure_password',
            name='Jane Doe',
            phone='9876543210',
            address='456 Oak St'
        )

        # Create a sample Application instance
        self.application = self.application.objects.create(
            appID=1,
            applicant=self.customer,
            grant=self.grant,
            award=self.special_award,
            detail='Application details',
            status='Pending'
        )

    def test_view_profile(self):
        # Test the viewProfile method of Person
        self.assertEqual(self.person.viewProfile(), None)

    def test_apply_for_grant(self):
        # Test the applyForGrant method of Customer
        self.assertEqual(self.customer.applyForGrant(), None)

    def test_view_applications(self):
        # Test the viewApplications method of Admin
        admin = admin.objects.create(
            userID=3,
            username='admin_user',
            password='admin_password',
            name='Admin User',
            phone='1112223333',
            address='789 Elm St'
        )
        self.assertEqual(admin.viewApplications(), None)

    def test_edit_application(self):
        # Test the editApplication method of Admin
        admin = admin.objects.create(
            userID=4,
            username='admin_user_2',
            password='admin_password_2',
            name='Admin User 2',
            phone='4445556666',
            address='987 Pine St'
        )
        self.assertEqual(admin.editApplication(), None)

    def test_view_customer(self):
        # Test the viewCustomer method of Admin
        admin = admin.objects.create(
            userID=5,
            username='admin_user_3',
            password='admin_password_3',
            name='Admin User 3',
            phone='7778889999',
            address='654 Maple St'
        )
        self.assertEqual(admin.viewCustomer(), None)

    def test_view_applications_in_grant(self):
        # Test the viewApplications method of Grant
        self.assertEqual(self.grant.viewApplications(), None)

    def test_apply_for_special_award(self):
        # Test the applyForSpecial method of SpecialAward
        self.assertEqual(self.special_award.applyForSpecial(), None)

    def test_submit_application(self):
        # Test the submitApplication method of Application
        self.assertEqual(self.application.submitApplication(), None)

    def test_view_status(self):
        # Test the viewStatus method of Application
        self.assertEqual(self.application.viewStatus(), None)
