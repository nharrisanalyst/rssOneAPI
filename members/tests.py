from django.test import TestCase
from members.models import Members

# Create your tests here.

class MembersTestCase(TestCase):
    
    def setUp(self):
        test_email = 'example@example.com'
        Members.objects.create(email=None, password=None)
        Members.objects.create(email= test_email, password='12345')
    
    def test_member_is_correct(self):
        test_email = 'example@example.com'
        """Memebers are present and have correct data"""
        member_1 = Members.objects.get(id=1)
        member_2 = Members.objects.get(email = test_email)

        self.assertEqual(member_1.id,1)
        self.assertEqual(member_2.email, test_email)