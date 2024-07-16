###  TO-DO LO DE USUARIOS
# establecemos conexión en nuestro caso (XAMPP)
def connect_db():
    import mysql.connector
    connex = mysql.connector.connect(
    user="root", 
    password="",
    host="localhost",
    database="bibliotecadb")
    if connect_db:
        return connex

    else:
        print("Ha habido un error en la conexión a MySQL")


# DATABASE (sql format)
# introducir un usuario en la base de datos
def set_data_mysql(valorOBJ,tabla):
    connex = connect_db()
    cursor = connex.cursor()
  # Evitar inyección SQL (seguridad)
    if tabla == "usuarios":
        query = f"insert into {tabla} values(null, %s,%s,%s,%s)"
        cursor.execute(query,(valorOBJ.dni,valorOBJ.nombre,valorOBJ.email,valorOBJ.contrasena))
        connex.commit()
        cursor.close()
        connex.close()
    elif tabla=="libros":
        query = f"insert into {tabla} values(null, %s,%s,%s,%s)"
        cursor.execute(query,(valorOBJ.isbn,valorOBJ.titulo,valorOBJ.autor,valorOBJ.genero))
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
def delete_user_mysql(dni):
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
def find_user_mysql(dni):
    connex = connect_db()
    cursor = connex.cursor()
    query = "select * from usuarios where dni = %s"
    cursor.execute(query,(dni,)) #NO OLVIDAR LA , ASÍ SEA SOLO UN VALOR
    resultado = cursor.fetchall()
    cursor.close()
    connex.close()
    return resultado


    ###  TO-DO LO DE LIBROS
def set_libro_mysql(libroOBJ):
    connex = connect_db()
    cursor = connex.cursor()
  # Evitar inyección SQL (seguridad)
    query = "insert into usuarios values(null, %s,%s,%s,%s)"
    cursor.execute(query,(libroOBJ.isbn,libroOBJ.titulo,libroOBJ.autor,libroOBJ.genero))
    connex.commit()
    cursor.close()
    connex.close()
    