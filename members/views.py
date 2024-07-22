from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from members.serializer import MembersSerializer

# Create your views here.

class UserRegistrationAPIView(APIView):
    
    def post(self, request, format=None):
        null_data = {'email':None, 'password': None}
        serializer =  MembersSerializer(null_data)
        return Response(serializer.data)



# class JustATestView(APIView):
#     def get(self, request, format=None):
#         return Response({'test':True})