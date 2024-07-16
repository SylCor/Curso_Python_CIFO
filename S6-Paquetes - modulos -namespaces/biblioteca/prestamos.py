import utils
prestamos=[]

def menu_prestamos():
    while True:
        print("---Gestión de Préstamos---")
        print("1: Registrar un préstamo")
        print("2: Retornar un libro")
        print("3: Mostrar préstamos usuario")
        print("4: Mostrar préstamos")
        print("5: Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            dni = input("Introduce el DNI del usuario: ")
            isbn = input("Introduce el ISBN del libro: ")
            fecha = input("Introduce la fecha libro en formato XX/XX/XXXX: ")
            añadir_prestamo(dni, isbn, fecha)
              
        if opcion == "2":
            isbn = input("Introduce el isbn del libro que quieres retornar: ")
            borrar_libro(isbn)

        if opcion == "3":
            dni = input("Introduce el DNI del usuario: ")
            buscar_usuario(dni)      

        if opcion == "4":
          mostrar_prestamos()

        elif opcion == "5":
           break


def añadir_prestamo(dni, isbn, fecha):

    if not utils.validar_libro_prestado(isbn, prestamos):
       print("libro prestado")
       return
    
    diccionario_prestamos = {
         "DNI" : dni, 
         "ISBN" : isbn, 
         "fecha" : fecha}
     
    prestamos.append(diccionario_prestamos)
    print(f"usuario y libro prestado añadido: {prestamos}")
     
     
def borrar_libro(isbn):
    for prestamo in prestamos:
        if prestamo["ISBN"] == isbn:
            prestamos.remove(prestamo)
            print (f"Libros con ISBN {isbn} borrado")
            print(prestamos)
            return   
    print("Libro no encontrado")


def buscar_usuario(dni): 
    print(dni)
    for prestamo in prestamos:
        if dni not in prestamo["DNI"]:
            print("DNI no existe, usuario sin préstamos")
        elif dni == prestamo["DNI"]:
            print(f"DNI: {prestamo["DNI"]}, ISBN: {prestamo["ISBN"]}, Fecha: {prestamo["fecha"]}")
        else:
            print("Usuario sin libro prestado")
       

        
def mostrar_prestamos():
    if prestamos:
        print("Préstamos realizados: ")
        for prestamo in prestamos:
            print(f"DNI: {prestamo["DNI"]}, ISBN: {prestamo["ISBN"]}, Fecha: {prestamo["fecha"]}")
    else:
        print("No se han realizado préstamos")
        

