from rest_framework.test import APITestCase
from rest_framework import status
from members.models import Members

class MemberRegistration(APITestCase):
    def test_member_registration_endpoint(self):
        response = self.client.post('/api/user/register')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Members.objects.count(), 1)

        