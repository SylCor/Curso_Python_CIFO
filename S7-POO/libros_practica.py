class Libro:
    def __init__(self, titulo, autor, isbn, genero):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.libroPrestado = False
        
    def isLibroPrestado(self):
        self.libroPrestado = True
        
libro1 = Libro("Hola", "Yo", "1234", "drama")
libro2 = Libro("Hola", "Tu", "5678", "terror")

librosx = []
librosx.append(libro1.__dict__)
librosx.append(libro2.__dict__)
print(librosx)

print()

libro1.isLibroPrestado()
print(librosx)


class GestionLibros:
    def __init__(self):
        self.libros = []
        
        
