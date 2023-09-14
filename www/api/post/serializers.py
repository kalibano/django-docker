from django.contrib.auth.models import User,Group
from rest_framework import serializers

class UserSerialier(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class GroupSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']