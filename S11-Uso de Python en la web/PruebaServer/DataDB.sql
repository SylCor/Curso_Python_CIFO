drop database if exists DataDB; 
create database DataDB; 
use DataDB;

create table Datos(
    id INT not NULL PRIMARY KEY auto_increment,
    Nombre varchar(100) not null,
    Apellido varchar(100) not null

);

