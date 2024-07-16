print ("Hola") 
# Probando comentarios
# Otro comentario


# Indentacion
if 5 > 2:
        print("Cinco es mayor que dos") # correcto
# print("Cinco es mayor que dos") incorrecto

# Python es un lenguaje dinámicamente tipado
        # Esto significa que el tipo es una variable que se determina en tiempo de ejecución y no es necesario declarar explicitamente el tipo de variable al definirla

x = 5 # ya python sabe que "x" variable es numérica y entero
y = 3.14 # "y" es un flotante
z = "Hola" # es una cadena (cadena de texto) - String

print(x)
print(type(x))
print(type(y))
print(type(z))

# Comprobación de tipos de ejecución
def sumar(a, b): #definición de la función
        return a+b #retorno valor de la suma de los parámetros

sumar (2,2) #llamada
print (sumar (2,2)) #llamada e impresión : 4

#Dinamicamente tipado:
#ventajas:
# - Mayor flexibilidad y rapidez en el desarrollo
# - Código más conciso y fácil de leer

#desventajas:
# - Mayor riesgo de errores
# - Más difícil de mantener y depurar

#Estaticamente tipado:
#ventajas:
# - Robustez en el código. Mejor manejo de errores

#desventajas:
# - Mayor desarrollo de código

#----------------------------
# Def Variable: Un contenedor que tiene nombre propio, que nos permite almacenar diferentes tipos de datos. Podemos leer, escribir, borrar y actualizar esos datos.. 
# Tipos de datos

# Numéricos
entero = 10 # declaro la variable con nombre "entero" y la inicializo a un valor entero 10
print (entero)

decimal = 10.5 
print (decimal)

# Cadenas / String
saludo = "Hola Mundo!"
print(saludo)

# Booleados
verdadero = True
falso = False
print(falso)

# Listas
lista = [1, 2, 3, "cuatro", 5.0, True, ["cosa", "cosa1"]]
print(lista)
        # Accceso a un determinado dato por posición
        # El primer valor de posición es el 0
print(lista[0])
        # el último valor de posición es el 5
print(lista[5])
print(lista[6][1]) #cuando hay una lista dentro de una lista, para llamar e imprimir así

#Tuplas
tupla = (1, 2, 3, "cuatro", 5.0, True)
        # El mismo acceso para las Tuplas
print(tupla[3])

# DIFERENCIA ENTRE LISTA Y TUPLA
        #Lista: Es mutable, podemos modificar sus datos
# Ejemplo:
lista[5] = False
print(lista)
        #Tuplas: Es inmutable, NO podemos modificar sus datos
# Ejemplo:
 #tupla[5]= False
 #print (tupla[5])

#Diccionarios (es mutable)
diccionario = {"clave1" : "valor1",
               "clave2" : "valor2",
               "clave3" : {
                       "clave3-1" : "valor3-1"}}
# accedo a "valor1"
print(diccionario["clave1"])
print(diccionario["clave3"]["clave3-1"])

alumnos_py = {"nombre" : "valor1",
              "apellido" : "valor2",
              "NIE" : "valor3",
              "edad" : "valor4"}

datos = ("valor1", "valor2", "valor3", "valor4")

valor1 = "Sylvia"
valor2 = "Corriere"
valor3 = "Y4449750T"
valor4 = 37

# EJEMPLO alumnos = [{1},{2},{3}] grupo de objetos (datos) de cada alumno. un diccionario lleno de listas de alumnos
alumnos = [{
        "nombre" : "Alumno1",
        "email" : "email@email.com",
        "fecha_nac" : "10/10/1990",
        "titulacion" : True,
        "nota_curso" : 8.4,
        "contenido_nota" : {
                "UF1-> Introd" : 7.45,
                "UF2" : 8.0,   
        }
},{
        "nombre" : "Alumno2",
        "email" : "email2@email.com",
        "fecha_nac" : "10/10/1990",
        "titulacion" : True,
        "nota_curso" : 8.4,
        "contenido_nota" : {
                "UF1-> Introd" : 7.45,
                "UF2" : 8.0,
        }

},{
        "nombre" : "Alumno3",
        "email" : "email3@email.com",
        "fecha_nac" : "10/10/1990",
        "titulacion" : True,
        "nota_curso" : 8.4,
        "contenido_nota" : {
                "UF1-> Introd" : 7.45,
                "UF2" : 8.0,
        }

}
]         


#Operadores y expresiones
#Aritméticos
suma = 10 + 5
resta = 10 - 5
mult = 10 * 5
div = 10 / 5
mod = 10 % 5
potencia = 10 ** 2

print(suma)
print(resta)
print(mult)
print(div)
print(mod)
print(potencia)

# De comparación
igual = 10 == 5   #S IMBOLO IGUAL ==
print(igual) #False

diferente = 10 != 5 # SIMBOLO !=
print(diferente) # rue

mayor = 10 > 5
print(mayor) # True

menor = 10 < 5
print(menor) # False

mayor_igual = 10>=5 
print(mayor_igual) # True

menor_igual = 10 <= 5 
print(menor_igual) # False

#Lógicos
# and: devuelve True si todas las comparaciones son True
# or: devuelve True si una de las comparaciones es True
# not: Invierte estado booleano True -> False

and_operador = (10 >5) and (10 < 5) # da False porque ninguno se cumple
and_operador2 = (10>5) and (10 > 7) and (10>11) # da False porque ninguno se cumple

or_operador = (10 > 5) or (10 < 5) # da True porque uno se cumple
or_operador2 = (1 > 5) or (10 > 5) or (10>11) # da True porque alguno se cumple

not_operador = not (10 > 5) # False porque 10 sí es mayor a 5