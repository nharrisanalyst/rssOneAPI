from rest_framework import serializers
from members.models import Members
from rss.serializers import RssURLSerializer

class MembersSerializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_null = True)
    password = serializers.CharField(allow_null = True)
    rssURLs =  RssURLSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Members
        fields = ['id', 'email','password', 'rssURLs']

