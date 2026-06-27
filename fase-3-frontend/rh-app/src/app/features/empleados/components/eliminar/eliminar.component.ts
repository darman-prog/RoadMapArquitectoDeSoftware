import { Component, inject, Input, Output, EventEmitter, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // <- ¡CRUCIAL! Importar para usar el enlace bidireccional
import { EmpleadoServicio } from '../../services/empleado.service';

@Component({
  selector: 'app-eliminar',
  standalone: true,
  imports: [CommonModule, FormsModule], // <- Registramos FormsModule aquí
  templateUrl: './eliminar.component.html',
  styleUrl: './eliminar.component.css'
})
export class EliminarComponent implements OnChanges {
  private empleadoService = inject(EmpleadoServicio);

  @Input() idEmpleadoEliminar!: number;
  @Input() nombreEmpleadoEliminar: string = '';
  @Output() empleadoEliminado = new EventEmitter<void>();

  // Variable donde se guardará lo que el usuario escribe en el input
  nombreConfirmacion: string = '';

  // Este método de Angular detecta cuando el listado nos pasa un empleado diferente
  ngOnChanges(changes: SimpleChanges): void {
    if (changes['idEmpleadoEliminar']) {
      this.nombreConfirmacion = ''; // Limpiamos el input anterior para que empiece vacío
    }
  }

  confirmarEliminacion(): void {
    // Doble verificación: Solo si coincide exactamente, disparamos la petición a Django
    if (this.nombreConfirmacion.trim() === this.nombreEmpleadoEliminar.trim()) {
      this.empleadoService.eliminarEmpleado(this.idEmpleadoEliminar).subscribe({
        next: () => {
          this.empleadoEliminado.emit();
          const botonCerrar = document.getElementById('btn-cerrar-modal-eliminar');
          if (botonCerrar) botonCerrar.click();
        },
        error: (err) => console.error('Error al intentar eliminar el empleado:', err)
      });
    }
  }
}