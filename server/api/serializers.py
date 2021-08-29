import re
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from api.models import Media, Post
from api.lib.excepion import *
from api.lib.audio_transform import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
        read_only_fields = ['created_at']
    
    def create(self, validated_data):
        media = Media()
        media.title = validated_data['title']
        media.album = validated_data['album']
        media.composer = validated_data['composer']
        media.copyright = validated_data['copyright']
        media.user = validated_data['user']

        try:
            file = validated_data['file']
            file_name, file_format = re.findall('(^[\w]+)([.][\w]+$)', file.name)[0]

            if not file: raise NotExistFileException()

            if file_format not in SUPPORT_FORMAT:
                raise NotSupportFormatException()

            metadata = get_metadata(validated_data)
            filtered_file = get_filtered_file(file, file_name, file_format)
            media.file = get_audio_with_meta(filtered_file, file_name, metadata)
        except Exception as err: print(err)
        media.save()
        return media


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
            raise Exception('처리 실패')
        user = validated_data['user']
        if not user:
            raise Exception('유저 없음')
        post.user = user

        post.save()
        return post