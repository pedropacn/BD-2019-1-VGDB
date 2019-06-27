create database if not exists exemplo;
use exemplo;
create table if not exists Dogs (
  id integer primary key not null auto_increment,
  name varchar(50) not null,
  age integer not null
);

insert into Dogs (name, age)
values ('carlinhos', 32);