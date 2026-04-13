
def generar_id(lista):
    if len(lista)== 0:
        return 1
    
    max_id = lista[0]["id"]

    for u in lista:
        if u["id"] > max_id:
            max_id = u["id"]
    
    return max_id + 1
        
def validar_edad(edad):
    if edad.isdigit():
        return True
    return False

def formatear_usuario(user):
    return f"{user['id']} - {user['nombre'].upper()} ({user['edad']})"