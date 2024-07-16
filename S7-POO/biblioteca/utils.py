# Funciones de validacion
#ISBN

def validar_isbn_format(self,isbn):
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False

def validar_isbn_unique(self, isbn, librosDB):
    for libro in librosDB:
        if libro.isbn == isbn:
            return False
    return True


# DNI
def validar_dni_format(self, dni):
    digitosDNI = dni[:8]
    letraDNI = dni[-1] 
    if len(dni) != 9:
        return False
    elif not digitosDNI.isdigit() or not letraDNI.isalpha():
        return False
    else: 
        return True 
        
def validar_dni_unique(self, dni, usuariosDB):
    for usuario in usuariosDB:
        if usuario.dni == dni:
            return False
    return True

#prestamo
def validar_libro_prestado(self, isbn, prestamosDB):
    for prestamo in prestamosDB:
        if prestamo.isbn == isbn:
            return False
    return True

