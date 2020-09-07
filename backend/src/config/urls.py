from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

] + static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)
