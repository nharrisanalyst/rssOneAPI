from rest_framework import serializers
from members.models import Members

class MembersSerializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_null = True)
    password = serializers.CharField(allow_null = True)
    
    
    class Meta:
        model = Members
        fields = ['id', 'email','password']

