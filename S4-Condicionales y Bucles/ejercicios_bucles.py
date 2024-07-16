# Ejercicio 1 -> Escribe un programa que imprima los números del 1 al 10 utilizando un bucle while.
i = 1
while i <= 10:
    print(i)
    i = i + 1
 

# Ejercicio 2 -> Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.
for i in range(11):
    if i == 0:
        continue
    print(i)
    

# Ejercicio 3 -> Escribe un programa que imprima los números pares del 2 al 10 utilizando un bucle for.
for i in range(2,11):
    print(i)

# Ejercicio 4 -> Escribe un programa que imprima los números impares del 1 al 9 utilizando un bucle for.
for i in range(1,11,2):
    print(i)


# Ejercicio 5 -> Escribe un programa que imprima los números del 10 al 1 utilizando un bucle while.
i = 10
while i >= 1:
    print(i)
    i = i - 1
    

# Ejercicio 6 -> Escribe un programa que imprima los números del 10 al 1 utilizando un bucle for.
for i in range(10):
    i = 10 - i 
    print(i)


# Ejercicio 7 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle for.
for i in range(1,20):
    if i <= 10:
        print(i)
    elif i > 10:
        i = 20 - i
        print(i)
  

# Ejercicio 8 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle while.
i = 1
while i <= 20: 
    if i <= 10:
        print(i)
        i = i + 1
    elif i > 10 and i <= 19:
        x = 20 - i
        print(x)
        i = i + 1
        
i = 1
while i <= 20: 
    if i <= 10:
        print(i)
    else:
        print(20-i)
    i = i + 1
            

# Ejercicio 9 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle for y un condicional.
for i in range(1,21):
    if i <= 10:
        print(i)
    elif i > 10 and i!=20:
        i = 20 - i
        print(i)



# Ejercicio 10 -> Escribe un programa que imprima los números del 1 al 10 en orden ascendente y descendente utilizando un solo bucle while y un condicional.
i = 1
while i <= 20: 
    if i <= 10:
        print(i)
        i = i + 1
    elif i > 10 and i <= 19:
        x = 20 - i
        print(x)
        i = i + 1



# Ejercicios con listas
# Ejercicio 1 -> Escribe un programa que imprima los elementos de una lista utilizando un bucle for.
familiares = ["John", "Sylvia", "Gabriela", "Nito"]
for familia in familiares:
    print(familia)


# Ejercicio 2 -> Escribe un programa que imprima los elementos de una lista utilizando un bucle while.
i = 0
familiares = ["John", "Sylvia", "Gabriela", "Nito"]
while i < len(familiares):
        print(familiares[i])
        i = i+1


# Ejercicio 3 -> Escribe un programa que imprima los elementos de una lista en orden inverso utilizando un bucle for.

familiares = ["John", "Sylvia", "Gabriela", "Nito"]
x = len(familiares) -1 #3
for familiar in familiares:
    print(familiares[x - familiares.index(familiar)])
   
   # opción 2 
familiares = ["John", "Sylvia", "Gabriela", "Nito"]
for i in range(len(familiares)-1, -1, -1):
    print(familiares[i])
    
    #opción 3
familiares = ["John", "Sylvia", "Gabriela", "Nito"]
for i in range(len(familiares)):
    print(familiares[-(i+1)])
    

# Ejercicio 4 -> Escribe un programa que imprima los elementos de una lista en orden inverso utilizando un bucle while.
i = 0
familiares = ["John", "Sylvia", "Gabriela", "Nito"]
x = len(familiares) #4
while  i < x:
    y= x-i-1
    print(familiares[y])
    i = i+1
  
 #opción 2 
i = 0
familiares = ["John", "Sylvia", "Gabriela", "Nito"]  
x = len(familiares - 1)
while i < len(familiares):
    print(familiares[x - familiares.index(familiares[i])])
    i = i + 1
    


# Ejercicios con diccionarios
# Ejercicio 1 -> Escribe un programa que imprima las claves y valores de un diccionario utilizando un bucle for.
alumnos_mate = {
    "Juan" : 6,
    "Maria": 7,
    "Pedro": 8,
    "Lucía": 10
}

for nombre, nota in alumnos_mate.items(): # alumnos_mate.items() nos devuelve [("Juan", 6), ("Maria", 7), ("Pedro", 8), ("Lucía", 10)]
    print(f"Nombre {nombre}, edad: {nota}")



# Ejercicio 2 -> Escribe un programa que imprima las claves y valores de un diccionario utilizando un bucle while.
alumnos_mate = {
    "Juan" : 6,
    "Maria": 7,
    "Pedro": 8,
    "Lucía": 10
}
i = 0
llave = list(alumnos_mate)

while i < len(llave):
    print(llave[i], ":",alumnos_mate[llave[i]])
    i = i + 1
    
