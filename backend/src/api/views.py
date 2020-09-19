from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.parsers import ParseError
from api.serializers import UserSerializer, GroupSerializer, DeepSerializer

# Deep Apps
from deep.models import Deep

# User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# Group
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# Deep File
class DeepViewSet(viewsets.ModelViewSet):
    queryset = Deep.objects.all()
    serializer_class = DeepSerializer
    # parser_classes = (FileUploadParser, )
    permission_classes = [permissions.IsAuthenticated]