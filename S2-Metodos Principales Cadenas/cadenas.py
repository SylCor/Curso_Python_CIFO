# Métodos principales de cadenas. Un método es una función
# upper(): retorna la cadena en mayúsculas
cadena ="hola"
print(cadena.upper())

# lower(): retorna la cadena en minúsculas
cadena ="HOLA"
print(cadena.lower())

# capitalize(): Convierte en mayúscula la primera letra del str
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#title(): retorna una cadena con la primera letra de cada palabra en mayúsculas
txt = "hello, and welcome to my world."
x = txt.title()
print (x)

#replace(): retorna la cadena que es reemplazada por otra subcadena
cadena = "Hola que tal";
str_replace = cadena.replace("que tal","cómo estás");
print(str_replace)

#split(): retorna una lista de palabras a partir de una cadena
str_split = "Hola cómo estás"
print(str_split.split())

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

# join(): retorna una cadena a partir de una lista
cadena = ["Hola", "que", "tal"]
print(" ".join(cadena)) #"Hola que tal" se pone el " " antes del .join para que haya el espacio entre palabras

# strip(): Retorna la cadena eliminando los esapcios por el principio y el final
cadena = "    Hola ke ase             "
print(cadena.strip())  # strip solo es por los dos lados
print(cadena.rstrip())
# rstrip() o lstrip() l es para izquierda o el principio y r por el final o la derecha

# startwith: Retorna un True si la cadena comienza por una subcadena
cadena = "Ola ke ase"
print(cadena.startswith("ola")) #False
print(cadena.startswith("Ola")) #True
print(cadena.startswith("O")) #True

# ejemplo validar telefono (comience por 6/7/9)
datos_alumnos = {} #diccionario vacío
telefono_validar = "689456123"
if telefono_validar.startswith("6") or telefono_validar.startswith("7")  or telefono_validar.startswith("9") :
    print("Teléfono OK")
    datos_alumnos["telefono"] = telefono_validar
    print(datos_alumnos)
else:
    print("Teléfono Malo")
    
# endswith(): Retorna un True si la cadena termina por una subcadena
cadena = "Ola ke ase"
print(cadena.startswith("ase")) #True

#find(): Retorna la posición de una subcadena en una cadena
cadena = "Hola que tal"
print(cadena.find("que")) #que comienza en la 5ta posición

#count(): retorna el número de veces que una subcadena aparece en una cadena
cadena = "Hola que tal, que más"
print(cadena.count("que"))  #"que" sale dos veces


#------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------
