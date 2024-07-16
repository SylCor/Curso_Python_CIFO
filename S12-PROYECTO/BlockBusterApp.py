# importar módulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt # para instalar en la casa --> pip install bcrypt
from datetime import datetime
import utils
from urllib.parse import urlparse, parse_qs, urlsplit

# módulo database
from BlockBusterDB import Database

class ApiSocioMovie(BaseHTTPRequestHandler):
    # método que gestiona las cabeceras (información que viaja junto al paquete (request, response))
    def set_headers(self, status_code = 200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        
# VER TODOS LOS VALORES
    def do_GET(self):
        db = Database() #instancia
        if self.path == "/movies":
            resultado = db.query("select * from movies")
            resultado_format = [
                {
                    "id" : mensaje[0],
                    "titulo" : mensaje[1],
                    "director" : mensaje[2],
                    "actor" : mensaje[3],
                    "genero" : mensaje[4]
                }
                for mensaje in resultado
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultado_format).encode("utf-8"))
            
        elif self.path=="/socios":
            resultado = db.query("select * from socios")
            resultado_format = [
                {
                    "id" : mensaje[0],
                    "dni" : mensaje[1],
                    "nombre" : mensaje[2],
                    "email" : mensaje[3],
                    "contrasena" : mensaje[4]
                }
                for mensaje in resultado
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultado_format).encode("utf-8"))
            
        elif self.path=="/alquileres":
            resultado = db.query("select * from alquileres")
    
            resultado_format = [
                {
                    "id" : mensaje[0],
                    "id_socio" : mensaje[1],
                    "id_movie" : mensaje[2],
                    "fecha" : mensaje[3].strftime("%d/%m/%Y")
                }
                for mensaje in resultado
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultado_format).encode("utf-8"))
            
# ----------------  CONTEO DE TOTAL ALQUILERES DE UN USUARIO--------
        elif self.path.startswith("/count_alquileres_socio/"):
            id_socio = int(self.path.split("/")[-1])
            query = "SELECT COUNT(*) FROM alquileres WHERE id_socio = %s"
            resultado = db.query(query, (id_socio,))
            count = resultado[0][0] if resultado else 0
            self.set_headers()
            self.wfile.write(json.dumps({"id_socio": id_socio, "total_alquileres": count}).encode("utf-8")) 
# ----------------  CONTEO DE TOTAL ALQUILERES DE UN USUARIO POR PELÍCULA--------
        elif self.path.startswith("/acontar_alquileres_socio_movie"):
            query_components = self.path.split("?")
            if len(query_components) > 1:
                params = dict(param.split("=") for param in query_components[1].split("&"))
                id_socio = int(params.get("id_socio", 0))
                id_movie = int(params.get("id_movie", 0))
                # Debug para verificar qué valores se están extrayendo
                print(f"id_socio: {id_socio}, id_movie: {id_movie}")
                query = "SELECT COUNT(*) FROM alquileres WHERE id_socio = %s AND id_movie = %s"
                resultado = db.query(query, (id_socio, id_movie))
                count = resultado[0][0] if resultado else 0
                self.set_headers()
                self.wfile.write(json.dumps({"id_socio": id_socio, "id_movie": id_movie, "total_alquileres": count}).encode("utf-8"))
            else:
                self.set_headers(400) 
                self.wfile.write(json.dumps({"error": "Parámetros id_socio y id_movie no encontrados"}).encode("utf-8"))
        else:
            self.set_headers(404)
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))
        

            
# INTRODUCIR 
    def do_POST(self):
        # ------------ VALORES DE MOVIES-------------
        if self.path == "/movie":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            db.execute("insert into movies values (default, %s, %s, %s, %s)", (mensaje["titulo"],mensaje["director"],mensaje["actor"],mensaje["genero"])) # LA COMA SI ES UN SOLO DATO
            db.close()
            self.set_headers(201) # envío un 201 (recurso creado) al método de cabeceras
            # devolvemos un mesanje al cliente
            self.wfile.write(json.dumps({"mensaje" : "Movie almacenada correctamente en MySQL"}).encode("utf-8"))
            
        # ------------ VALORES DE SOCIOS-------------
        elif self.path == "/socio":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

                #-----INICIO Validaciones-------
            email = mensaje["email"]
            if not utils.validarEmail(email):
                self.set_headers(400) # bad request
                response = json.dumps({"error" : "Formato Email incorrecto. Revise e introduzca nuevamente"}).encode("utf-8")
                self.wfile.write(response)
                return
            
            dni = mensaje["dni"]
            if not utils.validarDNI(dni):
                self.set_headers(400) # bad request
                response = json.dumps({"error" : "Formato DNI incorrecto. El DNI contiene 8 dígitos numéricos y una letra en Mayúsculas"}).encode("utf-8")
                self.wfile.write(response)
                return
            
            contrasena = mensaje["contrasena"]
            if not utils.validarPassword(contrasena):
                self.set_headers(400) # bad request
                response = json.dumps({"error" : "Formato Contraseña incorrecto. Su clave debe contener mínimo 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula, al menos un número y al menos un caracter especial"}).encode("utf-8")
                self.wfile.write(response)
                return
                #---- FIN Validaciones --------
                
                # Encriptar la contraseña
            hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            db.execute("insert into socios values (default, %s, %s, %s, %s)", (mensaje["dni"],mensaje["nombre"],mensaje["email"],hashed_password.decode("utf-8"))) # LA COMA SI ES UN SOLO DATO
            db.close()
            self.set_headers(201) # envío un 201 (recurso creado) al método de cabeceras
            # devolvemos un mesanje al cliente
            self.wfile.write(json.dumps({"mensaje" : "Socio almacenado correctamente en MySQL"}).encode("utf-8"))   
        
        # ------------ VALORES DE ALQUILERES-------------
        elif self.path == "/alquiler":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
                #----- INICIO Validaciones -------   
            fecha = mensaje["fecha"]
            if not utils.ValidarDate(fecha):
                self.set_headers(400) #bad request
                response = json.dumps({"error" : "Formato Fecha. Utilice formato YYYY-mm-dd, revise e introduzca nuevamente"}).encode("utf-8")
                self.wfile.write(response)
                return     
                #---- FIN Validaciones --------                
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            db.execute("insert into alquileres values (default, %s, %s, %s)", (mensaje["id_socio"],mensaje["id_movie"],mensaje["fecha"])) # LA COMA SI ES UN SOLO DATO
            db.close()
            self.set_headers(201) # envío un 201 (recurso creado) al método de cabeceras
            # devolvemos un mesanje al cliente
            self.wfile.write(json.dumps({"mensaje" : "Alquiler registrado correctamente en MySQL"}).encode("utf-8"))   
         
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error" : "Ruta no encontrada"}).encode("utf-8"))
            

