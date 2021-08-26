from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.
def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    return '/'.join(['video_file/', ymd_path, filename])


def get_processed_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    return '/'.join(['processed_file/', ymd_path, filename])    


# Video Model
class Video(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name='영상 제목')
    description = models.TextField(max_length=500, default='', verbose_name='영상 내용')
    file = models.FileField(upload_to=get_file_path, null=True, verbose_name='영상 파일')
    format = models.CharField(max_length=100, null=True, verbose_name='영상 포맷')
    copyright = models.TextField(max_length=500, null=True, verbose_name='영상 저작권')
    duration = models.IntegerField(default=0, verbose_name='영상 길이')
    size = models.IntegerField(default=0, verbose_name='영상 크기')
    is_processed = models.BooleanField(default=False, verbose_name='영상 욕설 처리 상태')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='영상 생성 일자')
    user = models.ForeignKey(User, models.CASCADE, verbose_name='영상 소유자')

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Video)
def file_delete_action(sender, instance, **kwargs):
    instance.video_file.delete(False)


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