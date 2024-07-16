
lista = [1,2,3,4,5,2,2]
#acceso, lectura o modificación
print(lista[4]) #nos devuelve el 5
lista[3] = 1
print(lista)

# Métodos
print(lista) # [1,2,3,1,5,2,2]
# append: inserta un valor en la última posición
lista.append(8) # resultado [1,2,3,1,5,2,2,8] SE AÑADE SOLO SIN TENER QUE VOLVER A DECLARAR LA VARIABLE. LA ACCIÓN SE EJECUTA AL APLICARLA

# insert: inserta un valor en una determinada posición
lista.insert(0,8) #[8,1,2,3,1,5,2,2,8]
lista.insert(2,8) #[8,1,8,2,3,1,5,2,2,8]

# remove: elimina el primer valor que hay en la lista
lista.remove(2) #[8,1,8,3,1,5,2,2,8] #remueve el primer "2" que encuentra

# pop: elimina un valor en una determinada posición
lista.pop(2) #[8,1,3,1,5,2,2,8] elimina el "8" que ocupaba la posición 2

# reverse: invierte los valores
lista.reverse() # [8,2,2,5,1,3,8,1,8]

# sort: ordena los valores de menor a mayor
lista.sort()
print(lista)

lista.sort(reverse=True) # invierte de mayor a menor
print(lista)

# ejemplo lista con cadenas, prioridad a la hora de ordenar
lista_cadena = ["epa","#","hola","que","tal","%","estas","Estas"]
lista_cadena.sort()
print(lista_cadena)