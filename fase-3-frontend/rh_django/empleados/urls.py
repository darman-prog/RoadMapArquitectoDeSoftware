from django.urls import path
from .views import EmpleadoListCreateView, EmpleadoRetrieveUpdateDestroyView

urlpatterns = [
    # Ruta para listar y crear: /api/empleados
    path('empleados', EmpleadoListCreateView.as_view(), name='empleado-list-create'),
    
    # Ruta para buscar, actualizar y eliminar según ID: /api/empleados/<id>
    path('empleados/<int:idEmpleado>', EmpleadoRetrieveUpdateDestroyView.as_view(), name='empleado-detail'),
]