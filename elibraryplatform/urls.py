
from django.contrib import admin
import django.urls
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path,re_path,include
schema_view = get_schema_view(
   openapi.Info(
      title="Elibraryplatform Api",
      default_version='v1',
      description="Elibraryplatform App Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kezechristian@gmail.com"),
      license=openapi.License(name="Mechrecommender licence"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('',include(('core_app_root.security.user.routers','core_app_root.security.user'))),
    path('',include(('core_app_root.security.auth.routers','core_app_root.security.auth'))),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)