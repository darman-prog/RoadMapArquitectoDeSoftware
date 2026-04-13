from data import guardar_usuario, cargar_datos
from utils import generar_id, validar_edad

def registrar():
    nombre = input("Nombre: ")
    edad = input("Edad:")

                
    if not validar_edad(edad):
        print("Edad inválida")
    
    usuarios = cargar_datos()
    
    nuevo = {
        "id": generar_id(usuarios),
        "nombre": nombre,
        "edad": int(edad),
        "rol": "user"
    }
    
    guardar_usuario(nuevo)
    print("Registrado correctamente")

def listar():
    usuarios = cargar_datos()
    
    for u in usuarios:
        print(u)      