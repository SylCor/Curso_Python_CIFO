# webserver:
# Un servidor web (software) es un programa que procesa una aplicación del lado servidor / backend y gestiona peticiones http que demanda el cliente (cualquier programa que pueda realizar peticiones http, el más común el Navegador Web)

# con pytho, podemos crear un servirdor web utilizando el módulo http.server- Este modulo proporciona clases base para implementar este servidor. 

# Este ejemplo, es un servidor web simple que un cliente (puede ser un navegador) si realiza una petición a esta ruta: "http://localhost:3000", el servidor devuelve un texto plano: "Hola mundo!"


from http.server import BaseHTTPRequestHandler, HTTPServer

#Creamos servidor: Clase que hereda de "BaseHTTPRequestHandler" y define el comportamiento del servidor
class Servidor(BaseHTTPRequestHandler):
    #do_GET: Método que se ejecuta cuando se recibe una petición GET
    # send_response: método que envia una respuesta al cliente
    # send_header: método que envía una cabecera HTTP (un conjunto de datos que definen el mensaje) al cliente
    # end_headers: método que finaliza las cabeceras HTTP
    # wfile: atributo que representa todo el cuerpo de mensaje de respuesta HTTP
    # b: prefijo que indica que el texto es de tipo "bytes"
    
    def do_GET(self):
        self.send_response(200) # 200 código de respuesta satisfactoria
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hola mundo!</h1>") # mensaje que se devuelve al cliente (navegador)
        return
    

# Inicia el servidor
def run():
    print("Iniciando servidor...")
    server_address = ("localhost", 3000)
    server = HTTPServer(server_address, Servidor)
    print("Servidor Localhost escuchando peticiones por el puerto 3000")
    server.serve_forever()
    
run()

#Para comprobar si funciona, abrimos un navegador y ponemos la siguiente dirección: http://localhost:3000
#HTLM
#CSS
#JS
