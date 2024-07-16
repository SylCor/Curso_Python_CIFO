
# establecemos conexión en nuestro caso (XAMPP)
def connect_db():
    import mysql.connector
    connex = mysql.connector.connect(
    user="root", 
    password="",
    host="localhost",
    database="usuariodb")
    if connect_db:
        return connex

    else:
        print("Ha habido un error en la conexión a MySQL")

# DATABASE (sql format)
# introducir un usuario en la base de datos
def set_data_mysql(usuarioOBJ):
    connex = connect_db()
    cursor = connex.cursor()
  # Evitar inyección SQL (seguridad)
    query = "insert into usuarios values(null, %s,%s,%s,%s)"
    cursor.execute(query,(usuarioOBJ.dni,usuarioOBJ.nombre,usuarioOBJ.email,usuarioOBJ.contrasena))
    connex.commit()
    cursor.close()
    connex.close()
    
# todos los usuarios   
def get_data_mysql():    
    query = "select * from usuarios"
    connex = connect_db()
    cursor = connex.cursor()
    cursor.execute(query)
    usuarios = cursor.fetchall()
    cursor.close()
    connex.close()
    return usuarios
    
# CONSULTAS FALTAN
# Borrar un usuario mediante DNI
def delete_data_mysql(dni):
    connex = connect_db()
    cursor = connex.cursor()
    query = "SELECT COUNT(*) FROM usuarios WHERE dni = %s"
    cursor.execute(query,(dni,)) #NO OLVIDAR LA , ASÍ SEA SOLO UN VALOR
    user_exists = cursor.fetchone()[0]
    
    if user_exists:
        delete_query = "DELETE FROM usuarios WHERE dni = %s"
        cursor.execute(delete_query,(dni,))
        connex.commit()
        cursor.close()
        connex.close()
        return True
    else:
        cursor.close()
        connex.close()
        return False

# Buscar un usuario por DNI
def find_data_mysql(dni):
    connex = connect_db()
    cursor = connex.cursor()
    query = "select * from usuarios where dni = %s"
    cursor.execute(query,(dni,)) #NO OLVIDAR LA , ASÍ SEA SOLO UN VALOR
    resultado = cursor.fetchall()
    cursor.close()
    connex.close()
    return resultado
# select * from tabla where dni = dni_que_pone_el_usuario




    