from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

] + static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)
