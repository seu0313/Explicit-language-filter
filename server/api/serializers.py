from rest_framework import serializers
from django.contrib.auth.models import User, Group
from api.models import Deep

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class DeepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deep
        fields = '__all__'