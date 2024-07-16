from libros import GestionLibros
from usuarios import GestionUsuarios
#from prestamos import GestionPrestamos

def menu_principal( gestionUsuarios,gestionLibros):
    while True:
        print("---Gestión Biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            # llama a funcion menu_libros de otro módulo
            gestionLibros.menu_libros()
        elif opcion == "2":
            # llama a funcion menu_usuarios de otro módulo
            gestionUsuarios.menu_usuarios()
        elif opcion == "3":
            # llama a funcion menu_prestamos de otro módulo
            print("en construcción")
            #gestionPrestamos.menu_prestamos()
        elif opcion == "4":
            print("Gracias por usar nuestra app")
            break
        else:
            print("Opción no válida. Inténtalo otra vez")
            
            
# Instancias

gestionLibros = GestionLibros()
gestionUsuarios = GestionUsuarios()
#gestionPrestamos = GestionPrestamos(gestionLibros, gestionUsuarios)
# carga el menú principal      
            
            
menu_principal(gestionUsuarios, gestionLibros)























from usuarios import GestionUsuarios
from libros import GestionLibros

def mostrar_menu(gestion_usuarios):
    while True:
        print("--Gestión Usuarios--")
        print("1: Añadir Usuario")
        print("2: Eliminar Usuario (dni)")
        print("3: Buscar Usuario (dni)")
        print("4: Mostrar todos los Usuarios")
        print("5: Salir")
    
        opcion = input("Elige una opción: ")

        if opcion == "1":
            gestion_usuarios.anadir_usuario()
        elif opcion == "2":
            gestion_usuarios.borrar_usuario()
        elif opcion == "3":
            gestion_usuarios.mostrar_usuario()
        elif opcion == "4":
            gestion_usuarios.mostrar_usuarios()
        elif opcion == "5":
            print("Bye")
            break
        else:
            print("Opción no válida")

# instancia
gestion_usuarios = GestionUsuarios()
gestion_libros = GestionLibros()

mostrar_menu(gestion_usuarios, gestion_libros)