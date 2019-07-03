create database if not exists exemplo;
use exemplo;
create table if not exists Dogs (
  id integer primary key not null auto_increment,
  name varchar(50) not null,
  age integer not null
);

create table User (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username varchar(60) not null,
  email varchar(100) not null,
  first_name varchar(100) not null,
  last_name varchar(100) not null,
  password varchar(200) not null
);

insert into Dogs (name, age)
values ('carlinhos', 32);