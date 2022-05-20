begin;
create schema Startups;
use Startups;
create table startup(
	id_startup INT NOT NULL,
    nome_startup VARCHAR (30) NOT NULL,
    cidade_sede VARCHAR (30),
    PRIMARY KEY (id_startup));

create table programador(
	id_programador INT NOT NULL,
    id_startup INT NOT NULL,
    nome_programador VARCHAR (30),
    genero CHAR (1),
    data_nascimento DATE NOT NULL,
    email VARCHAR (50) NOT NULL,
    PRIMARY KEY (id_programador),
    FOREIGN KEY (id_startup) REFERENCES startup(id_startup) ON UPDATE CASCADE,
    UNIQUE (email));
    
create table linguagem_programacao(
	id_linguagem INT NOT NULL,
    nome_linguagem VARCHAR (20) NOT NULL,
    ano_lancamento CHAR (4),
    PRIMARY KEY (id_linguagem));

create table programador_linguagem(
	id_programador INT NOT NULL,
    id_linguagem INT NOT NULL,
    FOREIGN KEY (id_programador) REFERENCES programador(id_programador) ON DELETE CASCADE,
    FOREIGN KEY (id_linguagem) REFERENCES linguagem_programacao(id_linguagem) ON DELETE RESTRICT);
    
INSERT INTO startup VALUES
	('10001', 'Tech4Toy', 'Porto Alegre'),
    ('10002', 'Smart123', 'Belo Horizonte'),
    ('10003', 'knowledgeUp', 'Rio de Janeiro'),
    ('10004', 'BSI Next Level', 'Recife'),
    ('10005', 'QualiHealth', 'São Paulo'),
    ('10006', 'ProEdu', 'Florianópolis');

INSERT INTO programador VALUES
	('30001','10001','João Pedro','M','1993/06/23','joaop@mail.com'),
    ('30002','10002','Paula Silva','F','1986/01/10','paulas@mail.com'),
    ('30003','10003','Renata Vieira','F','1991/07/05','renatav@mail.com'),
    ('30004','10004','Felipe Santos','M','1976/11/25','felipes@mail.com'),
    ('30005','10001','Ana Cristina','F','1968/02/19','anac@mail.com'),
    ('30006','10004','Alexandre Alves','M','1988/07/07','alexandrea@mail.com'),
    ('30007','10002','Laura Marques','F','1987/10/04','lauram@mail.com');

INSERT INTO linguagem_programacao VALUES
	('20001', 'Python', '1991'),
    ('20002', 'PHP', '1995'),
    ('20003', 'Java', '1995'),
    ('20004', 'C', '1972'),
    ('20005', 'JavaScript', '1995'),
    ('20006', 'Dart', '2011');

INSERT INTO programador_linguagem VALUES
('30001', '20001'),
('30001', '20002'),
('30002', '20003'),
('30003', '20004'),
('30003', '20005'),
('30004', '20005'),
('30007', '20001'),
('30007', '20002');


DELIMITER $$
CREATE TRIGGER checa_genero
BEFORE INSERT ON programador
FOR EACH ROW
BEGIN
IF NEW.genero not in ('M', 'F')  THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='Caracter inválido para gênero. Utilize M ou F.';
END IF;
END $$
DELIMITER ;


CREATE VIEW contagem_funcionarios
AS
select s.nome_startup as startup, count(p.nome_programador) as count from startup s left outer join programador p on p.id_startup=s.id_startup group by s.nome_startup;

CREATE VIEW contagem_homens
AS
select s.nome_startup as startup, count(p.nome_programador) as Homens from startup s left join programador p on p.genero='M' and p.id_startup=s.id_startup group by s.nome_startup;

CREATE VIEW contagem_mulheres
AS
select s.nome_startup as startup, count(p.nome_programador) as Mulheres from startup s left join programador p on p.genero='F' and p.id_startup=s.id_startup group by s.nome_startup;

CREATE VIEW contagem_programadoreslinguagem 
AS
SELECT LP.id_linguagem,
       LP.nome_linguagem,
       COUNT(PL.id_programador)  AS numero_de_programadores
FROM linguagem_programacao AS LP
JOIN programador_linguagem AS PL ON LP.id_linguagem = PL.id_linguagem 
JOIN programador AS P ON P.id_programador = PL.id_programador
GROUP BY LP.id_linguagem;


