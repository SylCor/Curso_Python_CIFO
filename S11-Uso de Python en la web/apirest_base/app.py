# importar módulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt # para instalar en la casa --> pip install bcrypt
import utils

# módulo database
from database import Database

class ApiRestBase(BaseHTTPRequestHandler):
    # método que gestiona las cabeceras (información que viaja junto al paquete (request, response))
    def set_headers(self, status_code = 200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
    def do_GET(self):
        db = Database() #instancia
        if self.path == "/datos":
            resultado = db.query("select * from datos")
            resultado_format = [
                {
                    "id" : mensaje[0],
                    "mensaje" : mensaje[1]
                }
                for mensaje in resultado
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultado_format).encode("utf-8"))
        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"Error: Ruta no encontrada"}).encode("utf-8"))
            
    
    def do_POST(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            # Validaciones
            # email = mensaje["email"]
            # if not utils.validarEmail(email):
            #     self.set_headers(400) # bad request
            #     response = json.dumps({"error" : "Email incorrecto"}).encode("utf-8")
            #     self.wfile.write(response)
            #     return

            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            db.execute("insert into datos values (default, %s)", (mensaje["mensaje"],)) # LA COMA SI ES UN SOLO DATO
            db.close()
            self.set_headers(201) # envío un 201 (recurso creado) al método de cabeceras
            # devolvemos un mesanje al cliente
            self.wfile.write(json.dumps({"mensaje" : "Dato almacenado correctamente en MySQL OK"}).encode("utf-8"))
            
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error" : "Ruta no encontrada"}).encode("utf-8"))
            
    
    #ACTUALIZAR VALORES
    def do_PUT(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            
            rows = db.execute("UPDATE datos set dato = %s where id = %s", (mensaje["mensaje"], mensaje["id"])) 
            db.close()
            if rows > 0:
                self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"mensaje" : "Dato actualizado correctamente en MySQL"}).encode("utf-8"))
            
            else:
                self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"error" : "Ruta no encontrada"}).encode("utf-8"))
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error" : "Ruta no encontrada"}).encode("utf-8"))
            
            
    # BORRAR VALORES
    def do_DELETE(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            rows = db.execute("DELETE from datos where id = %s",(mensaje["id"],)) 
            db.close()
            if rows > 0:
                self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"mensaje" : "Dato borrado correctamente en MySQL"}).encode("utf-8"))
            
            else:
                self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"error" : "Ruta no encontrada"}).encode("utf-8"))
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error" : "Ruta no encontrada"}).encode("utf-8"))      
            
            
            
                  
            
            
    
def run(server_class = HTTPServer, handle_class = ApiRestBase, port=3000):
    server_address = ("localhost", port)
    httpd= server_class(server_address, handle_class)
    print(f"ApiRest escuchando por el puerto {port}")
    httpd.serve_forever()
    
run()
                