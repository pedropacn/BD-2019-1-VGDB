create database if not exists vgbd_db;
use vgbd_db;
-- create table if not exists Dogs (
--   id integer primary key not null auto_increment,
--   name varchar(50) not null,
--   age integer not null
-- );

CREATE TABLE IF NOT EXISTS users (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(60) NOT NULL,
  email VARCHAR(100) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  password VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS series (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS genres (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL,
  PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS games (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  score_critics DECIMAL(5,2) NOT NULL,
  genres_id INT NOT NULL,
  series_id INT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (series_id)
    REFERENCES series (id),
  FOREIGN KEY (genres_id)
    REFERENCES genres (id)
);
ALTER TABLE games ADD COLUMN art LONGBLOB;

CREATE TABLE IF NOT EXISTS companies (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(80) NOT NULL,
  address VARCHAR(100) NOT NULL,
  number_employees INT NULL,
  website VARCHAR(60) NULL,
  foundation_date DATE NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS generations (
  id INT NOT NULL AUTO_INCREMENT,
  number INT NOT NULL,
  date_init YEAR(4) NOT NULL,
  date_end YEAR(4) NULL,
  PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS platforms (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(60) NOT NULL,
  price DECIMAL(5,2) NOT NULL,
  launch_date DATE NULL,
  manufacturer VARCHAR(80) NULL,
  units_sold INT NULL,
  generations_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (generations_id)
    REFERENCES generations (id)
);

CREATE TABLE IF NOT EXISTS developers (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(80) NOT NULL,
  last_name VARCHAR(80) NOT NULL,
  occupation VARCHAR(100) NOT NULL,
  nacionality VARCHAR(60) NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS releases (
  id INT NOT NULL AUTO_INCREMENT,
  date DATE NOT NULL,
  country VARCHAR(100) NOT NULL,
  games_id INT NOT NULL,
  platforms_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (games_id)
    REFERENCES games (id),
  FOREIGN KEY (platforms_id)
    REFERENCES platforms (id)
);

CREATE TABLE IF NOT EXISTS reviews (
  id INT NOT NULL AUTO_INCREMENT,
  score DECIMAL(5,2) NOT NULL,
  description LONGTEXT NOT NULL,
  games_id INT NOT NULL,
  users_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (games_id)
    REFERENCES games (id),
  FOREIGN KEY (users_id)
    REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS  companies_has_games (
  companies_id INT NOT NULL,
  games_id INT NOT NULL,
  PRIMARY KEY (companies_id, games_id),
  FOREIGN KEY (companies_id)
    REFERENCES companies (id),
  FOREIGN KEY (games_id)
    REFERENCES games (id)
);


CREATE TABLE IF NOT EXISTS users_has_games (
  users_id INT NOT NULL,
  games_id INT NOT NULL,
  hours_played INT NULL,
  PRIMARY KEY (users_id, games_id),
  FOREIGN KEY (users_id)
    REFERENCES users (id),
  FOREIGN KEY (games_id)
    REFERENCES games (id)
);

CREATE TABLE IF NOT EXISTS games_has_developers (
  games_id INT NOT NULL,
  developers_id INT NOT NULL,
  PRIMARY KEY (games_id, developers_id),
  FOREIGN KEY (games_id)
    REFERENCES games (id),
  FOREIGN KEY (developers_id)
    REFERENCES developers (id)
);

-- views

CREATE VIEW `most_sold_platform` AS

SELECT

  id, name, units_sold

FROM platforms

ORDER BY units_sold DESC LIMIT 10;

CREATE VIEW `dev_by_ocupation` AS

SELECT

  id, first_name, last_name, occupation

FROM developers

ORDER BY occupation ASC LIMIT 100;

CREATE VIEW `company_age` AS

SELECT

  id, name, YEAR(NOW()) - YEAR(foundation_date) as age

FROM companies

ORDER BY name DESC LIMIT 50;

CREATE VIEW `best_game` AS

SELECT

  id, name, score_critics

FROM games

ORDER BY score_critics DESC LIMIT 50;