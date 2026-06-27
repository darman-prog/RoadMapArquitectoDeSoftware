from django.db import models

class Empleado(models.Model):
    # idEmpleado actúa como clave primaria autoincremental
    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=150, null=False, blank=False)
    departamento = models.CharField(db_column='departamento', max_length=150, null=False, blank=False)
    sueldo = models.DecimalField(db_column='sueldo', max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        db_table = 'empleado'

    def __str__(self):
        return f"{self.nombre} - {self.departamento}"