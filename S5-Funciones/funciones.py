# Definición de funciones en Python:
# Bloque de código que se ejecuta cuando es llamado
# La función puede recibir un parámetro  retornar un valor

# Sintáxis:
#def nombre_funcion (param1, param2, ...):
#   Bloque de código de la función
#   return datos

# Ejemplo1
def suma_dos_numeros_1(a, b):
    suma = a + b
    print(suma)
    
suma_dos_numeros_1(2, 2)
print("--------------función suma_dos_numeros_1----------")


# Ejemplo2: suma dos números con retorno de dato
def suma_dos_numeros_2(a, b):
    suma = a + b
    return suma

# Si en una funcion existe el return, tenemos que gestionar ese dato en la llamada
resultado = suma_dos_numeros_2(2, 2)
print(resultado)
print("--------------función suma_dos_numeros_2----------")

# podemos escribir la función también como_
def suma_dos_numeros_2_1(a, b):
    return a + b

print(suma_dos_numeros_2_1(2,3))


# Ejemplo3: crear una función que detecte si un número es positivo o negativo
def es_positivo(numero):
    if numero >= 0:
        return True
    else:
        return False

print(f"Envía un número y delvuelve True si es positivo o False si es negativo:       {es_positivo(10)}")


      
# SCOPE: el scope o alcance de una variable es el contexto en el que se puede acceder a ella
# Variables locales: solo se pueden acceder a ella dentro de la función en la que se declara
# Variables globales: se puede acceder desde cualquier parte del programa
# A nivel de definición: una variable local tiene prioridad sobre una variable global. (Esto si definimos dos variables con el mismo nombre)

# Ejemplos:
def funcion():
    varibable_local = "Soy una variable local"
    print(varibable_local)
    
funcion()
#si intento imprimir variable_local desde fuera de la funcion el sistema da error
#print(variable_local)-->error

variable_global = "Soy una variable global"
def funcion():
    print(variable_global)
funcion()

#mezclando las dos variables
variable_global = "soy global"
def funcion():
    variable_local = "soy local"
    print(variable_global)
    print(variable_local)
    

# Para modificar una variable global dentro de una función, se debe utilizar la palabra clave "global"
x = 300
def myFunc():
    global x
    x = 200
    
myFunc()
print(x)


#----------------------------------------------------------------------------------------------------------------
#Ejercicios:
# Ejercicio de simulación de Login que hicimos en condicionales. Transformarlo a funcion
# Login
emailDB = "sylvia@gmail.com"
passwordDb = "1234"

def login(emailUSER, passwordUSER):
    
    if emailDB == emailUSER and passwordDb == passwordUSER:
        print("Login correcto")
    else:
        print("Datos erróneos")

login("sylvia@gmail.com", "1234")


#Ejercicio de detectar si un número es primo o no. Transformarlo a funcion

def primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            print (f"{num}  no es primo")
            break
        i = i + 1
    else:
        print (f"{num}  es primo")

primo(113)


# Ejercicio mediante funcion que escriba los números primos que hay en un rango de números

def primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            print (f"{num}  no es primo")
            break
        i = i + 1
    else:
        print (f"{num}  es primo")

primo(113)


def busca_primos(a,b):
    num_primos = []
    for num in range(a, b+1):
        if num < 2:
            continue
        i=2
        while i < num:
            if num%i ==0:
                break
            i = i + 1
        else:
            num_primos.append(num)
    print(num_primos)
        
busca_primos(0,11)

