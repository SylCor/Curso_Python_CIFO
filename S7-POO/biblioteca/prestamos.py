import utils
from datetime import datetime

class Prestamo:
    def __init__(self, dni, isbn): # poner fecha si se quiere como input
        self.dni = dni
        self.isbn = isbn
        self.fecha = datetime.now().date()
        

class GestionPrestamos:
    def __init__(self, gestionLibros, gestionUsuarios):
        self.prestamosDB=[]
        self.gestionLibros = gestionLibros
        self.gestionUsuarios = gestionUsuarios
        

    def menu_prestamos(self):
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
                #fecha = input("Introduce la fecha libro en formato XX/XX/XXXX: ")
                self.anadir_prestamo(dni, isbn) # si quiero input fecha pongo "fecha"
              
            if opcion == "2":
                isbn = input("Introduce el ISBN del libro que quieres retornar: ")
                self.borrar_libro(isbn)

            if opcion == "3":
                dni = input("Introduce el DNI del usuario: ")
                self.buscar_usuario(dni)      

            if opcion == "4":
                self.mostrar_prestamos()

            elif opcion == "5":
                break


    def anadir_prestamo(self,dni, isbn): #fecha
        if not utils.validar_dni_format(self,dni):
            print("DNI con formato incorrecto")
            print()
            return
        
        if not utils.validar_isbn_format(self, isbn):
            print("ISBN con formato incorrecto")
            print()
            return
        
        if not utils.validar_isbn_unique(self, isbn, self.prestamosDB):
            print("ISBN ya existente")
            print()
            return

        if not self.gestionLibros.buscador_libro(isbn):
            print("No se ha encontrado el libro.")
            return
        
        if not self.gestionUsuarios.buscador_usuario(dni):
            print ("No se ha encontrado el usuario.")
            return
        
    
        prestamo = Prestamo(dni, isbn) #fecha
        self.prestamosDB.append(prestamo)
        print(f"usuario y libro prestado añadido: {prestamo.__dict__}")   
        print()  
     
    def borrar_libro(self,isbn):
  
        for prestamo in self.prestamosDB:
            if prestamo.isbn == isbn:
                self.prestamosDB.remove(prestamo)
                print (f"Libros con ISBN {isbn} borrado")
                print()
                print(f"Libros prestados después de devolución del libro con ISBN: {isbn}")
                for prestamo in self.prestamosDB:
                    print(f"DNI: {prestamo.dni}, ISBN: {prestamo.isbn}, Fecha: {prestamo.fecha}")
                return  
        else:     
            print(f"Libro con ISBN {isbn} no encontrado")
            print()
    
    
    def buscar_usuario(self,dni): 
        if not self.prestamosDB:
            print("No hay préstamos en la lista")
        else:
            for prestamo in self.prestamosDB:
                if dni == prestamo.dni:
                    print(f"DNI: {prestamo.dni}, ISBN: {prestamo.isbn}, Fecha: {prestamo.fecha}")
                    

                
    def mostrar_prestamos(self):
        if self.prestamosDB:
            print("Préstamos realizados: ")
            for prestamo in self.prestamosDB:
                print(f"DNI: {prestamo.dni}, ISBN: {prestamo.isbn}, Fecha: {prestamo.fecha}")
                
        else:
            print("No se han realizado préstamos")
            print()

   