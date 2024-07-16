# Ejercicio 1: Mostrar cadena en mayúsculas.
cadena = "Ola ke ase"
print(cadena.upper())

# Ejercicio 2: Mostrar cadena en minúsculas.
print(cadena.lower())

# Ejercicio 3: Mostrar cadena con la primera letra en mayúsculas.
print(cadena.capitalize())

# Ejercicio 4: Mostrar cadena con la primera letra de cada palabra en mayúsculas.
print(cadena.title())
cadena = cadena.title()
# Ejercicio 5: Mostrar cadena con las mayúsculas convertidas en minúsculas y viceversa.
cadena = cadena.swapcase()
print(cadena)

# Ejercicio 6: Mostrar cadena donde una subcadena es reemplazada por otra subcadena.
cadena2 = "Ola ke ase"
cadena2 = cadena2.replace("Ola", "Hola")
print(cadena2)

# Ejercicio 7: Mostrar lista de palabras a partir de una cadena.
cadena = "Hola que tal" 
cadena = cadena.split()
print(cadena)

# Ejercicio 8: Mostrar cadena a partir de una lista de palabras.
cadena = ["Hola", "que", "tal"]
cadena = " ".join(cadena)
print(cadena)
# Ejercicio 9: Mostrar cadena sin espacios en blanco al principio y al final.
cadena = "             Palabras más palabras menos          " 
cadena=cadena.strip()
print(cadena)

# Ejercicio 10: Mostrar cadena sin espacios en blanco al principio.
cadena = "             Palabras más palabras menos           " 
cadena=cadena.lstrip()
print(cadena)

# Ejercicio 11: Mostrar cadena sin espacios en blanco al final.
cadena = "             Palabras más palabras menos           " 
cadena=cadena.rstrip()
print(cadena)

# Ejercicio 12: Mostrar True si la cadena comienza con una subcadena.
cadena = "Nito es mi perro" 
print(cadena.startswith("Nito"))

# Ejercicio 13: Mostrar True si la cadena acaba con una subcadena.
cadena = "Nito es mi perro bello" 
print(cadena.endswith("bello"))

# Ejercicio 14: Mostrar la primera posición de una subcadena en una cadena.
print(cadena.find("Nito"))

# Ejercicio 15: Mostrar la última posición de una subcadena en una cadena.
cadena = "Hola que que tal" 
print(cadena.rfind("que"))

# Ejercicio 16: Mostrar el número de veces que una subcadena aparece en una cadena.
cadena = "Hola que que tal" 
print(cadena.count("que"))

# Ejercicio 17: Mostrar True si la cadena es alfanumérica.
cadena = "Nito es mi perro bello" 
print(cadena.isalnum())

# Ejercicio 18: Mostrar True si la cadena es alfabética.
cadena = "Nito es mi 3m" 
print(cadena) #False porque contiene espacios

cadena = "Nitoesmi3m" 
print(cadena) #True, sin espacios si lo detecta como un valor alfanumérico

cadena = "Nito es mi perro bello"


