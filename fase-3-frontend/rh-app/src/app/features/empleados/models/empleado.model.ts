export interface Empleado {
    idEmpleado?: number; // El ID es opcional en la interfaz ya que lo genera el backend en las altas
    nombre: string;
    departamento: string;
    sueldo: number;
}