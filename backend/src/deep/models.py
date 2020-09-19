from django.db import models

# Create your models here.
class Deep(models.Model):
    title = models.CharField(max_length=150, default='')
    video_file = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
