# Ejercicio 1 -> Escribe una función que reciba dos números y devuelva el mayor de los dos.
def cual_es_mayor(a,b):
    if a == b:
        print("Son iguales")
    elif a > b:
        print(f"{a}  es mayor")
    else:
        print(f"{b}  es mayor")
        
cual_es_mayor(9,5)


# Ejercicio 2 -> Escribe una función que reciba dos números y devuelva el menor de los dos.
def cual_es_mayor(a,b):
    if a == b:
        print("Son iguales")
    elif b > a:
        print(f"{a}  es menor")
    else:
        print(f"{b}  es menor")
        
cual_es_mayor(9,5)



# Ejercicio 3 -> Escribe una función que reciba un número y devuelva True si es par y False si es impar.
def par_impar(num):
    if num %2 == 0:
        return True
    else:
        return False

print(par_impar(2))


# Ejercicio 4 -> Escribe una función que reciba un número y devuelva True si es impar y False si es par.
def par_impar(num):
    if num %2 == 0:
        return False
    else:
        return True

print(par_impar(3))


# Ejercicio 5 -> Escribe una función que reciba un número y devuelva True si es positivo y False si es negativo.
def posi_nega(a):
    if a < 0:
        return False
    elif a >=0:
        return True

print(posi_nega(2))


# Ejercicio 6 -> Escribe una función que reciba un número y devuelva True si es negativo y False si es positivo.
def posi_nega(a):
    if a < 0:
        return True
    elif a >=0:
        return False

print(posi_nega(2))


# Ejercicio 7 -> Escribe una función que reciba un número y devuelva True si es cero y False si no lo es.
def es_cero(a):
    if a == 0:
        return True
    else:
        return False

print(es_cero(0))


# Ejercicio 8 -> Escribe una función que reciba un número y devuelva True si es un número entero y False si no lo es.
def entero(a):
    if type(a) == int:
        return True
    elif type(a) == float:
        return False
    else:
        print ("Ni chicha, ni limonada")

print(entero(3))


# Ejercicio 9 -> Escribe una función que reciba un número y devuelva True si es un número decimal y False si no lo es.
def entero(a):
    if type(a) == int:
        return False
    elif type(a) == float:
        return True
    else:
        print ("Ni chicha, ni limonada")

print(entero(3))


# Ejercicio 10 -> Escribe una función que reciba un número y devuelva True si es un número positivo y decimal y False si no lo es. 
def p_n_e_d(a):
    if a >=0 and type(a)==float:
        return True
    else:
        return False
    
print(p_n_e_d(3))

# Ejercicio 11 -> Escribe una función que reciba un número y devuelva True si es un número negativo y decimal y False si no lo es. 
def p_n_e_d(a):
    if a <0 and type(a)==float:
        return True
    else:
        return False
    
print(p_n_e_d(-3.1))


# Ejercicio 12 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero y False si no lo es.
def p_n_e_d(a):
    if a >= 0 and type(a)==int:
        return True
    else:
        return False
    
print(p_n_e_d(3))


# Ejercicio 13 -> Escribe una función que reciba un número y devuelva True si es un número negativo y entero y False si no lo es.
def p_n_e_d(a):
    if a < 0 and type(a)==int:
        return True
    else:
        return False
    
print(p_n_e_d(-3))


 # Ejercicio 14 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero o decimal y False si no lo es.
def p_n_e_d(a):
    if a >= 0 and type(a)==int:
        return True
    if a >= 0 and type(a)== float:
        return True
    else:
        return False
    
print(p_n_e_d(3))
 
 
# Ejercicio 15 -> Escribe una función que reciba un número y devuelva True si es un número negativo y entero o decimal y False si no lo es.
def p_n_e_d(a):
    if a < 0 and type(a)==int:
        return True
    if a < 0 and type(a)== float:
        return True
    else:
        return False
    
print(p_n_e_d(-3.1))


# Ejercicio 16 -> Escribe una función que reciba un número y devuelva True si es un número entero o decimal y False si no lo es.
def ent_dec(a):
    if type(a) == int or type(a) == float:
        return True
    else:
        return False

print(ent_dec(3))


# Ejercicio 18 -> Escribe una función que reciba un número y devuelva True si es un número positivo y entero o decimal y False si no lo es.
def ent_dec(a):
    if a >= 0 and type(a) == int:
        return True
    if a >= 0 and type(a) == float:
        return True
    else:
        return False

print(ent_dec(10))

##Más complejos:
# Escribe una función contar_palabras que reciba una cadena de texto y devuelva un diccionario con el conteo de cada palabra en el texto.

x="Saber cuantas palabras se repiten en esta frase, la frase tiene varias palabras y hay que contarlas todas. todas las palabras en las palabras que tiene la frase. Hay palabras aquí."

def contar_palabras(texto):
    import string
    dicc_texto = {}

    texto = texto.translate(str.maketrans("","", string.punctuation))
    texto = texto.translate(str.maketrans("áéíóú", "aeiou")).lower()
    texto = texto.split(" ")
    texto.sort()
    print(texto)
    
    for palabra in texto:
        dicc_texto[palabra] = texto.count(palabra)
    return dicc_texto

print(contar_palabras(x))


# Escribe una función frecuencia_caracteres que reciba una cadena de texto y devuelva un diccionario con el conteo de cada carácter en el texto

def cuenta_letras(palabras):
    import string
#puntuaciones
    palabras = palabras.translate(str.maketrans("","", string.punctuation))
#acentos
    palabras = palabras.translate(str.maketrans("áéíóú", "aeiou")).lower()

    print(palabras)
    palabras = palabras.split()
    print(palabras)

    frecuencia_caracteres = {}
    caracteres = []
    for pala in palabras:
        for caract in pala:
            caracteres.append(caract)
    print(caracteres)

    for c_c in caracteres:
        frecuencia_caracteres[c_c] = caracteres.count(c_c)
    print(frecuencia_caracteres)

cuenta_letras("hola mundo python programación")

# Escribe una función analizar_palabras que reciba una cadena de texto y devuelva un diccionario con la longitud de cada palabra como clave y la lista de palabras de esa longitud como valor.
frase = "Esto es una lista de palabras"

def cuenta_palabras(lista_palabras):

    lista_palabras = lista_palabras.split()
    print(lista_palabras)

    diccionario_longitud ={}

    for palabra in lista_palabras:
        diccionario_longitud[palabra] = len(palabra)
    print(diccionario_longitud)

cuenta_palabras(frase)

# Escribe una función contar_vocales_consonantes que reciba una cadena de texto y devuelva un diccionario con el conteo de vocales y consonantes en el texto.


def contar_vocales_consonantes(cadena_palabras):
    
    cadena_palabras = cadena_palabras.lower()
    cadena_palabras = cadena_palabras.split()
    print(cadena_palabras)

    diccionario_letras = {
        "vocales" : 0,
        "consonantes" : 0
    }

    todas_letras = []

    for palabra in cadena_palabras:
        for letra in palabra:
            todas_letras.append(letra)
    print(todas_letras)

    for letrita in todas_letras:
        if letrita == "a" or letrita == "e" or letrita == "i" or letrita == "o" or letrita == "u":
            diccionario_letras["vocales"] +=1
        else:
            diccionario_letras["consonantes"] +=1
    print(diccionario_letras)

contar_vocales_consonantes("Vamos a contar letras xyz")