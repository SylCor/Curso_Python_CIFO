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

#exportar json 
def exportar_json(databaseLista, nombreFichero):
    import os
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    # abspath: devuelve la ruta absoluta del fichero actual
    # print(directorio_actual)
    # dirname: devuelve la ruta del directorio padre/madre
    ruta_carpeta_json = os.path.join(directorio_actual,"json")
    # join: une la ruta absoluta con /json
    
    #si es la primera vez, creo la carpeta
    if not os.path.exists(ruta_carpeta_json):
        os.makedirs(ruta_carpeta_json)
        
    #escribir en el fichero json
    ruta_fichero = os.path.join(ruta_carpeta_json,nombreFichero)
    
    import json
    with open(ruta_fichero,"w", encoding="utf-8") as file:
        json.dump([libro.__dict__ for libro in databaseLista], file, ensure_ascii=False, indent=4)
        

