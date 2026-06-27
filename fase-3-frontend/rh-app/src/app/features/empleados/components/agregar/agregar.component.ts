import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router , RouterModule} from '@angular/router';
import { Empleado } from '../../models/empleado.model';
import { EmpleadoServicio } from '../../services/empleado.service';

@Component({
  selector: 'app-agregar',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule], // FormsModule habilita ngModel en la vista
  templateUrl: './agregar.component.html',
  styleUrl: './agregar.component.css'
})
export class AgregarComponent {
  private empleadoService = inject(EmpleadoServicio);
  private router = inject(Router);

  // Instancia base del modelo vinculada a los campos del formulario
  nuevoEmpleado: Empleado = {
    nombre: '',
    departamento: '',
    sueldo: 0
  };

  // Envía el modelo al servicio e intercepta el resultado
  guardar(): void {
    this.empleadoService.agregarEmpleado(this.nuevoEmpleado).subscribe({
      next: () => {
        // Redirección inmediata al listado tras insertar con éxito
        this.router.navigate(['/empleados']);
      },
      error: (err) => {
        console.error('Error al intentar registrar al empleado:', err);
      }
    });
  }
}