import utils

class Libro:
    # constructor
    def __init__(self, isbn, titulo, autor, genero):
        self.isbn= isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

class GestionLibros:
    def menu_libros(self):
        while True:
            print("---Gestión de Libros---")
            print("1: Añadir un libro")
            print("2: Eliminar un libro")
            print("3: Buscar un libro")
            print("4: Mostrar todos los libros")
            print("5: Volver al menú principal")
        
            opcion = input("Elige una opción: ")
        
            if opcion == "1":
                isbn = input("Introduce el ISBN del libro: ")
                titulo = input("Introduce el Título del libro: ")
                autor = input("Introduce el Autor del libro: ")
                genero = input("Introduce el Género del libro: ")
                self.anadir_libro(isbn,titulo,autor,genero)

            if opcion == "2":
                isbn = input("Introduce el ISBN del libro que quiere borrar: ")
                self.borrar_libro(isbn)
                
            if opcion == "3":
                isbn = input("Introduce el ISBN del libro que quiere buscar: ")
                self.mostrar_libro(isbn)
            
            if opcion =="4":
                self.mostrar_libros()

            elif opcion == "5":
                break


  # AÑADIR 
    def anadir_libro(self,isbn,titulo,autor,genero):
        # TODO: validar estos datos
        libro = Libro(isbn, titulo, autor, genero)
        utils.set_data_mysql(libro,"libros")
        print("usuario insertado con éxito!")

    # BORRAR
    def borrar_libro(self,isbn):
        
        if  utils.find_user_mysql(isbn):
            utils.delete_user_mysql(isbn)
            print(f"Libro con ISBN {isbn} eliminado correctamente")
        else:
            print(f"Libro con ISBN {isbn} no registrado")
    
    # MOSTRAR UNO
    def mostrar_libro(self,isbn):
        
        if utils.find_user_mysql(isbn):
            print(utils.find_user_mysql(isbn))
        else:
            print("No se ha encontrado el libro con ISBN " + isbn)
        
    # MOSTRAR TODOS
    def mostrar_libross(self):
        if not utils.get_users_mysql():
            print("No hay usuarios registrados")
        else:
            print(utils.get_users_mysql())


