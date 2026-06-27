from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        # Mapeamos explícitamente todos los campos requeridos en el JSON resultante
        fields = ['idEmpleado', 'nombre', 'departamento', 'sueldo']

    # Validación nativa para el campo 'nombre' (Formato: validate_nombreCampo)
    def validate_nombre(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("El nombre del empleado no puede estar vacío.")
        return value

    # Validación nativa para el campo 'departamento' (Formato: validate_nombreCampo)
    def validate_departamento(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("El departamento del empleado no puede estar vacío.")
        return value

    # Validación nativa para el campo 'sueldo' (Formato: validate_nombreCampo)
    def validate_sueldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("El sueldo del empleado debe ser estrictamente mayor a 0.")
        return value