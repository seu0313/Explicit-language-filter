from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import routers
from api.views import UserViewSet, GroupViewSet
from deep.views import DeepViewSet
from deep.views import Deep_list

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('deeps', DeepViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('deep/', Deep_list, name='deep-list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
