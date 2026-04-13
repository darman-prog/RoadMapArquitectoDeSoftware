from data import cargar_datos, eliminar_usuario, buscar_usuario_por_id
from utils import formatear_usuario

def listar_completo():
    lista = cargar_datos()
    
    if not lista:  
        print("Sin usuarios")
    
    for u in lista:
        print(formatear_usuario(u))

def eliminar():
    user_id = input("ID: ").strip()
    
    
    user = buscar_usuario_por_id(user_id)
    
    if user:
        eliminar_usuario(user_id)
        print("Eliminado")
    else:
        print("No existe")

def promover_admin():
    user_id = int(input("ID a promover: "))
    
    user = buscar_usuario_por_id(user_id)
    
    if user["rol"] == "admin": 
        print("Ya es admin")
    
    user["rol"] = "admin"
    print("Promovido")