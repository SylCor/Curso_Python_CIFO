# En Python, cada uno de nuestros archivos .py se denominan módulos. Estos módulos a la vez, pueden formar parte de paquetes. Un paquete es una carpeta que contiene módulos. Para que esa carpeta pueda ser considerada un paquete, debe contener un archivo de inicio llamado "__init__.py". Este archivo no tiene ninguna instrucción dentro (vacío)

# __paquete 
# |_____ __init__.py 
# |_____ modulo1__.py 
# |_____ modulo2__.py 
# |_____ modulo1__.py 
# |_____ .....

# Los módulos no necesariamente deben pertenecer a un paquete

# |__ paquete
#     |____ __init__.py 
#     |____ modulo1.py 
#     |____ subpaquete
#           |____ __init__.py 
#           |____ modulo1.py 


# import modulo1
# import paquete.modulo1
# import paquete.subpaquete.modulo1

#namespace: es el nombre que se indica detrás de la palabra import. Es decir, la "ruta" (namespace) del módulo

#Ejemplo:
import paquete.modulo1

paquete.modulo1.funcion1()

# crear un aleas
import paquete.modulo1 as m1 

m1.funcion1()
print(m1.diccionario)

# Importar módulo math
import math
print(math.sqrt(16))

# Importar módulo match con alias
import math as m 
#redondea a la baja
print(m.floor(4.8)) #4
print(m.cos(0)) #1

# Importar una función de un módulo
from math import sqrt
print (sqrt(16))

#Importar  todas las funciones del módulo
from math import *
print(sin(0))
print(tan(0))
