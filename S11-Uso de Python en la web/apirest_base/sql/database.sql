DROP database if exists apirest_base; -- borra DB si existe
CREATE database apirest_base; -- crea DB
use apirest_base; -- selecciona DB

-- crea la tabla "datos"
CREATE table datos(
    id int primary key auto_increment,
    dato varchar(255) not NULL
);

