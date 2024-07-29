from rest_framework import serializers
from rss.models import (
    RssURL
)

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
        fields = ('url','title', 'link', 'description','posts')

class RssURLSerializer(serializers.ModelSerializer):
    feed =RssFeedSerializer(read_only=True)
    class Meta:
        ordering =['-url']
        model = RssURL
        fields = ('url', 'feed')
    
        





