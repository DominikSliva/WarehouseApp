create database dominiksliva_cz;
use dominiksliva_cz;
drop database dominiksliva_cz;

-- * Tabulky
create table lokace_ulozeni(
id int primary key auto_increment not null,
lokace varchar(50) not null unique, 
kapacita int not null
);

create table dodavatel(
id int primary key auto_increment not null,
nazev varchar(100) not null unique,
adresa varchar(255) not null,
telefon varchar(30) not null unique
);

create table kategorie(
id int primary key auto_increment not null,
nazev varchar(80) not null unique,
popis text not null
);

create table polozka(
id int primary key auto_increment not null,
nazev varchar(50) not null unique,
cena float(10,2) not null check(cena > 0),
kod int not null unique,
pocet_ks int not null check(cena >= 0),
lokace_ulozeni_id int not null,
dodavatel_id int not null,
kategorie_id int not null,
foreign key (lokace_ulozeni_id) references lokace_ulozeni(id),
foreign key (dodavatel_id) references dodavatel(id),
foreign key (kategorie_id) references kategorie(id)
);


create table historie_pohybu_polozky(
id int primary key auto_increment not null,
datum datetime not null default now(),
polozka_id int not null,
puvodni_lokace_id int not null,
nova_lokace_id int not null,
foreign key (polozka_id) references polozka(id),
foreign key (puvodni_lokace_id) references lokace_ulozeni(id),
foreign key (nova_lokace_id) references lokace_ulozeni(id)
);

create table zakaznik(
id int primary key auto_increment not null,
jmeno varchar(50) not null,
prijmeni varchar(50) not null unique,
email varchar(50) not null unique,
adresa varchar(255) not null,
telefon varchar(30) not null unique
);

create table objednavka(
id int primary key auto_increment not null,
cena_objednavky float(10,2) not null default 0,
datum_objednavky date not null default now(),
expedovana_objednavka tinyint(1) not null default 0,
zakaznik_id int not null,
foreign key (zakaznik_id) references zakaznik(id)
);


create table polozka_v_objednavce(
id int primary key auto_increment not null,
objednavka_id int not null,
polozka_id int not null,
foreign key (objednavka_id) references objednavka(id),
foreign key (polozka_id) references polozka(id),
ks_polozek int not null check(ks_polozek > 0)
);

-- * Pohledy a trigery
-- Triger pro automatické sčítání celkové ceny objednávky
DELIMITER $$
CREATE TRIGGER update_cena_objednavky
AFTER INSERT ON polozka_v_objednavce
FOR EACH ROW
BEGIN
   UPDATE objednavka 
   SET cena_objednavky = 
   (SELECT SUM(polozka.cena * polozka_v_objednavce.ks_polozek) 
    FROM polozka_v_objednavce 
    JOIN polozka ON polozka.id = polozka_v_objednavce.polozka_id 
    WHERE polozka_v_objednavce.objednavka_id = NEW.objednavka_id)
   WHERE id = NEW.objednavka_id;
END $$
DELIMITER ;

-- Triger pro automatické ukladání do historie, po změně lokace ulozeni
DELIMITER $$
CREATE TRIGGER polozka_moved
AFTER UPDATE ON polozka
FOR EACH ROW
BEGIN
    IF NEW.lokace_ulozeni_id <> OLD.lokace_ulozeni_id THEN
        INSERT INTO historie_pohybu_polozky (polozka_id, puvodni_lokace_id, nova_lokace_id)
        VALUES (NEW.id, OLD.lokace_ulozeni_id, NEW.lokace_ulozeni_id);
    END IF;
END$$
DELIMITER ;
SHOW TRIGGERS;


CREATE VIEW polozky_a_lokace AS
SELECT polozka.nazev AS polozka, lokace_ulozeni.lokace AS lokace
FROM polozka
JOIN lokace_ulozeni ON polozka.lokace_ulozeni_id = lokace_ulozeni.id;


CREATE VIEW pohled_na_zasoby AS
SELECT 
    p.id AS id_polozky, 
    p.nazev AS nazev_polozky, 
    p.cena AS cena_polozky, 
    p.pocet_ks AS pocet_ks, 
    l.lokace AS lokace_ulozeni, 
    l.kapacita AS kapacita_lokace, 
    COUNT(*) AS obsazeno_v_lokaci
