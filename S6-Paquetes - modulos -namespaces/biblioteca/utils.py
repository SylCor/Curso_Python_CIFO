# Funciones de validacion
#ISBN

def validar_isbn_format(isbn):
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False

def validar_isbn_unique(isbn, libros):
    for libro in libros:
        if libro["isbn"] == isbn:
            return False
    return True


# DNI
def validar_dni_format(dni):
    digitosDNI = dni[:8]
    letraDNI = dni[-1] 
    if len(dni) != 9:
        return False
    elif not digitosDNI.isdigit() or not letraDNI.isalpha():
        return False
    else: 
        return True 
        
def validar_dni_unique(dni, usuarios):
    for usuario in usuarios:
        if usuario["DNI: "] == dni:
            return True
    return False

#prestamo
def validar_libro_prestado(isbn, prestamos):
    for prestamo in prestamos:
        if prestamo["ISBN"] == isbn:
            return False
    return True
        