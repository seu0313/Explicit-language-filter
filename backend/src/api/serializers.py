from django.contrib.auth.models import User, Group
from rest_framework import serializers
from deep.models import Deep

# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

# Group
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


# FileUpload Parser
class DeepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deep
        fields = ('id', 'title', 'video_file')




