# Excepciones: una excepción es un error que ocurre durante la ejecución de un programa. Cuando se produce una excepción, el programa se detiene y Python captura esa excepción. Mediante este manejo de errores podemos controlar cualquier evento o error. 

#try:
    # código que puede lanzar una excepción
    

#except Exception as e:+
    # código que se ejecuta si se lanza excepción
    
#finally: 
    # código que se ejecuta siempre, es opcional y es habitual para printar que se ha liberado recursos, cerrado conexiones, o ficheros... 
    
# Ejemplo 1:
try: 
    x = 4
    print(x)
    
except Exception as e:
    print("Error"+str(e))

finally:
    print("Finalizado")

# Ejemplo 2:
try:
    print(1/0)
except Exception as e:
    print("Error"+str(e))
    
# Ejemplo 3: consumo de recurso asincrono
try:
    # Temporizador (simula tiempo en consumo)
    import time
    time.sleep(5)
except Exception as e:
    print("Error"+str(e))
finally:
    print("El recurso ha finalizado")
    
# Ejemplo 4:
import mysql.connector
from mysql.connector import Error

# Las excepciones de un módulo que se han instalado mediante PIP, se gestionan con sus propias Clases, en este caso lo podemos ver en su documentación:
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html

# suponemos una función (utils.py) que conecta a un server MySQL
def get_connection():
    try:
        connex = mysql.connector.connect(
            user="root", 
            password="",
            host="localhost"
        )
        if connex.is_connected():
            print("Conexión a MySQL correcta")
    except Error as e:
        # print("Error en la conexión a MySQL: " + str(e))
        print("Error code:", e.errno)        # error number
        print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
        print("Error message:", e.msg)     # error message
    
get_connection()
