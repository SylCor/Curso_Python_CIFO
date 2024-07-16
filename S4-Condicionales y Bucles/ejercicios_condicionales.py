
# Ejercicio 1 -> Escribe un programa que pida al usuario un número entero e imprima si es positivo, negativo o cero.
x = input("escribe un número entero  ")
x = int(x)
print(x)
if x > 0:
    print(f"{x} es positivo")
elif x < 0:
    print(f"{x} es negativo")
else:
    print(f"{x} es cero")
 
 
# Ejercicio 2 -> Introducir el color del semáforo y mostrar si puede pasar, extremar la precaución o no pasar.
color = "rojo"
if color == "rojo":
    print("No puedes pasar!")
elif color == "ambar":
    print("Precaución!")
elif color =="verde":
    print("Puedes pasar!")
else:
    print("Color erroneo")
          
 
# Ejercicio 3 -> Mostrar si un número es par o impar
numero = 4
tipo_dato = type(numero) #para ver que tipo de dato es
if tipo_dato != int:
    print("Dato no numérico")
else:
    if numero % 2 ==0:
        print (numero + " es par")
    else:
        print(numero + " es impar")

 
# Ejercicio 4 -> Introducir 3 números. Indicar si el tercero es la suma de los dos primeros o no.
num1 = 1
num2 = 5
num3 = 6

if num1 + num2 == num3:
    print("la suma de los dos primeros números corresponde al tercero")
else:
    print ("los dos primeros números no corresponden a la suma para obtener el tercero")


# Ejercicio 5 -> Introducir un precio a pagar y el dinero disponible y mostrar si le falta dinero, indicarle cuanto, si le sobra indicar cuánto y si esta justo mostrar gracias por la compra
precioPagar = 150
dineroDisponible = 200

if precioPagar > dineroDisponible:
    print(f"Te falta {precioPagar - dineroDisponible}")
elif precioPagar < dineroDisponible:
    print(f"Te sobra {dineroDisponible-precioPagar}")
elif precioPagar==dineroDisponible:
    print("Tienes el dinero justo")


# Ejercicio 6 -> Introducir 3 números. Ordenar descendentemente.
a = 20
b = 7
c = 50
 
lista = [a,b,c]
print(lista)
lista.sort(reverse=True)
print(lista)
 
# Ejercicio 7 -> Comprobar la letra del DNI:

# Para la calcular la letra divide tu número de dni entre 23 y el resto es la posicion de la lista anterior: Ejemplo: 11223344 % 23 = 8 -> letra P
letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
numeroDNI_user = 11223344
letraDNI_user = "A"

letraDNI_calculo = letras[numeroDNI_user % 23] #-> debería ser 3
if letraDNI_user == letraDNI_calculo:
    print("Letra Correcta")
else:
    print("Letra incorrecta")



#VALIDANDO

letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
numeroDNI_user = 11223344
letraDNI_user = "A"
#DNI_completo = input("Introduce tu NIE")

DNI_completo = "11223344A"
print(DNI_completo[:8]) # [:8] devuelve los 8 primeros caracteres
print(DNI_completo[8]) # nos da el último caracter que es la letra
print(DNI_completo[-1]) #recorre el string del final a adelante, nos da el último valor que es la letra

#len() --> devuelve la longitud (cantidad de caracteres) de un string

if len(DNI_completo) != 9:
    print("DNI incorrecto")
    
else:
    digitos = int(DNI_completo[:8])
    letra = DNI_completo[-1]
    letraDNI_calculo = letras[digitos % 23]
    if letra == letraDNI_calculo:
        print("Letra correcta")
    else:
        print("letra incorrecta")
        print(f"La letra debería ser {letraDNI_calculo}")
    