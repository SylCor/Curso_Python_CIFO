import utils

class Usuario:
    # constructor
    def __init__(self, dni, nombre, email, contrasena):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

class GestionUsuarios:
    # AÑADIR
    def anadir_usuario(self):
        dni = input("Introduce tu dni: ")
        nombre = input("Introduce tu nombre: ")
        email = input("Introduce tu email: ")
        contrasena = input("Introduce tu password: ")
        # TODO: validar estos datos
        usuario = Usuario(dni, nombre, email, contrasena)
        utils.set_data_mysql(usuario)
        print("usuario insertado con éxito!")

    # BORRAR
    def borrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if  utils.find_data_mysql(dni):
            utils.delete_data_mysql(dni)
            print(f"Usuario con dni {dni} eliminado correctamente")
        else:
            print(f"Usuario con dni {dni} no registrado")
    
    # MOSTRAR UNO
    def mostrar_usuario(self):
        dni = input("Introduce el dni del usuario: ")
        if utils.find_data_mysql(dni):
            print(utils.find_data_mysql(dni))
        else:
            print("No se ha encontrado el usuario con dni " + dni)
        
    # MOSTRAR TODOS
    def mostrar_usuarios(self):
        if not utils.get_data_mysql():
            print("No hay usuarios registrados")
        else:
            print(utils.get_data_mysql())


