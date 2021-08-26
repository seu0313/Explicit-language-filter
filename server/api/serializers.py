import re
from django.db.utils import Error
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from api.models import Video, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def processing(self, value):
        value = re.sub('[^0-9a-zA-Z ]', '*', value)
        return value
    
    def create(self, validated_data):
        post = Post()
        post.content = validated_data['content']
        try:
            post.processed_content = self.processing(validated_data['content'])
            post.length = len(validated_data['content'])
            post.is_processed = True
        except:
            raise Error('처리 실패')
        user = validated_data['user']
        if not user:
            raise Error('유저 없음')
        post.user = user

        post.save()
        return post