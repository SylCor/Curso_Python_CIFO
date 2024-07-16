# La manera en que interactúan las tuplas

# Tuplas: son colecciones de datos ordenados e inmutables. SE DEFINE CON ()

# Propiedades:
    # Inmutabilidad:una vez creada no podemos modificar sus datos
    # Indexación:Se puede acceder a los datos mediante índices(valor numérico)
    # Ordenadas: mantienen el orden en el que se insertan los elementos 

# Métodos:
    # count(): cuenta cuantas veces aparece un valor
    # index(): devuelve el índice del primer elemento
    
# Ejemplos:
tupla = (1, 2, 3, 4, 5, 2, 2)
#tupla[0] = 0 # nos da error, porque es inmutable

print(tupla.count(2)) # el resultado sería 3
print(tupla.index(3)) # el resultado sería 2