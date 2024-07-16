# Nuestra Base de Datos (temporal) para gestionar los usuarios

import utils
usuarios=[]

def menu_usuarios():
    while True:
        print("---Gestión de Usuarios---")
        print("1: Añadir un usuario")
        print("2: Eliminar un usuario")
        print("3: Buscar usuario")
        print("4: Mostrar todos los usuarios")
        print("5: Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Introduce el nombre del usuario: ")
            apellido = input("Introduce el apellido del usuario: ")
            dni = input("Introduce el DNI del usuario: ")
            #dni = check_dni()
            email = input("Introduce el email del usuario: ")
            añadir_usuario(nombre, apellido, dni, email)
              
        if opcion == "2":
            dni = input("Introduce el DNI del usuario que quieres borrar: ")
            borrar_usuario(dni)

        if opcion == "3":
            busqueda = input("Introduce el DNI o email del usuario que quieres buscar: ")
            resultados = buscar_usuario( busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for resultado in resultados:
                    print(f"Nombre: {resultado["Nombre: "]}, Apellido: {resultado["Apellido: "]}, DNI: {resultado["DNI: "]}, Email: {resultado["email: "]}")
            else:
                print ("No se encontraron resultados")        

        if opcion == "4":
          mostrar_usuarios()

        elif opcion == "5":
           break

def añadir_usuario(nombre, apellido, dni, email): #defino una lista de diccionarios de usuarios para irlos añadiendo a medida que se crean
    
    if not utils.validar_dni_format(dni):
        print("DNI con formato incorrecto")
        return
    
    if not utils.validar_dni_unique(dni, usuarios):
        print("DNI ya registrado")
        return
    
    diccionario_usuario = {
        "Nombre: " : nombre, 
        "Apellido: " : apellido, 
        "DNI: " : dni, 
        "email: " : email}
     
    usuarios.append(diccionario_usuario)
    print(f"usuario añadido: {usuarios}")
    
# def check_dni():
#     dni = input("Introduce el DNI del usuario: ")
    
#     for usuario in usuarios:
#         while usuario["DNI: "] == dni:
#             print("Usuario existente")
#             dni = input("Introduce DNI")
#     return dni    
        

def borrar_usuario(dni):
    for usuario in usuarios:
        if usuario["DNI: "] == dni:
            usuarios.remove(usuario)
            print (f"Usuario con DNI {dni} borrado")
            print(usuarios)
            return   
    print("Usuario no encontrado")

def buscar_usuario(dni= None, email= None): # Si no llega valor al parámetro, toma el valor nulo None. 
    resultados = []
    for usuario in usuarios:
        if dni and dni.upper() == usuario["DNI: "].upper():
            resultados.append(usuario)
        elif email and email.lower() == usuario["email: "].lower():
            resultados.append(usuario)
    else:
        print("Datos introducidos incorrectos")
    return resultados       

        
def mostrar_usuarios():
    if usuarios:
        print("Usuarios disponibles: ")
        for usuario in usuarios:
            print(f"Nombre: {usuario["Nombre: "]}. Apellido: {usuario["Apellido: "]}, DNI: {usuario["DNI: "]}, email {usuario["email: "]}")
    else:
        print("No hay usuarios disponibles.")
        

