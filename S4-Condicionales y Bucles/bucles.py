# Bucle / Loop
# Definición: estructura de control que nos permite repetir cualquier tipo de instruccion/es
# Pasos claves para el control de un bucle
# 1- INICIALIZACIÓN
# 2- COMPARACIÓN
# 3- ACTUALIZACIÓN

# Bucle while
# while comp:
    # bloque de instrucciones SI SE CUMPLE
    
# while True:
#    print ("Soy un bucle")

# Ejemplo de imprimir del 1 al 9, porque el 10 no lo toma
i = 1           # 1- INICIALIZACIÓN
while i < 10:   # 2- COMPARACIÓN
    print(i)
    i = i + 1   # 3- ACTUALIZACIÓN
    # escribir i += 1 es lo mismo i = i + 1. siempre la operación antes del igual
# 1, 2... 10 hace el bucle hasta 10

# Ejemplo de imprimir los números del 1 al 10
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Ejemplo de imprimir los números del 10 al 0
i = 10
while i >= 0:
    print(i)
    i = i - 1
    
# Bucle for - in
# Imprimir los números del 1 al 5, es como si le dijera del 1 al <6
for i in range(1, 6):
    print(i)
    
# Bucle for con pasos
#Ejemplo: imprime los números pares del 2 al 10
for i in range (2, 11, 2): # cuenta cada 2 pasos
        print(i," es un número par")
        
# Ejemplo: con una lista de strings, imprimir los datos de una lista
frutas = ["manzana", "pera", "plátano"]
for fruta in frutas:
    print(fruta) #siempre se tiene que definir una variable para ir revisando, o en este caso imprimiendo, cada valor de la lista

# Cómo recorrer un diccionario   
datos = {
    "Juan" : 68,
    "Maria" : 25,
    "Pedro" : 41
}
# para imprimir uno por uno se haría, accediendo individualmente a las edades mediante su clave
print(datos["Juan"]) #68
print(datos["Maria"]) #25
print(datos["Pedro"]) #41

# Imprimir todas la claves: # keys(): devuelve en una LISTA las claves del diccionario
print(datos.keys()) # ["Juan","Maria","Pedro"]

# Para recorrer una lista con un for, primero obtenemos una lista de claves mediante el método items()
print(datos.items()) #[("Juan, 68"), ("Maria", 25), ("Pedro", 41)]

for nombre, edad in datos.items(): #convierte el diccionario en LISTA, "nombre" busca lo que en el diccionario eran las claves, y "edad" busca lo que en el diccionario eran los valores.
    print(nombre, edad)
    

# Sentencia BREAK y CONTINUE
# Ejemplo con break
# Imprimir los números del 1 al 10, y se acaba cuando llega si el número es 5
for i in range(1,11):
    if i == 5:
        break # detiene el for y pasa a la línea 78
    print(i)
    
# Ejemplo con continue
# Imprimir los números del 1 al 10, y omitir el número es 5
for i in range(1,11):
    if i == 5:
        continue # detiene el for y pasa a la línea 78
    print(i)
    
#Bucle con ELSE, con un ejemplo que 
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("Bucle completado sin interrupciones")
    
    
# EJEMPLO   
# Detectar que el email de un usuario este registrado en nuestra "DB"
email_DB = ["a@a.com", "b@b.com", "c@c.com", "d@d.com"]
# Quiero conocer si el usuario con el email "c@c.com" está registrado en nuestra DB
email_buscar = "c@c.com"
for email in email_DB:
    if email == email_buscar:
        print("El email " + email_buscar + " está registrado")
        break  #para de buscar si ya conseguimos el valor que buscábamos
    

