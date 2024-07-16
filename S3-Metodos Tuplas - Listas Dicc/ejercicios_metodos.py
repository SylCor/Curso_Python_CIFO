
# Ejercicio con Tuplas:
# Crea una tupla con los números del 1 al 5.
tup = (1, 2, 3, 4, 5)

# Accede al tercer elemento de la tupla.
print(tup[2])

# Cuenta cuántas veces aparece el número 2 en la tupla.
print(tup.count(2))

# Encuentra el índice del número 4 en la tupla.
print(tup.index(4))

# Ejercicio con Listas:
# # Crea una lista con los números del 1 al 5.
listaa = [1, 2, 3, 4, 5]
# # Añade el número 6 al final de la lista.
listaa.append(6)
print(listaa)
# # Inserta el número 0 al inicio de la lista.
listaa.insert(0,0)
print(listaa)

# # Ordena la lista en orden descendente.
listaa.reverse()
print(listaa)

# # Elimina el tercer elemento de la lista.
listaa.pop(2)
print(listaa)



# Ejercicio de Conversión de Tipos:
# # Convierte una lista 1, 2, 3 en una tupla.
# # Convierte una tupla (("clave1", "valor1"), ("clave2", "valor2")) en un diccionario.
# # Convierte un diccionario {"a": 1, "b": 2} en una lista de sus claves.


#Ejercicio con Tuplas:
# Crea una tupla con los números del 1 al 5.
tupla1 = (1,2,3,4,5)

# Accede al tercer elemento de la tupla.
print(tupla1[2]) # el 3

# Cuenta cuántas veces aparece el número 2 en la tupla.
print(tupla1.count(2)) #1 vez

# Encuentra el índice del número 4 en la tupla.
print(tupla1.index(4)) # posición 3

#Ejercicio con Listas:
# Crea una lista con los números del 1 al 5.
lista = [1,2,3,4,5]

# Añade el número 6 al final de la lista.
lista.append(6)
print(lista)

# Inserta el número 0 al inicio de la lista.
lista.insert(0,0)
print(lista)

# Ordena la lista en orden descendente.
lista.sort(reverse=True)
print(lista)

# Elimina el tercer elemento de la lista.
lista.pop(2)
print(lista)


#Ejercicio con Diccionarios:
# Crea un diccionario con las claves "nombre" y "edad", y los valores "Ana" y 25, respectivamente.
diccix = {
    "nombre" : "Ana",
    "edad" : "25"
}

# Añade una nueva clave "ciudad" con el valor "Barcelona".
diccix["ciudad"] = "Barcelona" #Si la clave "ciudad" ya existe, actualiza el valor. Si no existe, la crea.
print(diccix)
 
# Actualiza el valor de la clave "edad" a 26.
diccix["edad"] = "26"
diccix.update({"edad" : "30"})
print(diccix)

# Elimina la clave "ciudad" y muestra su valor.
dato_borrado = diccix.pop("ciudad")
print(dato_borrado)

#Ejercicio de Conversión de Tipos:
# Convierte una lista 1, 2, 3 en una tupla.
listax = [1,2,3]
tuplax = tuple(listax)
print(tuplax)

# Convierte una tupla (("clave1", "valor1"), ("clave2", "valor2")) en un diccionario.
tuplaXX = (("clave1", "valor1"), ("clave2", "valor2"))
dicXX = dict(tuplaXX)
print(dicXX)

# Convierte un diccionario {"a": 1, "b": 2} en una lista de sus claves.
DICC = {"a": 1, "b": 2} 
LisTDic = DICC.keys()
print(LisTDic)