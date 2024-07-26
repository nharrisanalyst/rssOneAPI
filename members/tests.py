from django.test import TestCase
from members.models import Members
from members.serializer import MembersSerializer

# Create your tests here.

#test for Models

class MembersTestCase(TestCase):
    
    def setUp(self):
        test_email = 'example@example.com'
        Members.objects.create(email=None, password=None)
        Members.objects.create(email= test_email, password='12345')
    
    def test_member_is_correct(self):
        test_email = 'example@example.com'
        """Members are present and have correct data"""
        member_1 = Members.objects.get(email=None)
        member_2 = Members.objects.get(email = test_email)
        
        self.assertGreaterEqual(member_1.id,0)
        self.assertEqual(member_2.email, test_email)


#test for Serializer

class MembersSerializerTestCase(TestCase):
        
    def setUp(self):
        self.memberData_1 ={
            "email":None,
            "password":None

        }
        self.memberData_2 ={
            'email':'example@example.com',
            'password':'12345'
        }

        self.serializer_1 =MembersSerializer(data = self.memberData_1)
       
        if self.serializer_1.is_valid():
           self.members_instance = self.serializer_1.save()

    def test_contains_specif_fields(self):
        data = self.serializer_1.data
        self.assertEqual(set(data.keys()), set(['id', 'email', 'password']))
            

