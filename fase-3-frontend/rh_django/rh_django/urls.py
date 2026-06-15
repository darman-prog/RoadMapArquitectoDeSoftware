from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incorporamos las urls del módulo de empleados y les anteponemos el segmento 'api/'
    path('api/', include('empleados.urls')),
]