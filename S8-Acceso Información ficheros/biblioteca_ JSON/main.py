from libros import GestionLibros
from usuarios import GestionUsuarios
from prestamos import GestionPrestamos

def menu_principal(gestionLibros, gestionUsuarios, gestionPrestamos):
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
            gestionPrestamos.menu_prestamos()
        elif opcion == "4":
            print("Gracias por usar nuestra app")
            break
        else:
            print("Opción no válida. Inténtalo otra vez")
            
            
# Instancias

gestionLibros = GestionLibros()
gestionUsuarios = GestionUsuarios()
gestionPrestamos = GestionPrestamos(gestionLibros, gestionUsuarios)
# carga el menú principal      
            
            
menu_principal(gestionLibros, gestionUsuarios, gestionPrestamos)



