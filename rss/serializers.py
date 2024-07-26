from rest_framework import serializers
from rss.models import (
    RssURL
)
from members.serializer import MembersSerializer
from members.models import Members

class RssPostSerializer(serializers.ModelSerializer):
    class Meta:
        ordering =['-url']
        model = RssURL
        fields = ('url','title', 'link', 'description')

class RssFeedSerializer(serializers.ModelSerializer):
    posts = RssPostSerializer(many=True, read_only=True)
    
    class Meta:
        ordering =['-url']
        model = RssURL
        fields = ('url','title', 'link', 'description')

class RssURLSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        ordering =['-url']
        model = RssURL
        fields = ('url', 'members')
    

# class ModelRssSerializer(serializers.ModelSerializer):

        





