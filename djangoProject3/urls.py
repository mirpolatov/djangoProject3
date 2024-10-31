from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from apps import apps
from djangoProject3 import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_BASE_DIR) + static(settings.MEDIA_URL,
                                                                                               document_root=settings.MEDIA_ROOT)
