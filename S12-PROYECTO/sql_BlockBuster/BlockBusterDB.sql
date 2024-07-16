drop database if exists BlockBusterDB; 
create database BlockBusterDB; 
use BlockBusterDB;

create table socios(
    id INT not NULL PRIMARY KEY auto_increment,
    dni char(9) NOT NULL UNIQUE,
    nombre varchar(100) NOT NULL,
    email varchar(50) NOT NULL,
    contrasena varchar(50) NOT NULL 
);


-- Crear la tabla películas
CREATE TABLE movies (
    id INT not NULL PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(200) NOT NULL,
    director VARCHAR(100) NOT NULL,
    actor VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL
);

-- Crear la tabla prestamos
CREATE TABLE alquileres (
    id INT not NULL PRIMARY KEY AUTO_INCREMENT,
    id_socio INT NOT NULL,
    id_movie INT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (id_socio) REFERENCES socios(id),
    FOREIGN KEY (id_movie) REFERENCES movies(id)
);

