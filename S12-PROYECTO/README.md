#API REST SocioMovie (Servidor Web) Block Buster proyecto final de curso de Python de Sylvia Corriere. 

# Estructura de Proyecto
/apirest_base/
    |-------- /sql_BlockBuster  -> Carpeta con Scripts SQL para la estructura de la Base de Datos
    |-------- BlockBusterApp.py -> Punto de entrada de la apirest (toda la lógica del servidor web)
    |-------- BlockBusterDB.py  -> Clase con lógica de interacción a MySQL
    |-------- requirements.txt  -> Archivo que contiene todos los módulos necesarios para la app
    |-------- utils.py          -> Validaciones de DNI, email, contraseña y fecha usando RegExp 
    

# requirements.txt: el comando que ejecutamos para que lea todos los módulos (dependencias) de este archico y los instale en nuestro proyecto:
```
pip install -r requirements.txt
```

# Crear entorno virtual y activarlo
```
python -m venv venv
```
```
venv\Scripts\activate
```


# PASOS DESARROLLO
1- Crear el archivo "BlockBusterDB.sql" dentro de la carpeta sqlBlockBuster, que contiene la estructura de la base de datos en MySQL (DB relacional). Esta base de datos crea las tablas "socios", "movies" y "alquileres" con sus rexpectivos campos en los que interactua la api rest.

2- Desarrollar la Clase "Database" en "/BlockBusterDB.py":
    - Constructor: crea la conexión a MySQL
    - 3 Métodos: que realizan las acciones de "CONSULTA", "EJECUCIÓN" y "CERRAR CONEXIÓN"

3- Desarrollar la API REST en "/BlockBusterApp.py"
    1- Añadir los imports que necesita este módulo
    2- Desarrollamos la clase "ApiRestSocioMovie"
        1- Método que gestiona las cabeceras (información que viaja junto al paquete (request, response))
        2- Método que gestiona la petición GET
        3- Método que gestiona la peticion POST
        4- Método que gestiona la peticion DELETE

# Módulos necesarios al inicio de la API REST
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt # para instalar en la casa --> pip install bcrypt
from datetime import datetime
import utils
from urllib.parse import urlparse, parse_qs, urlsplit


# Peticiones CRUD (create/read/update/delete) Ejemplo para la tabla Movies
# GET: http://localhost:3000/movies -> devuelve todos las movies (str) de la tabla "movies" (cRud)
    - body: None
# POST: http://localhost:3000/movie -> Crea/inserta una movie (str)  en la tabla "movies" (Crud)
    - body (JSON): { "mensaje": "dato_tipo_texto" } 
# PUT: http://localhost:3000/movie -> Actualiza un valor específico de movie (str)  en la tabla "movies" (crUd)
    - body (JSON): { id: "id_de_la_movie_a_actualizar", "mensaje": "dato_tipo_texto_actualizado" } 
# DELETE: http://localhost:3000/movie -> Borra una movie (str)  en la tabla "movies" (cruD)
    - body (JSON): { id: "id_de_la_movie_a_borrar" } 

# NOTA: Adicionalmente, para la tabla "alquileres" existen dos tipos de consultas GET:
    1- Saber el total alquileres de un usuario.
    2. Saber el total de alquileres de una película específica para un usuario.





