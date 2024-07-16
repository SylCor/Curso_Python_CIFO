import utils

class Usuario:
    # constructor
    def __init__(self, dni, nombre, email, contrasena):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

class GestionUsuarios:
    def menu_usuarios(self):
        while True:
            print("---Gestión de Usuarios---")
            print("1: Añadir un usuario")
            print("2: Eliminar un usuario")
            print("3: Buscar usuario")
            print("4: Mostrar todos los usuarios")
            print("5: Volver al menú principal")
        
            opcion = input("Elige una opción: ")
        
            if opcion == "1":
                dni = input("Introduce tu dni: ")
                nombre = input("Introduce tu nombre: ")
                email = input("Introduce tu email: ")
                contrasena = input("Introduce tu password: ")
                self.anadir_usuario(dni,nombre,email,contrasena)

            if opcion == "2":
                dni = input("Introduce el dni del usuario que quiere borrar: ")
                self.borrar_usuario(dni)
                
            if opcion == "3":
                dni = input("Introduce el dni del usuario que quiere buscar: ")
                self.mostrar_usuario(dni)
            
            if opcion =="4":
                self.mostrar_usuarios()

            elif opcion == "5":
                break
    
    
    # AÑADIR 
    def anadir_usuario(self,dni,nombre,email,contrasena):
        # TODO: validar estos datos
        usuario = Usuario(dni, nombre, email, contrasena)
        utils.set_data_mysql(usuario, "usuarios")
        print("usuario insertado con éxito!")

    # BORRAR
    def borrar_usuario(self,dni):
        
        if  utils.find_user_mysql(dni):
            utils.delete_user_mysql(dni)
            print(f"Usuario con dni {dni} eliminado correctamente")
        else:
            print(f"Usuario con dni {dni} no registrado")
    
    # MOSTRAR UNO
    def mostrar_usuario(self,dni):
        
        if utils.find_user_mysql(dni):
            print(utils.find_user_mysql(dni))
        else:
            print("No se ha encontrado el usuario con dni " + dni)
        
    # MOSTRAR TODOS
    def mostrar_usuarios(self):
        if not utils.get_users_mysql():
            print("No hay usuarios registrados")
        else:
            print(utils.get_users_mysql())


