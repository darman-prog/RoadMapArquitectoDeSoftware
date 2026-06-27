import { Component, inject, OnInit, signal } from '@angular/core';
import { Empleado } from '../../models/empleado.model';
import { EmpleadoServicio } from '../../services/empleado.service';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { EliminarComponent } from '../eliminar/eliminar.component';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-lista',
  imports: [RouterOutlet,CommonModule,EliminarComponent,RouterModule], // Necesario para inyectar las vistas según la URL actual
  templateUrl: './lista.component.html', // Vinculo a su plantilla externa
  styleUrl: './lista.component.css'
})
export class ListaComponent implements OnInit {
  // Manejo de estado moderno mediante Signals
  empleados = signal<Empleado[]>([]);
  
  // Inyección directa del servicio de datos
  private empleadoService = inject(EmpleadoServicio);

  // Variables para guardar temporalmente al empleado que se quiere borrar
  idSeleccionado!: number;
  nombreSeleccionado: string = '';

  ngOnInit(): void {
    this.cargarEmpleados();
  }

  // Consulta el servicio y actualiza el valor del Signal reactivo
  cargarEmpleados(): void {
    this.empleadoService.obtenerEmpleados().subscribe({
      next: (data) => {
        this.empleados.set(data);
      },
      error: (err) => {
        console.error('Error al recuperar los empleados:', err);
      }
    });
  }

  prepararEliminacion(id: number, nombre: string): void {
    this.idSeleccionado = id;
    this.nombreSeleccionado = nombre;
  }
  
}