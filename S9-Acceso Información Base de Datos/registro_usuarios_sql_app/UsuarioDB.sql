drop database if exists UsuarioDB; 
create database UsuarioDB; 
use UsuarioDB;

create table usuarios(
    id INT not NULL PRIMARY KEY auto_increment,
    dni char(9) not null UNIQUE,
    nombre varchar(100) not null,
    email varchar(50) not null,
    contrasena varchar(50) not null 
);

