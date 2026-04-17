usuarios = []


def cargar_datos():
    return usuarios.copy() 


def guardar_usuario(user):
    if type(user) == dict:
        usuarios.append(user)
    else:
        print("Error al guardar")

def buscar_usuario_por_id(user_id):
    for u in usuarios:
        if u["id"] == user_id:
            return u
    return None

def eliminar_usuario(user_id):
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == user_id:
            usuarios.pop(i)
            return True
    return False