#ACTUALIZAR UN VALOR ESPECÍFICO
    def do_PUT(self):
        if self.path == "/movie":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            
        # Update para los elementos de "Movies"
            if "titulo" in mensaje:
                rows = db.execute("UPDATE movies set titulo = %s where id = %s", (mensaje["titulo"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Nombre de la Movie actualizada correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "Ya este título fue actualizado"}).encode("utf-8"))
            
            elif "director" in mensaje:
                rows = db.execute("UPDATE movies set director = %s where id = %s", (mensaje["director"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Nombre Director actualizado correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "Ya este director fue actualizado"}).encode("utf-8"))
                
            elif "actor" in mensaje:
                rows = db.execute("UPDATE movies set actor = %s where id = %s", (mensaje["actor"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Nombre del Actor actualizado correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "Ya este actor fue actualizado"}).encode("utf-8"))
                    
            elif "genero" in mensaje:
                rows = db.execute("UPDATE movies set genero = %s where id = %s", (mensaje["genero"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Género de la movie actualizado correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "Ya este género fue actualizado"}).encode("utf-8"))


        # Update para los elementos de "Socios" 
        elif self.path == "/socio":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
                  
            db = Database()

            if "dni" in mensaje:
                #-------- INICIO Validación DNI ------------
                dni = mensaje["dni"]
                if not utils.validarDNI(dni):
                    self.set_headers(400) # bad request
                    response = json.dumps({"error" : "Formato DNI incorrecto. El DNI contiene 8 dígitos numéricos y una letra en Mayúsculas"}).encode("utf-8")
                    self.wfile.write(response)
                    return
                #--------- FIN Validación----------------       
                rows = db.execute("UPDATE socios set dni = %s where id = %s", (mensaje["dni"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "DNI del socio actualizada correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "DNI ya existente"}).encode("utf-8"))
            
            elif "nombre" in mensaje:
                rows = db.execute("UPDATE socios set nombre = %s where id = %s", (mensaje["nombre"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Nombre del socio actualizada correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "Este nombre ya ha sido actualizado"}).encode("utf-8"))
            
            elif "email" in mensaje:
                #-------- INICIO Validación Email ------------
                email = mensaje["email"]
                if not utils.validarEmail(email):
                    self.set_headers(400) # bad request
                    response = json.dumps({"error" : "Formato Email incorrecto. Revise e introduzca nuevamente"}).encode("utf-8")
                    self.wfile.write(response)
                    return
                #--------- FIN Validación ----------------      
                
                rows = db.execute("UPDATE socios set email = %s where id = %s", (mensaje["email"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Email del socio actualizada correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "email repetido o ya actualizado"}).encode("utf-8"))
            
            elif "contrasena" in mensaje:
                #-------- INICIO Validación Password ------------        
                contrasena = mensaje["contrasena"]
                if not utils.validarPassword(contrasena):
                    self.set_headers(400) # bad request
                    response = json.dumps({"error" : "Formato Contraseña incorrecto. Su clave debe contener mínimo 8 caracteres, al menos una letra mayúscula, al menos una letra minúscula, al menos un número y al menos un caracter especial"}).encode("utf-8")
                    self.wfile.write(response)
                    return
                 #--------- FIN Validación ----------------    

                    # Encriptar la nueva contraseña
                hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
                rows = db.execute("UPDATE socios set contrasena = %s where id = %s", (hashed_password.decode('utf-8'), mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Contraseña del socio actualizada correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "Usuario no existe"}).encode("utf-8"))
    
       # Update para los elementos de "Alquileres"     
        elif self.path == "/alquiler":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            if "id_socio" in mensaje:
                rows = db.execute("UPDATE alquileres set id_socio = %s where id = %s", (mensaje["id_socio"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "ID del socio del alquiler actualizados correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "ID del Usuario ya existente, intente otro valor"}).encode("utf-8")) 
            
            elif "id_movie" in mensaje:
                rows = db.execute("UPDATE alquileres set id_movie = %s where id = %s", (mensaje["id_movie"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "ID de la movie del alquiler actualizados correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "ID de la Movie ya existente, intente otro valor"}).encode("utf-8"))      
                    
            elif "fecha" in mensaje:
                #----- INICIO Validaciones -------   
                fecha = mensaje["fecha"]
                if not utils.ValidarDate(fecha):
                    self.set_headers(400) #bad request
                    response = json.dumps({"error" : "Formato Fecha. Utilice formato YYYY-mm-dd, revise e introduzca nuevamente"}).encode("utf-8")
                    self.wfile.write(response)
                    return     
                #---- FIN Validaciones --------  
                rows = db.execute("UPDATE alquileres set fecha = %s where id = %s", (mensaje["fecha"], mensaje["id"])) 
                db.close()
                if rows > 0:
                    self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"mensaje" : "Fecha del alquiler actualizados correctamente en MySQL"}).encode("utf-8"))
                else:
                    self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                    self.wfile.write(json.dumps({"error" : "Fecha ya existente, pruebe de nuevo"}).encode("utf-8"))    
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error" : "Ruta no encontrada"}).encode("utf-8"))
            
            
# BORRAR VALORES
    def do_DELETE(self):
        if self.path == "/movie":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            rows = db.execute("DELETE from movies where id = %s",(mensaje["id"],)) 
            db.close()
            if rows > 0:
                self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"mensaje" : "Movie borrada correctamente en MySQL"}).encode("utf-8"))
            else:
                self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"error" : "Movie ya eliminada previamente o no existe"}).encode("utf-8"))
                
        elif self.path == "/socio":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            rows = db.execute("DELETE from socios where id = %s",(mensaje["id"],)) 
            db.close()
            if rows > 0:
                self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"mensaje" : "Socio borrado correctamente en MySQL"}).encode("utf-8"))  
            else:
                self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"error" : "Socio ya eliminado o no existe"}).encode("utf-8"))       
        
        elif self.path == "/alquiler":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            
            db = Database()
            # LLAMAMOS AL método "execute" con el formato de consulta que evita inyección de SQL
            rows = db.execute("DELETE from alquileres where id = %s",(mensaje["id"],)) 
            db.close()
            if rows > 0:
                self.set_headers(200) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"mensaje" : "Alquiler finalizado correctamente en MySQL"}).encode("utf-8"))
            else:
                self.set_headers(400) # envío un 200 DE ACTUALIZADO 
                self.wfile.write(json.dumps({"error" : "Alquiler ya eliminado, movie devuelta"}).encode("utf-8"))        
        else:
            self.set_headers(404) # envío un 404 al método de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error" : "ya este registro de alquiler fue eliminado o no existe"}).encode("utf-8"))      
                       
            
    
def run(server_class = HTTPServer, handle_class = ApiSocioMovie, port=3000):
    server_address = ("localhost", port)
    httpd= server_class(server_address, handle_class)
    print(f"ApiRest escuchando por el puerto {port}")
    httpd.serve_forever()
    
run()
              
              
