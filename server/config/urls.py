from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import UserViewSet, GroupViewSet
from deep.views import DeepViewSet

app_name = 'deep'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('deeps', DeepViewSet)

schema_url_patterns = [ 
    path('api/v1/', include(router.urls)), 
]
schema_view = get_schema_view( 
    openapi.Info( 
        title="Django API", 
        default_version='v1', 
        terms_of_service="https://www.google.com/policies/terms/",
    ), 
    public=True,
    permission_classes=(permissions.AllowAny,), 
    patterns=schema_url_patterns, 
)

urlpatterns = [
    # admin site
    path('admin/', admin.site.urls),

    # api
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
