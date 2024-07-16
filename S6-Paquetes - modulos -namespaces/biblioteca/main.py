import libros 
import usuarios
import prestamos

def menu_principal():
    while True:
        
        print("---Gestión Biblioteca---")
        print("1: Gestión de libros")
        print("2: Gestión de usuarios")
        print("3: Gestión de préstamos")
        print("4: Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            # llama a funcion menu_libros de otro módulo
            libros.menu_libros()
        elif opcion == "2":
            # llama a funcion menu_usuarios de otro módulo
            usuarios.menu_usuarios()
        elif opcion == "3":
            # llama a funcion menu_prestamos de otro módulo
            prestamos.menu_prestamos()
        elif opcion == "4":
            print("Gracias por usar nuestra app")
            break
        else:
            print("Opción no válida. Inténtalo otra vez")
            
menu_principal()

