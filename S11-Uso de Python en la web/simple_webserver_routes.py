from http.server import BaseHTTPRequestHandler, HTTPServer

# MÉTODO GET
# Nuestras rutas/recursos:
# "/": "Hola soy la página de inicio"
# "/cotact": "Hola soy la página de formulario de contacto"
# "/*/ruta_no_existente": "Devolvemos un 404 (código de págona no encontrada)"
# Listado de código:  https://developer.mozilla.org/es/docs/Web/HTTP/Status


# MÉTODO POST
# Recibimos un dato (JSON) mediante POST y mediante la extensión "Thunder Client" y lo imprimimos en el servidor. Después le enviamos un OK al cliente.

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("Hola soy la página de inicio".encode("utf-8"))
            return
        
        if self.path =="/contact":
            self.send_response(200)
            self.send_header("Content-type","text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("Hola soy la página de formulario de contacto".encode("utf-8"))
            return
        
        self.send_response(404)
        self.send_header("Content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Página no encontrada".encode("utf-8"))
        return
    
    def do_POST(self):
        import json
        content_length = int(self.headers["Content-Length"]) # Longitud del contenido
        post_data = self.rfile.read(content_length) # lee el contenido
        data = json.loads(post_data.decode("utf-8")) # convertimos el datoq ue nos viene en json en diccionario
        print(data)
        
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
        
                