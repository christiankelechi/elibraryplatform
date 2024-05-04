
from django.contrib import admin
import django.urls
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import include
from rest_framework import permissions
from django.urls import path,re_path,include
from django.urls import path, include
from core_app_root.security import views
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Elibraryplatform Api",
      default_version='v1',
      description="Elibraryplatform App Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kezechristian@gmail.com"),
      license=openapi.License(name="Elibraryplatform licence"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('',include('core_app_root.urls')),
    path('library/',include('core_app_root.ai_application_dashboard.urls')),
    path('ai/',include('core_app_root.ai_applications.routers')),
    path('',include('core_app_root.security.urls')),
    path('',include(('core_app_root.security.user.routers','core_app_root.security.user'))),
    path('',include(('core_app_root.security.auth.routers','core_app_root.security.auth'))),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.face_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
