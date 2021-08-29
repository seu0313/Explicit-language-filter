from django.contrib import admin
from api.models import Media, Post

# Register your models here.
admin.site.register([Media, Post])