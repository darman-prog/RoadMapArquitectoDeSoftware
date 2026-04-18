from data import guardar_usuario, cargar_datos
from utils import generar_id, validar_edad,formatear_usuario

def registrar():
    
    while True:
        
        nombre = input("Nombre: ")
        edad = input("Edad:")

                    
        if not validar_edad(edad):
            print("Edad inválida")
            respuesta = input("¿Deseas intentar de nuevo? (s/n): ").lower()
            if respuesta == "s":
                continue
            else:
                break

        usuarios = cargar_datos()
        
        nuevo = {
            "id": generar_id(usuarios),
            "nombre": nombre,
            "edad": int(edad),
            "rol": "user"
        }
        
        guardar_usuario(nuevo)
        print("Registrado correctamente")

        respuesta = input("¿Deseas registrar otro usuario? (s/n): ").lower()
        if respuesta != "s":
            break

def listar():
    usuarios = cargar_datos()
    
    for u in usuarios:
        print(formatear_usuario(u))