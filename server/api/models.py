import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver


def get_dir_path():
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    return '/'.join(['audio', ymd_path])


def get_file_path(instance, filename):
    PATH_DIR = get_dir_path()
    FILE_DIR = os.path.join(settings.MEDIA_ROOT, PATH_DIR)
    if not os.path.exists(FILE_DIR):
        os.makedirs(FILE_DIR, exist_ok=True)
    return os.path.join(PATH_DIR, filename)


# Media Model
class Media(models.Model):
    title = models.CharField(max_length=100, default='', null=False, verbose_name='제목')
    album = models.CharField(max_length=100, default='', null=False, verbose_name='분류')
    composer = models.CharField(max_length=100, default='', null=False, verbose_name='저자')
    copyright = models.TextField(max_length=500, default='', null=False, verbose_name='저작권')
    file = models.FileField(upload_to=get_file_path, null=True, verbose_name='파일')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 일자')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='생성자')

    def __str__(self):
        return self.title


# Post Model
class Post(models.Model):
    content = models.TextField(max_length=500, default='', verbose_name='글 원본 내용')
    length = models.IntegerField(default=0, verbose_name='글 원본 길이')
    processed_content = models.TextField(max_length=500, default='', verbose_name='글 욕설 처리된 내용')
    is_processed = models.BooleanField(default=False, verbose_name='글 욕설 처리 상태')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='글 생성 일자')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='글 소유자')

    def __str__(self):
        return self.content