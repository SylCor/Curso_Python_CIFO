# Condicionales
# Def: estructura de control que permite tomar decisiones basadas en el valor de una expresión
# En Python, se define mediante la palabra clave if, es seguida de una expresión booleana y dos puntos:
# Si la expresión booleana es verdadera, se ejecuta el bloque de código que sigue al condicional, si se ejecuta el siguiente condicional o bloque de código

# Ejemplo 1
# Condicional simple

x = 10
if x > 5:
    print("x es mayor que 5") # comparativa devuelve True
    
# Ejemplo 2
# Condicional compuesto. Gestiona la comparación contraria (no se cumple)
x = 3
if x > 5:
    print("x es mayor que 5") # comparativa devuelve True
else:
    print("x es menor o igual que 5") # comparativa devuelve False
    
# Ejemplo 3
# Condicional anidado: vemos el ejemplo anterior gestionando la salida si el valor es igual a 5
x = 3
if x > 5:
    print("x es mayor que 5")
else:
    if x == 5:
        print("x es igual que 5")
    else:
        print("x es menor que 5")
        
# Ejemplo 4
# Condicional else if --> elif
x = 3
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual que 5")
else:
    print("x es menor que 5")

# Ejemplo 5: detecta si estoy saludando con la palabra "hola"
# aceptamos "hola", "Hola" y "HOLA"
cadena = "Hola"

if cadena == "Hola":
    print(cadena + " que tal") #Hola que tal
    
elif cadena == "HOLA":
    print(cadena + " que tal") #HOLA que tal
elif cadena == "hola":
    print(cadena + " que tal") #hola que tal
else:
    print ("No has saludado!")

# Ejemplo 5.1: podemos usar métodos de cadenas para optimizar y validar el código
# aceptamos "hola", "Hola" y "HOLA"
cadena = "Hola"
cadena = cadena.lower()

if cadena == "hola":
        print(cadena + " que tal") #hola que tal
else:
    print ("No has saludado!")

# Ejemplo 6: comparadores lógicos
# Login
emailDB = "sylvia@gmail.com"
passwordDb = "1234"

emailUSER = "sylvia@gmail.com"
passwordUSER = "1234"

if emailDB == emailUSER and passwordDb == passwordUSER:
    print("Login correcto")
else:
    print("Datos erróneos")
    
# Ejemplo 7: detectar si un número es positivo o negativo
num = 10
if num >= 0:
    print("El número es positivo")
else:
    print("El número es negativo")
    
#versión 2: quiero detectar el valor 0:
num = 10
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es 0")


# Ejemplo 8: detectar si un número es par o impar
x = 20
y = x%2
if y == 0:
    print("El número es par")
else:
    print("El número es impar")

# otra manera de hacerlo    
x = 20
xType = type(x)
if xType != int:
    print(str(x) + " El número es par")
else:
    print(str(x) + " El número es impar")  
    

# Ejemplo 9: ordenar 3 números de mayor o menor
x = 50 
y = 5
z = 500
a = []
if x > y and x > z and y > z:
    a= [x, y, z]     
    print(a)
elif x > y and x > z and y < z:
    a= [x, z, y]     
    print(a)
        
else: 
    if y > x and y > z and x > z:
        a= [y, x, z]     
        print(a)
    elif y > x and y > z and x < z:
        a= [y, x, z]     
        print(a)
 
    else:
        if z > x and z > y and x > y:
            a= [z, x, y]     
            print(a)
        elif z > x and z > y and x < y:
            a= [z, y, x]     
            print(a)   


# otra manera
x = 50 
y = 5
z = 500
a = []
if x > y and x > z :
    if y > z:
        a= [x, y, z]     
        print(a)
    else:
        a= [x, z, y]     
        print(a)
        
elif y > x and y > z:
    if x > z:
        a= [y, x, z]     
        print(a)
    else:
        a= [y, x, z]     
        print(a)
 
elif z > x and z > y:
    if x > y:
            a= [z, x, y]     
            print(a)
    else:
            a= [z, y, x]     
            print(a)   


# manera fácil
x = 50 
y = 5
z = 500
a = [x , y , z]
print(a)
a.sort(reverse=True)
print(a)



