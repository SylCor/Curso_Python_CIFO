# Acceso a servidor MY SQL
# Para conectarnos a un servidor MySQL utilizamos un módulo que nos facilita esta tarea. 
# Mediante el gestor de módulos de Python "PIP" instalamos este módulo y lo importamos:
# pip instal mysql-connector-python 
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.htlm
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

import mysql.connector

# establecemos conexión en nuestro caso (XAMPP)
connex = mysql.connector.connect(
    user="root", 
    password="",
    host="localhost",
    database="prueba")

# creamos curso que nos permite ejecutar código SQL (create, select, insert...)
cursor = connex.cursor()

# vacía la tabla de registros
cursor.execute("truncate table mis_datos")

# insertamos un registro en la tabla "mis_datos"
cursor.execute("insert into mis_datos values(null,'Hola mundo!')")
cursor.execute("insert into mis_datos values(null,'Hello World!')")

# Asegurémonos de que los cambios se guarden en la base de datos
connex.commit()

# Cierra el cursor 
cursor.close()

# creamos un nuevo cursor para realizar una consulta
cursor2 = connex.cursor()
cursor2.execute("select * from mis_datos")
datos = cursor2.fetchall()
print(datos)
