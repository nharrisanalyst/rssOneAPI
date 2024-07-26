from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rss.serializers import RssURLSerializer
from members.models import Members

# Create your views here.

message_created='The RSS URL was added'

class RssURL(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request, format=None):
        data = request.data
        member_data = data['member']
        try:
            member = Members.objects.get(id=member_data)
        except Members.DoesNotExist:
            return Response({'message':'The member is not in the database', 'error':True, 'code':500})
        
        url_serializer = RssURLSerializer(data=data)
        if url_serializer.is_valid():
            url_inst = url_serializer.save()
        else:
            return Response(url_serializer.errors.values(), status=status.HTTP_400_BAD_REQUEST)
        url_inst.members.add(member)



        
        

        

        
