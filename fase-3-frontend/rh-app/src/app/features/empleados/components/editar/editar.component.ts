import { Component, inject, OnInit, ChangeDetectorRef } from '@angular/core'; // <- 1. Importamos ChangeDetectorRef
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { Empleado } from '../../models/empleado.model';
import { EmpleadoServicio } from '../../services/empleado.service';

@Component({
  selector: 'app-editar',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './editar.component.html',
  styleUrl: './editar.component.css'
})
export class EditarComponent implements OnInit {
  private empleadoService = inject(EmpleadoServicio);
  private router = inject(Router);
  private route = inject(ActivatedRoute);
  private cdr = inject(ChangeDetectorRef); // <- 2. Inyectamos el detector de cambios

  id!: number;
  empleado: Empleado = { nombre: '', departamento: '', sueldo: 0 };

  ngOnInit(): void {
    this.id = Number(this.route.snapshot.paramMap.get('id'));
    
    this.empleadoService.obtenerEmpleadoPorId(this.id).subscribe({
      next: (datos) => {
        this.empleado = datos;
        this.cdr.detectChanges(); // 💡 3. ¡Despertamos a Angular manualmente para que pinte los datos ya mismo!
      },
      error: (err) => console.error('Error al cargar datos del empleado:', err)
    });
  }

  actualizar(): void {
    // Nota: Asegúrate de que en tu servicio el método se llame 'editarEmpleado' o 'actualizarEmpleado'
    this.empleadoService.editarEmpleado(this.id, this.empleado).subscribe({
      next: () => {
        this.router.navigate(['/empleados']);
      },
      error: (err) => console.error('Error al actualizar el empleado:', err)
    });
  }
}