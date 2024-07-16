drop database if exists BibliotecaDB; 
create database BibliotecaDB; 
use BibliotecaDB;

create table usuarios(
    id INT not NULL PRIMARY KEY auto_increment,
    dni char(9) NOT NULL UNIQUE,
    nombre varchar(100) NOT NULL,
    email varchar(50) NOT NULL,
    contrasena varchar(50) NOT NULL 
);


-- Crear la tabla libros
CREATE TABLE libros (
    id INT not NULL PRIMARY KEY AUTO_INCREMENT,
    isbn CHAR(13) NOT NULL UNIQUE,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL
);

-- Crear la tabla prestamos
CREATE TABLE prestamos (
    id INT not NULL PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    id_libro INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_libro) REFERENCES libros(id)
);