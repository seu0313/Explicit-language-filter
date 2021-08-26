from django.db import models
from datetime import datetime
from django.db.models.signals import post_delete
from django.dispatch import receiver

def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    return '/'.join(['video_file/', ymd_path, filename])

def get_processed_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    return '/'.join(['processed_file/', ymd_path, filename])    

# Create your models here.
class Deep(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    description = models.TextField(max_length=500, verbose_name='내용')
    video_file = models.FileField(upload_to=get_file_path, null=True, verbose_name='영상 파일')
    video_duration = models.IntegerField(null=True, verbose_name='영상 길이')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 일자')

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Deep)
def file_delete_action(sender, instance, **kwargs):
    instance.video_file.delete(False)