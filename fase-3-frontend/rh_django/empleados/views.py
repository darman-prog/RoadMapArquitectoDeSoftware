from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoListCreateView(generics.ListCreateAPIView):
    """
    Controla dos operaciones:
    - GET: Lista todos los empleados de la base de datos.
    - POST: Crea un nuevo empleado validando los datos de entrada.
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class EmpleadoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Controla tres operaciones basándose en el ID del empleado provisto en la URL:
    - GET: Busca y devuelve los detalles de un empleado específico.
    - PUT / PATCH: Modifica y actualiza la información del empleado.
    - DELETE: Remueve permanentemente el registro del empleado.
    """
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    # Definimos que el parámetro de búsqueda en la URL coincida con el nombre de nuestra PK
    lookup_field = 'idEmpleado'