INSERT INTO developers
  (first_name, last_name, occupation, nacionality)
VALUES
  ('Hiedeo', 'Kojima', 'Diretor', 'Japao');
INSERT INTO developers
  (first_name, last_name, occupation, nacionality)
VALUES
  ('Charles', 'Martinet', 'Dublador', 'EUA');
INSERT INTO developers
  (first_name, last_name, occupation, nacionality)
VALUES
  ('Marcin', 'Stroinski', 'Compositor', 'Polonia');
INSERT INTO developers
  (first_name, last_name, occupation, nacionality)
VALUES
  ('Florian', 'Strauss', 'Programador', 'Alemanha');
INSERT INTO developers
  (first_name, last_name, occupation, nacionality)
VALUES
  ('Markus', 'Persson', 'Criador', 'Suecia');


INSERT INTO companies
  (name, address, number_employees, website, foundation_date)
VALUES
  ('Kojima Productions', 'Amsterda', '100', 'http://www.kojimaproductions.jp/index.html', '2005-04-01');
INSERT INTO companies
  (name, address, number_employees, website, foundation_date)
VALUES
  ('Nintendo Entertainment', 'Kyoto', '150', 'https://www.nintendo.com/', '2015-09-16');
INSERT INTO companies
  (name, address, number_employees, website, foundation_date)
VALUES
  ('CD Projekt RED', 'Varsovia', '700', 'https://en.cdprojektred.com/', '1994-07-01');
INSERT INTO companies
  (name, address, number_employees, website, foundation_date)
VALUES
  ('SIE Santa Monica Studio', 'Los Angeles', '200', 'https://sms.playstation.com/', '1999-01-01');
INSERT INTO companies
  (name, address, number_employees, website, foundation_date)
VALUES
  ('Mojang Specifications', 'Estocolmo', '450', 'https://www.mojang.com/', '2009-05-01');


INSERT INTO series
  (name)
VALUES
  ('Metal Gear');
INSERT INTO series
  (name)
VALUES
  ('Mario');
INSERT INTO series
  (name)
VALUES
  ('The Withcer');
INSERT INTO series
  (name)
VALUES
  ('God of War');
INSERT INTO series
  (name)
VALUES
  ('Minecraft');


INSERT INTO genres
  (name)
VALUES
  ('Acao-Aventura');
INSERT INTO genres
  (name)
VALUES
  ('Plataforma');
INSERT INTO genres
  (name)
VALUES
  ('Acao RPG');
INSERT INTO genres
  (name)
VALUES
  ('Acao-Aventura');
INSERT INTO genres
  (name)
VALUES
  ('Sandbox');


INSERT INTO generations
  (number, date_init, date_end)
VALUES
  ('8', '2011', '2017');
INSERT INTO generations
  (number, date_init, date_end)
VALUES
  ('7', '2004', '2011');
INSERT INTO generations
  (number, date_init, date_end)
VALUES
  ('6', '1998', '2004');
INSERT INTO generations
  (number, date_init, date_end)
VALUES
  ('5', '1993', '1999');
INSERT INTO generations
  (number, date_init, date_end)
VALUES
  ('4', '1987', '1996');


INSERT INTO platforms
  (name, price, launch_date, manufacturer, units_sold, generations_id)
VALUES
  ('PlayStation 4', '399', '2013-11-15', 'Sony', '94200000', '1');
INSERT INTO platforms
  (name, price, launch_date, manufacturer, units_sold, generations_id)
VALUES
  ('Nintendo Switch', '299', '2017-03-03', 'Nintendo', '34740000', '2');
INSERT INTO platforms
  (name, price, launch_date, manufacturer, units_sold, generations_id)
VALUES
  ('PlayStation 3', '499', '2006-11-11', 'Sony', '95000000', '3');
INSERT INTO platforms
  (name, price, launch_date, manufacturer, units_sold, generations_id)
VALUES
  ('Xbox 360', '299', '2005-11-22', 'Microsoft', '93120000', '4');
INSERT INTO platforms
  (name, price, launch_date, manufacturer, units_sold, generations_id)
VALUES
  ('Xbox One', '499', '2013-11-22', 'Microsoft', '52100000', '5');