FROM polozka p
JOIN lokace_ulozeni l ON p.lokace_ulozeni_id = l.id
GROUP BY p.id, l.id;


CREATE VIEW vsechny_objednavky AS
SELECT zakaznik.jmeno, zakaznik.prijmeni, objednavka.datum_objednavky, 
CASE 
    WHEN objednavka.expedovana_objednavka = 1 THEN 'expedováno'
    ELSE 'neexpedováno'
END AS 'stav_objednavky'
FROM zakaznik
JOIN objednavka ON zakaznik.id = objednavka.zakaznik_id;

CREATE VIEW historie_pohybu_polozky_view AS
SELECT h.id, h.datum, p.nazev AS polozka, l1.lokace AS puvodni_lokace, l2.lokace AS nova_lokace
FROM historie_pohybu_polozky h
INNER JOIN polozka p ON h.polozka_id = p.id
INNER JOIN lokace_ulozeni l1 ON h.puvodni_lokace_id = l1.id
INNER JOIN lokace_ulozeni l2 ON h.nova_lokace_id = l2.id;

-- * DATA
insert into lokace_ulozeni (lokace, kapacita) values ('100-0-0', 28);
insert into lokace_ulozeni (lokace, kapacita) values ('100-0-1', 25);
insert into lokace_ulozeni (lokace, kapacita) values ('100-0-2', 12);
insert into lokace_ulozeni (lokace, kapacita) values ('100-0-3', 17);
insert into lokace_ulozeni (lokace, kapacita) values ('100-1-0', 22);
insert into lokace_ulozeni (lokace, kapacita) values ('100-1-1', 27);
insert into lokace_ulozeni (lokace, kapacita) values ('100-1-2', 12);
insert into lokace_ulozeni (lokace, kapacita) values ('100-1-3', 27);
insert into lokace_ulozeni (lokace, kapacita) values ('100-2-0', 17);
insert into lokace_ulozeni (lokace, kapacita) values ('100-2-1', 21);
insert into lokace_ulozeni (lokace, kapacita) values ('100-2-2', 23);
insert into lokace_ulozeni (lokace, kapacita) values ('100-2-3', 30);
insert into lokace_ulozeni (lokace, kapacita) values ('100-3-0', 17);
insert into lokace_ulozeni (lokace, kapacita) values ('100-3-1', 26);
insert into lokace_ulozeni (lokace, kapacita) values ('100-3-2', 28);
insert into lokace_ulozeni (lokace, kapacita) values ('100-3-3', 21);
insert into lokace_ulozeni (lokace, kapacita) values ('100-4-0', 27);
insert into lokace_ulozeni (lokace, kapacita) values ('100-4-1', 15);
insert into lokace_ulozeni (lokace, kapacita) values ('100-4-2', 13);
insert into lokace_ulozeni (lokace, kapacita) values ('100-4-3', 11);
insert into lokace_ulozeni (lokace, kapacita) values ('100-5-0', 40);


insert into dodavatel (nazev, adresa, telefon) values ('Shufflebeat', '1201 Ruskin Road', '1633581785');
insert into dodavatel (nazev, adresa, telefon) values ('Twimbo', '92888 Prentice Lane', '9216637231');
insert into dodavatel (nazev, adresa, telefon) values ('Oyope', '14 Jackson Avenue', '3162206783');
insert into dodavatel (nazev, adresa, telefon) values ('Dynava', '96 Meadow Valley Drive', '7056298714');
insert into dodavatel (nazev, adresa, telefon) values ('Dabjam', '1 Heffernan Park', '2228212785');
insert into dodavatel (nazev, adresa, telefon) values ('Eabox', '54 Hayes Plaza', '2622954599');
insert into dodavatel (nazev, adresa, telefon) values ('Zooxo', '910 1st Street', '1003237647');
insert into dodavatel (nazev, adresa, telefon) values ('Brainlounge', '5 Artisan Trail', '9082823743');
insert into dodavatel (nazev, adresa, telefon) values ('Jaloo', '0 Clyde Gallagher Street', '4509849211');
insert into dodavatel (nazev, adresa, telefon) values ('Pixope', '937 Talisman Plaza', '9013037903');

