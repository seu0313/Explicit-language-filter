from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from api.models import Deep
from api.serializers import UserSerializer, GroupSerializer, DeepSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeepViewSet(viewsets.ModelViewSet):
    queryset = Deep.objects.all()
    serializer_class = DeepSerializer

    @api_view(['POST'])
    def create_deep(self, request: Request):
        video_file = request.data['video_file']