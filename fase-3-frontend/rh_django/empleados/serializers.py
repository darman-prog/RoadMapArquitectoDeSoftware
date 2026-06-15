from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        # Mapeamos explícitamente todos los campos requeridos en el JSON resultante
        fields = ['idEmpleado', 'nombre', 'departamento', 'sueldo']

    # Validación nativa para el campo 'sueldo' (Formato: validate_nombreCampo)
    def validate_sueldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("El sueldo del empleado debe ser estrictamente mayor a 0.")
        return value