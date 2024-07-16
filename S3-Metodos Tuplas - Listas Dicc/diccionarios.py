# Diccionarios: son colecciones de datos desordenados de pares "clave" :"valor"

# Propiedades:
    # Mutabilidad
    # Desordenados (no son indexados): no mantienen un orden específico
    # Claves únicas: no podemos repetir el nombre de las claves
    
# Métodos
#get(): a través del nombre de la clave, nos devuelve el valor
diccionario = {
    "nombre" : "Pepe",
    "apellido" : "López"
}

print(diccionario["nombre"])
print(diccionario.get("nombre"))
# "clave" : "valor" 
# "key" : "value"

# keys(): devuelve en una LISTA las claves del diccionario
print(diccionario.keys()) # ["nombre","apellido"]

# items(): devuelve una lista de tuplas, cada una con "clave" : "valor"
print(diccionario.items()) # [("nombre","Pepe"), ("apellido","Lopez")]
# puedo guardar la consulta en otra variable
x = diccionario.items()

# values(): devuelve en una LISTA los valores(lo que guardan las claves) del diccionario
print(diccionario.values()) # ["Pepe", "Lopez"]

# pop(): elimina un elemento con una clave determinada, devuelve el valor
diccionario2 = {
    "nombre" : "Maria",
    "apellido" : "Sanchez",
    "ciudad" : "Barcelona",
    "dato" : True
}

print(diccionario2)

dato_eliminado = diccionario2.pop("dato")
print(dato_eliminado)  #el pop me almacenó el valor de la clave "dato" eliminado
print(diccionario2) # diccionario2 sin la clave "dato"

# update():podemos añadir un nuevo par "clave" : "valor". También podemos modificar un par de "clave" : "valor" ya existente
diccionario2.update({"dato" : dato_eliminado})
print(diccionario2) #volví a añadir una clave con su valor, en este caso volví a añadir el dato eliminado

diccionario2. update({"dato" : "False"}) #modifiqué el valor de la clave "dato" a el valor False
print(diccionario2)

