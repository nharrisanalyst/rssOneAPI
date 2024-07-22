from rest_framework import serializers
from members.models import Members

class MembersSerializer(serializers.Serializer):
    email = serializers.CharField(allow_null = True)
    password = serializers.CharField(allow_null = True)
    
    def create(self, validated_data):
        Members.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
