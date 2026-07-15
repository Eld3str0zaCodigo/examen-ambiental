from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from campañas.views import CampañaViewSet, ActividadViewSet 

# Importaciones necesarias para los archivos MEDIA
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

router = routers.DefaultRouter()
router.register(r'campanias', CampañaViewSet, basename='campaña')
router.register(r'actividades', ActividadViewSet, basename='actividad')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Le dice a Django cómo servir las fotos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 🔥 CREACIÓN AUTOMÁTICA DEL ADMINISTRADOR EN PRODUCCIÓN
User = get_user_model()
try:
    # Puedes cambiar 'admin', 'admin@mail.com' y 'admin1234' por tus credenciales
    User.objects.create_superuser('admin', 'admin@mail.com', 'admin1234')
    print("¡Superusuario creado con éxito en producción!")
except IntegrityError:
    # Si ya se creó en un reinicio anterior, no hace nada para evitar errores
    pass