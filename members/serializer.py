from rest_framework import serializers
from members.models import Members
from rss.serializers import RssURLSerializer

class MembersSerializer(serializers.Serializer):
    email = serializers.CharField(allow_null = True)
    password = serializers.CharField(allow_null = True)
    rssURLS = RssURLSerializer(many = True, read_only=True)
    
    def create(self, validated_data):
       return  Members.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
