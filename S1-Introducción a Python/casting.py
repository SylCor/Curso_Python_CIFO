#Datos de entrada con el metodo input(), generalmente se reciben en fortamo str (string/Cadena), pero a menudo es necesario convertirlos a otros tipos de datos (int) (float), ...
edad = input("Dime tu edad: ") # str
edad = int(edad) # int
print(edad)
tipo_dato_edad = print(type(edad))

#EJEMPLO Comprobar si una persona es mayor de edad
edad = input("Dime tu edad: ")
edad_int = int(edad)

if edad_int >= 18:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")
    

#EJEMPLO que se convierte antes de operar
num1 = "10"
num2 = "5"
print("10"+"5")  #el operador suma en Python concatena elementos si sumamos datos str (string/texto)

suma = int(num1) + int(num2)
print(suma)
print(int(num1) + int(num2)) #lo mismo sin crear la variable suma

# CONCATENAR: Útil cuando imprimo datos str y datos contenidos en variables. En Pythin el símbolo de concatenar es +
#Ejemplo de concatenar string y varible. 
miNombre = "Sylvia"
# output: "Mi nombre es Sylvia"
print("Mi nombre es " + miNombre)

# Ejemplo de cast str. Solo se pueden concatenar str usando el símbolo "+"
pi = 3.14159
print(type(pi))

print("El valor de pi es: " + str(pi))

# Convertir tupla en una lista
tupla = (1,2,3)
# tupla[0] = 1 da error, no se pueden editar los valores de la tupla
lista = list (tupla)
lista[0] = 0  #cambié a 0 el primer valor porque primero lo convertí en una lista. La tupla no deja
