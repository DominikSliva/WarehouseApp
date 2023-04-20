import csv
from src.db.connection import DatabaseConnector


class RestartDB:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)

    def use_db(self):
        self.cursor.execute("use dominiksliva_cz")

    def smazani_tabulek(self):
        """
        Metoda, která smaže všechny tabulky v databázi
        """
        tabulky = ["polozka_v_objednavce",
                  "objednavka",
                  "zakaznik",
                  "historie_pohybu_polozky",
                  "polozka",
                  "kategorie",
                  "dodavatel",
                  "lokace_ulozeni"]
        try:
            self.use_db()
            self.cursor.execute("Start TRANSACTION")
            for table in tabulky:
                sql = f"DROP TABLE IF EXISTS {table}"
                self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(f"Chyba při mazání tabulek", err)
            self.connection.rollback()

    def smazani_trigeru(self):
        """
        Metoda, která smaže všechny trigery v databázi
        """
        trigery = ["polozka_moved",
                   "update_cena_objednavky"]
        try:
            self.use_db()
            self.cursor.execute("Start TRANSACTION")
            for triggers in trigery:
                sql = f"DROP TRIGGER IF EXISTS {triggers}"
                self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(f"Chyba při mazání trigerů", err)
            self.connection.rollback()

    def smazani_pohledu(self):
        """
        Metoda, která smaže všechny pohledy v databázi
        """
        pohledy = ["pohled_na_zasoby",
                   "polozky_a_lokace",
                   "vsechny_objednavky,"
                   "historie_pohybu_polozky_view"]
        try:
            self.use_db()
            self.cursor.execute("Start TRANSACTION")
            for views in pohledy:
                sql = f"DROP VIEW IF EXISTS {views}"
                self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            print(f"Chyba při mazání pohledů", err)
            self.connection.rollback()

    def vytvoreni_tabulek(self):
        """
        Metoda, která vytvoří tabulky lokace_ulozeni, dodavatel, kategorie, polozka,
        historie_pohybu_polozky, zakaznik, objednavka, polozka_v objednavce
        """
        tabulky = [
            """CREATE TABLE IF NOT EXISTS lokace_ulozeni (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                lokace VARCHAR(50) NOT NULL UNIQUE, 
                kapacita INT NOT NULL
            );""",
            """CREATE TABLE IF NOT EXISTS dodavatel (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                nazev VARCHAR(100) NOT NULL UNIQUE,
                adresa VARCHAR(255) NOT NULL,
                telefon VARCHAR(30) NOT NULL UNIQUE
            );""",
            """CREATE TABLE IF NOT EXISTS kategorie (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                nazev VARCHAR(80) NOT NULL UNIQUE,
                popis TEXT NOT NULL
            );""",
            """CREATE TABLE IF NOT EXISTS polozka (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                nazev VARCHAR(50) NOT NULL UNIQUE,
                cena FLOAT(10,2) NOT NULL CHECK(cena > 0),
                kod INT NOT NULL UNIQUE,
                pocet_ks INT NOT NULL CHECK(cena >= 0),
                lokace_ulozeni_id INT NOT NULL,
                dodavatel_id INT NOT NULL,
                kategorie_id INT NOT NULL,
                FOREIGN KEY (lokace_ulozeni_id) REFERENCES lokace_ulozeni(id),
                FOREIGN KEY (dodavatel_id) REFERENCES dodavatel(id),
                FOREIGN KEY (kategorie_id) REFERENCES kategorie(id)
            );""",
            """CREATE TABLE IF NOT EXISTS historie_pohybu_polozky (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                datum DATETIME NOT NULL DEFAULT NOW(),
                polozka_id INT NOT NULL,
                puvodni_lokace_id INT NOT NULL,
                nova_lokace_id INT NOT NULL,
                FOREIGN KEY (polozka_id) REFERENCES polozka(id),
                FOREIGN KEY (puvodni_lokace_id) REFERENCES lokace_ulozeni(id),
                FOREIGN KEY (nova_lokace_id) REFERENCES lokace_ulozeni(id)
            );""",
            """CREATE TABLE IF NOT EXISTS zakaznik (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                jmeno VARCHAR(50) NOT NULL,
                prijmeni VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(50) NOT NULL UNIQUE,
                adresa VARCHAR(255) NOT NULL,
                telefon VARCHAR(30) NOT NULL UNIQUE
            );""",
            """CREATE TABLE IF NOT EXISTS objednavka (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                cena_objednavky FLOAT(10,2) NOT NULL DEFAULT 0,
                datum_objednavky DATE NOT NULL DEFAULT NOW(),
                expedovana_objednavka TINYINT(1) NOT NULL DEFAULT 0,
                zakaznik_id INT NOT NULL,
                FOREIGN KEY (zakaznik_id) REFERENCES zakaznik(id)
            );""",
            """CREATE TABLE IF NOT EXISTS polozka_v_objednavce (
                id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                objednavka_id INT NOT NULL,
                polozka_id INT NOT NULL,
                FOREIGN KEY (objednavka_id) REFERENCES objednavka(id),
                FOREIGN KEY (polozka_id) REFERENCES polozka(id),
                ks_polozek INT NOT NULL CHECK(ks_polozek > 0)
            );"""
        ]
        try:
            self.use_db()
            self.cursor.execute("Start TRANSACTION")
            for table in tabulky:
                self.cursor.execute(table)
            self.connection.commit()
        except Exception as err:
            print("Chyba při vytváření tabulek")
            self.connection.rollback()

    def vytvoreni_trigeru(self):
        """
        Metoda, která vytvoří trigery pro automatické přepisování celokové ceny,
        a pro automatický zápis do historie_pohybu_polozek při změně lokace položky
        """
        trigery = [
            """CREATE TRIGGER IF NOT EXISTS update_cena_objednavky
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
            END""",
            """CREATE TRIGGER IF NOT EXISTS polozka_moved
            AFTER UPDATE ON polozka
            FOR EACH ROW
            BEGIN
                IF NEW.lokace_ulozeni_id <> OLD.lokace_ulozeni_id THEN
                    INSERT INTO historie_pohybu_polozky (polozka_id, puvodni_lokace_id, nova_lokace_id)
                    VALUES (NEW.id, OLD.lokace_ulozeni_id, NEW.lokace_ulozeni_id);
                END IF;
            END"""
        ]
        try:
            self.use_db()
            self.cursor.execute("Start TRANSACTION")
            for triggers in trigery:
                self.cursor.execute(triggers)
            self.connection.commit()
        except Exception as err:
            print("Chyba při vytváření trigerů")
            self.connection.rollback()

    def vytvoreni_pohledu(self):
        """
        Metoda pro vytvoření pohledů: položky a jejich lokace, pohled na zůstatek zásob,
        všechny objednávky a historie pohybu polozky
        """
        pohledy = [
            """
            CREATE VIEW IF NOT EXISTS polozky_a_lokace AS
            SELECT polozka.nazev AS polozka, lokace_ulozeni.lokace AS lokace
            FROM polozka
            JOIN lokace_ulozeni ON polozka.lokace_ulozeni_id = lokace_ulozeni.id;
            """,
            """
            CREATE VIEW IF NOT EXISTS pohled_na_zasoby AS
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
            """,
            """
            CREATE VIEW vsechny_objednavky AS
            SELECT zakaznik.jmeno, zakaznik.prijmeni, objednavka.datum_objednavky, 
            CASE 
                WHEN objednavka.expedovana_objednavka = 1 THEN 'expedováno'
                ELSE 'neexpedováno'
            END AS 'stav_objednavky'
            FROM zakaznik
            JOIN objednavka ON zakaznik.id = objednavka.zakaznik_id;
            """,
            """
            CREATE VIEW historie_pohybu_polozky_view AS
            SELECT h.id, h.datum, p.nazev AS polozka, l1.lokace AS puvodni_lokace, l2.lokace AS nova_lokace
            FROM historie_pohybu_polozky h
            INNER JOIN polozka p ON h.polozka_id = p.id
            INNER JOIN lokace_ulozeni l1 ON h.puvodni_lokace_id = l1.id
            INNER JOIN lokace_ulozeni l2 ON h.nova_lokace_id = l2.id;
            """
        ]
        try:
            self.use_db()
            self.cursor.execute("Start TRANSACTION")
            for views in pohledy:
                self.cursor.execute(views)
            self.connection.commit()
        except Exception as err:
            print("Chyba při vytváření pohledů")
            self.connection.rollback()

    def export_databaze(self):
        """
        Metoda, která udělá export dat pro každou tabulku, pro ní po té vytvoří soubor pojmenovaný {tabulka}_backup
        """
        try:
            tables = ["lokace_ulozeni", "dodavatel", "kategorie", "polozka", "historie_pohybu_polozky",
                      "zakaznik", "objednavka", "polozka_v_objednavce"]
            for table_name in tables:
                self.cursor.execute(f"SELECT * FROM {table_name}")
                with open(f'data/backup_db/{table_name}_backup.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    headers = ['id'] + [i[0] for i in self.cursor.description[1:]]
                    writer.writerow([''] + headers)
                    # zápis dat
                    for row in self.cursor:
                        writer.writerow([''] + list(row[1:]))
        except Exception as e:
            print("Chyba při exportu databáze: ", e)
            self.connection.rollback()

    def import_databaze(self):
        """
        Metoda, která naimportuje data uložené z posledního backupu.
        Projede každý soubor patřičné tabulky a naimportuje data do tabulky
        """
        try:
            tables = ["lokace_ulozeni", "dodavatel", "kategorie", "polozka", "historie_pohybu_polozky",
                      "zakaznik", "objednavka", "polozka_v_objednavce"]
            for table_name in tables:
                with open(f'data/backup_db/{table_name}_backup.csv', "r") as file:
                    csv_data = csv.reader(file)
                    next(csv_data)
                    for row in csv_data:
                        placeholders = ', '.join(['%s'] * len(row))
                        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                        self.cursor.execute(query, row)
                    self.connection.commit()
        except Exception as err:
            print("Chyba při importu databáze: ", err)
            self.connection.rollback()

