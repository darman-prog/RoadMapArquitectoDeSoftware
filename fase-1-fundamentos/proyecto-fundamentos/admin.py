from data import cargar_datos, eliminar_usuario, buscar_usuario_por_id
from utils import formatear_usuario

def listar_completo():
    lista = cargar_datos()
    
    if not lista:  
        print("Sin usuarios")
        return
    
    hay_admin = False

    for u in lista:
        if u["rol"] == "admin":
            print(formatear_usuario(u))
            hay_admin = True

    if not hay_admin:
        print("no hay admins")

def eliminar():

    user_id = int(input("ID: "))

    user = buscar_usuario_por_id(user_id)
    
    if user is not None:
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