insert into kategorie(nazev, popis) values ("Potraviny","Potraviny");
insert into kategorie(nazev, popis) values ("Zahradnické nástroje","Zahradnické nástroje");
insert into kategorie(nazev, popis) values ("Hnojivo","Hnojivo");
insert into kategorie(nazev, popis) values ("Nářadí","Nářadí");
insert into kategorie(nazev, popis) values ("Dekorace","Dekorace");


insert into polozka(nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values("Konev", "200", "10001", 10, 1, 1, 1);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Hnojivo pokojové 10L', 1347, 10002, 30, 1, 1, 3);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Hnojivo pokojové 20L', 1292, 10003, 25, 2, 1, 3);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Hnojivo pokojové 40L', 1221, 10004, 25, 3, 1, 3);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Hnojivo pokojové 50L', 927, 10005, 11, 4, 1, 3);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Sekera X10', 1475, 10006, 16, 5, 2, 2);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Sekera X12', 1437, 10007, 15, 5, 2, 2);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Sekera X15', 275, 10008, 25, 6, 2, 2);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Sekera X18', 1474, 10009, 24, 6, 2, 2);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Sekera X22', 502, 10010, 11, 7, 2, 2);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Kladivo', 595, 10011, 20, 8, 3, 5);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Kladívko', 801, 10012, 14, 8, 3, 5);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Čajová svíčka 5ks', 1053, 10013, 14, 9, 4, 5);
insert into polozka (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) values ('Čajová svíčka 10ks', 1260, 10014, 19, 10, 4, 5);

insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Dorita', 'Baylis', 'dbaylis0@weibo.com', '360 Carberry Court', '5662001481');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Arman', 'Schinetti', 'aschinetti1@hostgator.com', '5 Huxley Hill', '9437945270');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Caldwell', 'Halgarth', 'chalgarth2@freewebs.com', '5948 Duke Court', '1781386719');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Constancy', 'Coenraets', 'ccoenraets3@elpais.com', '0 Doe Crossing Center', '9901342894');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Samantha', 'Southan', 'ssouthan4@comsenz.com', '17 Dwight Junction', '9187487828');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Micheil', 'Nabarro', 'mnabarro5@theglobeandmail.com', '5370 Del Mar Trail', '9589594898');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Orsola', 'Frayling', 'ofrayling6@miitbeian.gov.cn', '68838 Hagan Circle', '2514487190');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Cherida', 'Beckworth', 'cbeckworth7@chicagotribune.com', '88220 Sycamore Center', '2672326444');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Mariellen', 'Maghull', 'mmaghull8@time.com', '20160 Morning Drive', '1786424918');
insert into zakaznik (jmeno, prijmeni, email, adresa, telefon) values ('Priscilla', 'MacEvilly', 'pmacevilly9@umn.edu', '8 4th Pass', '8293064048');

insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2019-03-28 14:28:30', 0, 9);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2019-08-03 16:41:15', 1, 9);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2021-07-12 19:35:22', 1, 4);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2020-09-26 01:13:52', 0, 5);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2019-01-21 17:12:36', 0, 4);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2022-02-14 19:46:39', 0, 6);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2021-11-28 12:15:20', 1, 3);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2018-03-25 05:19:22', 0, 3);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2021-05-30 07:59:15', 0, 8);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2022-11-13 03:20:17', 0, 6);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2020-11-02 02:08:48', 1, 1);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2022-09-08 18:25:31', 1, 1);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2020-09-05 20:47:27', 1, 6);
insert into objednavka (cena_objednavky, datum_objednavky, expedovana_objednavka, zakaznik_id) values (0, '2022-10-12 18:44:33', 1, 4);
insert into objednavka (datum_objednavky, expedovana_objednavka, zakaznik_id) values ('2018-11-09 04:06:27', 1, 1);

insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (1, 9, 1);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (1, 8, 1);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (3, 4, 6);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (4, 4, 3);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (5, 7, 4);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (6, 10, 2);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (7, 6, 1);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (8, 5, 9);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (9, 3, 6);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (10, 12, 4);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (11, 10, 10);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (12, 7, 1);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (13, 11, 4);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (14, 11, 7);
insert into polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) values (15, 5, 6);
