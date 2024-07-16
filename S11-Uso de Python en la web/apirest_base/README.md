#API REST (Servidor Web) base qie mps sorve àra desarrollar el proyecto final de curso de Python. 

# Estructura de Proyecto
/apirest_base/
    |-------- /sql              -> Scripts SQL para la estructura de la Base de Datos
    |-------- app.py            -> Punto de entrada de la apirest (toda la lógica del servidor web)
    |-------- database.py       -> Clase con lógica de interacción a MySQL
    |-------- requirements.txt  -> Archivo que contiene todos los módulos necesarios para la app
    

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
1- Crear el archivo "database.sql" que contiene la estructura de la base de datos en MySQL (DB relacional). Esta  base de datos contiene solamente una tabla con un campo "dato" en el que interactua la api rest.

2- Desarrollar la Clase "Database" en "/database.py":
    - Constructor: crea la conexión a MySQL
    - 3 Métodos: que realizan las acciones de "CONSULTA", "EJECUCIÓN" y "CERRAR CONEXIÓN"

3- Desarrollar la API REST en "/app.py"
    1- Añadir los imports que necesita este módulo
    2- Desarrollamos la clase "ApiRestBase"
        1- Método que gestiona las cabeceras (información que viaja junto al paquete (request, response))
        2- Método que gestiona la petición GET


# Peticiones CRUD (create/read/update/delete)
# GET: http://localhost:3000/datos -> devuelve todos los datos (str) de la tabla "datos" (cRud)
    - body: None
# POST: http://localhost:3000/dato -> Crea/inserta un dato (str)  en la tabla "datos" (Crud)
    - body (JSON): { "mensaje": "dato_tipo_texto" } 
# PUT: http://localhost:3000/dato -> Actualiza un dato (str)  en la tabla "datos" (crUd)
    - body (JSON): { id: "id_del_dato_a_actualizar", "mensaje": "dato_tipo_texto_actualizado" } 
# DELETE: http://localhost:3000/dato -> Borra un dato (str)  en la tabla "datos" (cruD)
    - body (JSON): { id: "id_del_dato_a_borrar" } 


