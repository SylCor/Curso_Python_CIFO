from http.server import BaseHTTPRequestHandler, HTTPServer
from mysql.connector import Error


class Conect():
    def connect_db(self):
        try:
            import mysql.connector
            connex = mysql.connector.connect(
            user="root", 
            password="",
            host="localhost",
            database="datadb")
            if connex.is_connected():
                return connex
        except Error as e:
            print("Error en MySQL: " + str(e))
        
        finally:
            print("Conexión a MySQL correcta")
            

            
    def insertarDato(data):
        connex = Conect.connect_db()
        cursor = connex.cursor()
        cursor.execute( "INSERT INTO datos VALUES (NULL, %s,%s)", (data["Nombre"],data["Apellido"])) #NO OLVIDAR LA COMA
        connex.commit()
        cursor.close()
        connex.close()
        
            
class Servidor(BaseHTTPRequestHandler):     
    
    def do_POST(self):
        import json
        content_length = int(self.headers["Content-Length"]) # Longitud del contenido
        post_data = self.rfile.read(content_length) # lee el contenido
        data = json.loads(post_data.decode("utf-8")) # convertimos el dato que nos viene en json en diccionario
    
        Conect.insertarDato(data)
        
        self.send_response(200)
        self.send_header("Content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("El dato ha sido recibido correctamente".encode("utf-8"))
        return


def run():
    print("Iniciando servidor...")
    server_address = ("localhost", 3000)
    server = HTTPServer(server_address, Servidor)
    print("Servidor Localhost escuchando peticiones por el puerto 3000")
    server.serve_forever()
    
run()
        
                