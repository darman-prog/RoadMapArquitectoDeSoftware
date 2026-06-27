import { Routes } from '@angular/router';
import { ListaComponent } from './features/empleados/components/lista/lista.component';
import { AgregarComponent } from './features/empleados/components/agregar/agregar.component'; // Importa el nuevo componente de formulario
import { EditarComponent } from './features/empleados/components/editar/editar.component'; // <- ¡Ahora sí existe!

export const routes: Routes = [
  { path: 'empleados', component: ListaComponent },
  { path: 'agregar-empleado', component: AgregarComponent }, // Nueva ruta para el formulario
  { path: '', redirectTo: 'empleados', pathMatch: 'full' },
  { path: 'editar-empleado/:id', component: EditarComponent } // Ruta para editar un empleado específico
];