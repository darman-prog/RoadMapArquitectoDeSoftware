import usuarios
import admin

def main():
    while True:
        print("\n--- SISTEMA ---")
        print("1. Registrar")
        print("2. Listar usuarios")
        print("3. Admin listar")
        print("4. Eliminar usuario")
        print("5. Promover a admin")
        print("6. Salir")
        
        op = input("Opción: ")
        
        if op == "1":
            usuarios.registrar()
        
        elif op == "2":
            usuarios.listar()
        
        elif op == "3":
            admin.listar_completo()
        
        elif op == "4":
            admin.eliminar()
        
        elif op == "5":
            admin.promover_admin()
        
        elif op == "6":
            print("Cerrando Programa....")
            break
        
        else:
            print("Error")

if __name__ == "__main__":
    main()