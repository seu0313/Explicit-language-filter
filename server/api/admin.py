from django.contrib import admin
from api.models import Video, Post

# Register your models here.
admin.site.register([Video, Post])