import utils

class Usuario:
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        
class GestionUsuarios:
    def __init__(self):
        self.usuariosDB = []
        
    def menu_usuarios(self):
        while True:
            print("---Gestión de Usuarios---")
            print("1: Añadir un usuario")
            print("2: Eliminar un usuario")
            print("3: Buscar usuario")
            print("4: Mostrar todos los usuarios")
            print("5: Generar JSON de todos los usuarios")
            print("6: Volver al menú principal")
        
            opcion = input("Elige una opción: ")
        
            if opcion == "1":
                nombre = input("Introduce el nombre del usuario: ")
                apellido = input("Introduce el apellido del usuario: ")
                dni = input("Introduce el DNI del usuario: ")
                email = input("Introduce el email del usuario: ")
                self.anadir_usuario(nombre, apellido, dni, email)
              
            if opcion == "2":
                dni = input("Introduce el DNI del usuario que quieres borrar: ")
                self.borrar_usuario(dni)

            if opcion == "3":
                busqueda = input("Introduce el DNI o email del usuario que quieres buscar: ")
                resultados = self.buscar_usuario( busqueda, busqueda)
                if resultados:
                    print("Resultados de la búsqueda: ")
                    print()
                    for resultado in resultados:
                        print(f"Nombre: {resultado.nombre}, Apellido: {resultado.apellido}, DNI: {resultado.dni}, Email: {resultado.email}")
                else:
                    print ("No se encontraron resultados")
                    print()        

            if opcion == "4":
                self.mostrar_usuarios()
                
            if opcion == "5":
                utils.exportar_json(self.usuariosDB,"usuarios.json")
                print("Se ha generado el archivo JSON con todos los usuarios")

            elif opcion == "6":
                break

    def anadir_usuario(self, nombre, apellido, dni, email):
        if not utils.validar_dni_format(self,dni):
            print("DNI con formato incorrecto")
            print()
            return
    
        if not utils.validar_dni_unique(self, dni, self.usuariosDB):
            print("DNI ya registrado")
            print()
            return
    
        usuario = Usuario(nombre, apellido, dni, email)
        self.usuariosDB.append(usuario)
    
        print(f"usuario añadido: {usuario.__dict__}")
        print()
    
        # def check_dni():
        #     dni = input("Introduce el DNI del usuario: ")
    
        #     for usuario in usuarios:
        #         while usuario["DNI: "] == dni:
        #             print("Usuario existente")
        #             dni = input("Introduce DNI")
        #     return dni    
        

    def borrar_usuario(self,dni):
        for usuario in self.usuariosDB:
            if usuario.dni == dni:
                self.usuariosDB.remove(usuario)
                print (f"Usuario con DNI {dni} borrado")
                print(self.usuariosDB)
                print()
                return   
        print("Usuario no encontrado")
        print()

    def buscar_usuario(self, dni= None, email= None): # Si no llega valor al parámetro, toma el valor nulo None. 
        resultados = []
        for usuario in self.usuariosDB:
            if dni and dni.upper() == usuario.dni.upper():
                resultados.append(usuario)
            elif email and email.lower() == usuario.email.lower():
                resultados.append(usuario)
        else:
            print("Datos introducidos incorrectos")
            print()
        return resultados       

        
    def mostrar_usuarios(self):
        if self.usuariosDB:
            print("Usuarios disponibles: ")
            print()
            for usuario in self.usuariosDB:
                print(f"Nombre: {usuario.nombre}. Apellido: {usuario.apellido}, DNI: {usuario.dni}, email {usuario.email}")
                print()
        else:
            print("No hay usuarios disponibles.")
            print()
        

    def buscador_usuario(self, dni):
        for usuario in self.usuariosDB:
            if usuario.dni == dni:
                return True
        return False