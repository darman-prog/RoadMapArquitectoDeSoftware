import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Empleado } from '../models/empleado.model';

@Injectable({
  providedIn: 'root'
})
export class EmpleadoServicio {
  private http = inject(HttpClient);
  private baseURL = 'http://localhost:8080/api/empleados';

  obtenerEmpleados(): Observable<Empleado[]> {
    return this.http.get<Empleado[]>(this.baseURL);
  }

  // Envía un nuevo registro de empleado a la API de Django
  agregarEmpleado(empleado: Empleado): Observable<Empleado> {
    // Clonamos el objeto para limpiar el idEmpleado antes del envío
    const { idEmpleado, ...empleadoSinId } = empleado;
    return this.http.post<Empleado>(this.baseURL, empleadoSinId);
  }

  obtenerEmpleadoPorId(idEmpleado: number): Observable<Empleado> {
      return this.http.get<Empleado>(`${this.baseURL}/${idEmpleado}`);
    }

  editarEmpleado(idEmpleado: number, empleado: Empleado): Observable<Empleado> {
      return this.http.put<Empleado>(`${this.baseURL}/${idEmpleado}`, empleado);
    }

  actualizarEmpleado(idEmpleado: number, empleado: Empleado): Observable<Empleado> {
    return this.http.put<Empleado>(`${this.baseURL}/${idEmpleado}`, empleado);
  }

  eliminarEmpleado(idEmpleado: number): Observable<void> {
    return this.http.delete<void>(`${this.baseURL}/${idEmpleado}`);
  }
}