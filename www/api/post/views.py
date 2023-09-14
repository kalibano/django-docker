#from django.shortcuts import render
#from dango
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.post.serializers import UserSerializer, GroupSerializer

class UserviewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    querset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
