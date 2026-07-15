from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from campañas.views import CampañaViewSet, ActividadViewSet 

# Importaciones necesarias para los archivos MEDIA
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'campanias', CampañaViewSet, basename='campaña')
router.register(r'actividades', ActividadViewSet, basename='actividad')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# ESTO ES LO QUE FALTA: Le dice a Django cómo servir las fotos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)