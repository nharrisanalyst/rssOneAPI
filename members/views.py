from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from members.serializer import MembersSerializer

# Create your views here.

class UserRegistrationAPIView(APIView):
    
    def post(self, request, format=None):
        if 'id' in request.data:
            return Response({'error', 'id already in use'}, status=status.HTTP_400_BAD_REQUEST)
        null_data = {'email':None, 'password': None}
        member_serializer =  MembersSerializer(data=null_data)
        if member_serializer.is_valid():
            member_serializer.save()
        return Response({"id": f"{member_serializer.data.get('id')}"}, status=status.HTTP_201_CREATED)



