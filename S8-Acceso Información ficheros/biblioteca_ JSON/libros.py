import utils

class Libro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

# Clase que contiene la gestión de todas las acciones sobre la entidad Libro
class GestionLibros:
    def __init__(self):
        self.librosDB = [] # data base

    # Métodos de gestion libros
    # 1 - Método de imprimir el menú de libros
    def menu_libros(self):
        while True:
            print("---Gestión de Libros---")
            print("1: Añadir un libro")
            print("2: Eliminar un libro")
            print("3: Buscar libros")
            print("4: Mostrar todos los libros")
            print("5: Generar JSON de todos los libros")
            print("6: Volver al menú principal")
        
            opcion = input("Elige una opción: ")
        
            if opcion == "1":
                titulo = input("Introduce el título del libro: ")
                autor = input("Introduce el autor del libro: ")
                isbn = input("Introduce el ISBN del libro: ")
                genero = input("Introduce el género del libro: ")
                self.anadir_libro(titulo, autor, isbn, genero)
                
            elif opcion =="2":
                isbn = input("Introduce el isbn del libro que quieres borrar: ")
                self.borrar_libro(isbn)    
                
            if opcion == "3":
                busqueda = input("Introduce el título, autor o isbn del libro que quieres buscar: ")
                resultados = self.buscar_libro(busqueda, busqueda, busqueda)
                if resultados:
                    print("Resultados de la búsqueda: ")
                    print()
                    for resultado in resultados:
                        print(f"Título: {resultado.titulo}, Autor: {resultado.autor}, ISBN: {resultado.isbn}, Género: {resultado.genero}")
                        print()
                else:
                    print ("No se encontraron resultados")    
                    print()    

            if opcion == "4":
                self.mostrar_libros()
                
            if opcion == "5":
                utils.exportar_json(self.librosDB,"libros.json")
                print("Se ha generado el archivo JSON con todos los libros")

            elif opcion == "6":
                break

    def anadir_libro(self, titulo, autor, isbn, genero): 
        if not utils.validar_isbn_format(self, isbn):
            print("ISBN con formato incorrecto")
            print()
            return
    
        if not utils.validar_isbn_unique(self, isbn, self.librosDB):
            print("ISBN ya existente")
            print()
            return
    
        libro = Libro( titulo, autor, isbn, genero)
        self.librosDB.append(libro)
        print(f"Libro añadido: {libro.__dict__}")
        print()
     
     
    def borrar_libro(self,isbn):
        for libro in self.librosDB:
            if libro.isbn == isbn:
                self.librosDB.remove(libro)
                print (f"Libros con isbn {isbn} borrado")
                print(self.librosDB)
                print()
                return   
        print("Libro no encontrado")
        print()
        
    def buscar_libro(self, titulo = None, autor= None, isbn= None): 
        resultados = []
        for libro in self.librosDB:
            if titulo and titulo.lower() == libro.titulo.lower():
                resultados.append(libro)
            elif autor and autor.lower() == libro.autor.lower():
                resultados.append(libro)
            elif isbn and isbn == libro.isbn:
                resultados.append(libro)
        return resultados     
    
    def mostrar_libros(self):
        if self.librosDB:
            print("Libros disponibles: ")
            print()
            for libro in self.librosDB:
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}, Género {libro.genero}")
                print()
        else:
            print("No hay libros disponibles.")  
            print()

 
    def buscador_libro(self, isbn):
        for libro in self.librosDB:
            if libro.isbn == isbn:
                return True
        return False
            