# otra manera-------------------
alumnos_mate = {
    "Juan" : 6,
    "Maria": 7,
    "Pedro": 8,
    "Lucía": 10
}
i = 0
clave = list(alumnos_mate.keys())
valores = list(alumnos_mate.values())
longitud = len(alumnos_mate)

while i < longitud:
    print(clave[i])
    print(valores[i])
    i = i + 1
    

# Ejercicio 3 -> Escribe un programa que imprima las claves de un diccionario utilizando un bucle for.
alumnos_mate = {
    "Juan" : 6,
    "Maria": 7,
    "Pedro": 8,
    "Lucía": 10
}
llave = alumnos_mate.keys()
print(llave)
for claves in llave:
    print(claves)


# Ejercicio 4 -> Escribe un programa que imprima las claves de un diccionario utilizando un bucle while.
alumnos_mate = {
    "Juan" : 6,
    "Maria": 7,
    "Pedro": 8,
    "Lucía": 10
}
i = 0
llave = list(alumnos_mate)
print(llave)

while i < len(llave):
    print(llave[i])
    i = i + 1
    
##OTRA manera_______------
alumnos_mate = {
    "Juan" : 6,
    "Maria": 7,
    "Pedro": 8,
    "Lucía": 10
}




##---------------------------------------------------------##




# Más complejos
# Ejercicio 1 -> Conteo de Palabras: Dado un texto, contar la frecuencia de cada palabra y almacenar los resultados en un diccionario (if in)
import string
texto = "El rápido zorro marrón salta sobre el perro perezoso. El perro no estaba listo para eso."
#puntuaciones
texto = texto.translate(str.maketrans("","", string.punctuation))
#acentos
texto = texto.translate(str.maketrans("áéíóú", "aeiou")).lower()
#                                     
print(texto)
texto = texto.split(" ")
print(texto)
dicc_texto = {}

for palabra in texto:
    dicc_texto[palabra] = texto.count(palabra)

print(dicc_texto)



# Ejercicio 2 -> Promedio de Calificaciones: Dada una lista de estudiantes con sus calificaciones, calcular el promedio de calificaciones por estudiante y almacenar los resultados en un diccionario.
estudiantes = {
   "Ana": [85, 92, 78],
   "Luis": [79, 95, 88],
   "Marta": [92, 88, 84],
   "Carlos": [70, 75, 80]
}

Nota_promedio = {}

estudiantes_promedio = estudiantes.items()
print(estudiantes_promedio)

for estudiante, notas in estudiantes_promedio:
    promedio = sum(notas) / len(notas)
    Nota_promedio[estudiante] = promedio
    
print(Nota_promedio)
    
    

# Ejercicio 3 -> Agrupación de Elementos: Dada una lista de números, agrupar los números en un diccionario según su paridad (pares e impares).
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dicci_num = {
    "par":[], 
    "impar":[]
    }
for num in numeros:
    if num % 2 ==0:
        dicci_num["par"].append(num)
        
    else:
        dicci_num["impar"].append(num)
        
print(dicci_num)


# Ejercicio 4 -> Conteo de Caracteres: Dada una lista de palabras, contar la frecuencia de cada carácter y almacenar los resultados en un diccionario.
palabras = ["hola", "mundo", "python", "programación"]

palabra_cadena =" ".join(palabras)
import string
#puntuaciones
palabra_cadena = palabra_cadena.translate(str.maketrans("","", string.punctuation))
#acentos
palabra_cadena = palabra_cadena.translate(str.maketrans("áéíóú", "aeiou")).lower()

palabras = palabra_cadena.split()
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

# Ejercicio 5 -> Diccionario de Diccionarios: Dada una lista de estudiantes con sus calificaciones en varias asignaturas, crear un diccionario de diccionarios donde cada estudiante tiene un diccionario de asignaturas y sus calificaciones.   (if not in)
datos = [
   ("Ana", "Matemáticas", 85),
   ("Ana", "Ciencias", 92),
   ("Ana", "Historia", 78),
   ("Luis", "Matemáticas", 79),
   ("Luis", "Ciencias", 95),
   ("Luis", "Historia", 88),
   ("Marta", "Matemáticas", 92),
   ("Marta", "Ciencias", 88),
   ("Marta", "Historia", 84),
   ("Carlos", "Matemáticas", 70),
   ("Carlos", "Ciencias", 75),
   ("Carlos", "Historia", 80)
]

calificaciones = {}

for nombre, asignatura, nota in datos:
    if nombre not in calificaciones:
        calificaciones[nombre] = {}
    calificaciones[nombre][asignatura]= nota
    
print(calificaciones)


## Cómo saber si un número es primo

num1 = 10
i = 2
while i < num1:
    if num1 % i == 0:
        print (f"{num1} + no es primo")
        break
    i = i + 1
else:
    print (f"{num1} + es primo")
