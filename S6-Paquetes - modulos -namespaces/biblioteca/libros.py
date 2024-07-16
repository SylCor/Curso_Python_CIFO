# Nuestra Base de Datos (temporal) para gestionar los libros
from turtle import title
import utils

libros=[]

def menu_libros():
    while True:
        print("---Gestión de Libros---")
        print("1: Añadir un libro")
        print("2: Eliminar un libro")
        print("3: Buscar libros")
        print("4: Mostrar todos los libros")
        print("5: Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            isbn = input("Introduce el ISBN del libro: ")
            genero = input("Introduce el género del libro: ")
            añadir_libro(titulo, autor, isbn, genero)
              
        if opcion == "2":
            isbn = input("Introduce el isbn del libro que quieres borrar: ")
            borrar_libro(isbn)

        if opcion == "3":
            busqueda = input("Introduce el título, autor o isbn del libro que quieres buscar: ")
            resultados = buscar_libro(busqueda, busqueda, busqueda)
            if resultados:
                print("Resultados de la búsqueda: ")
                for resultado in resultados:
                    print(f"Título: {resultado["Título: "]}, Autor: {resultado["Autor: "]}, ISBN: {resultado["isbn: "]}, Género: {resultado["Género: "]}")
            else:
                print ("No se encontraron resultados")        

        if opcion == "4":
          mostrar_libros()

        elif opcion == "5":
           break


def añadir_libro(titulo, autor, isbn, genero): #defino una lista de diccionarios de libros para irlos añadiendo a medida que se crean
    if not utils.validar_isbn_format(isbn):
       print("ISBN con formato incorrecto")
       return
    
    if not utils.validar_isbn_unique(isbn,libros):
        print("ISBN ya existente")
        return
    
    diccionario_libro = {
         "Título: " : titulo, 
         "Autor: " : autor, 
         "isbn: " : isbn, 
         "Género: " : genero}
     
    libros.append(diccionario_libro)
    print(f"libro añadido: {libros}")
     
     
def borrar_libro(isbn):
    for libro in libros:
        if libro["isbn: "] == isbn:
            libros.remove(libro)
            print (f"Libros con isbn {isbn} borrado")
            print(libros)
            return   
    print("Libro no encontrado")

def buscar_libro(titulo = None, autor= None, isbn= None): # Si no llega valor al parámetro, toma el valor nulo None. 
    resultados = []
    for libro in libros:
        if titulo and titulo.lower() == libro["Título: "].lower():
            resultados.append(libro)
        elif autor and autor.lower() == libro["Autor: "].lower():
            resultados.append(libro)
        elif isbn and isbn == libro["isbn: "]:
            resultados.append(libro)
    return resultados       

 
        
def mostrar_libros():
    if libros:
        print("Libros disponibles: ")
        for libro in libros:
            print(f"Título: {libro["Título: "]}. Autor: {libro["Autor: "]}, ISBN: {libro["isbn: "]}, Género {libro["Género: "]}")
    else:
        print("No hay libros disponibles.")
        

