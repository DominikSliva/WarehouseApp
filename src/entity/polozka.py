import mysql

from src.db.connection import DatabaseConnector


class Polozka:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def add(self, nazev, cena, kod, pocet_ks, lokace, dodavatel_nazev, kategorie_nazev):
        """
        Metoda vytvoří novou položku ve skladě
        :param nazev: Název nové položky
        :param cena: Cena položky
        :param kod: Unikátní kód položky (pětičíselné číslo)
        :param pocet_ks: Počet kusů na skladě
        :param lokace: Název lokace umístění položky
        :param dodavatel_nazev: Název dodavatele
        :param kategorie_nazev: Název kategorie
        :return:
        """
        global lokace_ulozeni_id, dodavatel_id, kategorie_id
        try:
            self.cursor.execute("Start TRANSACTION")

            sql_lokace_id = "select id from lokace_ulozeni where lokace = %s"
            val_lokace_id = (lokace,)
            try:
                self.cursor.execute(sql_lokace_id, val_lokace_id)
                lokace_ulozeni_id = self.cursor.fetchall()[0][0]
                if not lokace_ulozeni_id:
                    print(f"Lokace s názvem {lokace} neexistuje")
            except Exception as err:
                print(f"Došlo k chybě při vyhledávání lokace:", err)

            sql_dodavatel_id = "select id from dodavatel where nazev = %s"
            val_dodavatel_id = (dodavatel_nazev,)
            try:
                self.cursor.execute(sql_dodavatel_id, val_dodavatel_id)
                dodavatel_id = self.cursor.fetchall()[0][0]
                if not dodavatel_id:
                    print(f"Dodavatel s názvem {dodavatel_nazev} neexistuje")
            except Exception as err:
                print(f"Došlo k chybě při vyhledávání dodavatele:", err)

            sql_kategorie_id = "select id from kategorie where nazev = %s"
            val_kategorie_id = (kategorie_nazev,)
            try:
                self.cursor.execute(sql_kategorie_id, val_kategorie_id)
                kategorie_id = self.cursor.fetchall()[0][0]
                if not kategorie_id:
                    print(f"Kategorie s názvem {kategorie_nazev} neexistuje")
            except Exception as err:
                print(f"Došlo k chybě při vyhledávání kategorie:", err)

            sql_insert_polozka = "insert into polozka(nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id) " \
                                 "values (%s, %s, %s, %s, %s, %s, %s)"
            val_insert_polozka = (nazev, cena, kod, pocet_ks, lokace_ulozeni_id, dodavatel_id, kategorie_id)
            self.cursor.execute(sql_insert_polozka, val_insert_polozka)
            self.connection.commit()

        except Exception as err:
            print("Došlo k chybě při vkládání nového dodavatele do databáze")
            self.connection.rollback()

    def findAll(self):
        """
        Metoda vypíše všechny položky uložené v databázi
        """
        try:
            self.cursor.execute("select * from polozka")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V objednávkách neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def findByCena(self, cena):
        """
        Metoda vypíše všechny položky se zvolenou cenou
        :param cena: Cena položky
        """
        sql_select_polozka = "select * from polozka where cena = %s"
        val_select_polozka = (cena,)
        try:
            self.cursor.execute(sql_select_polozka, val_select_polozka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Položka s cenou {cena} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání položky:", err)

    def findByKod(self, kod):
        """
        Metoda vypíše všechny položky se zvoleným kódem
        :param kod: Unikátní kód položky
        """
        sql_select_polozka = "select * from polozka where kod = %s"
        val_select_polozka = (kod,)
        try:
            self.cursor.execute(sql_select_polozka, val_select_polozka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Položka s kodovým číslem {kod} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání položky:", err)

    def findByPocetKs(self, pocet_ks):
        """
        Metoda vypíše všechny položky se zvoleným počtem kusů
        :param pocet_ks: Počet kusů položek
        """
        sql_select_polozka = "select * from polozka where pocet_ks = %s"
        val_select_polozka = (pocet_ks,)
        try:
            self.cursor.execute(sql_select_polozka, val_select_polozka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Položka s počtem kusů {pocet_ks} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání položky:", err)

    def findByLokaceUlozeni(self, lokace):
        """
        Metoda vypíše všechny položky se zvolenou lokací
        :param lokace: Název lokace umístění
        """
        sql_select_polozka = "select polozka.nazev, polozka.cena, polozka.pocet_ks from polozka join lokace_ulozeni " \
                              "lokace ON polozka.lokace_ulozeni_id = lokace.id where lokace.lokace = %s"
        val_select_polozka = (lokace,)
        try:
            self.cursor.execute(sql_select_polozka, val_select_polozka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Položka s lokací uložení {lokace} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání položky:", err)

    def findByDodavatel(self, dodavatel):
        """
        Metoda vypíše všechny položky se zvoleným dodavatelem
        :param dodavatel: Název dodavatele
        """
        sql_select_polozka = "select polozka.nazev, polozka.cena, polozka.pocet_ks from polozka polozka JOIN dodavatel" \
                             " dodavatel ON polozka.dodavatel_id = dodavatel.id where dodavatel.nazev = %s "
        val_select_polozka = (dodavatel,)
        try:
            self.cursor.execute(sql_select_polozka, val_select_polozka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Položka od dodavatele {dodavatel} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání položky:", err)

    def findByKategorie(self, kategorie):
        """
        Metoda vypíše všechny položky se zvolenou kategorií
        :param kategorie: Název kategorie
        """
        sql_select_polozka = "select polozka.nazev, polozka.cena, polozka.pocet_ks from polozka polozka join kategorie" \
                             " kategorie ON polozka.kategorie_id = kategorie.id where kategorie.nazev = %s "
        val_select_polozka = (kategorie,)
        try:
            self.cursor.execute(sql_select_polozka, val_select_polozka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Položka s kategorií {kategorie} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání položky:", err)

    def updateCena(self, nazev, nova_cena):
        """
        Metoda změní cenu u vybrané položky
        :param nazev: Název položky
        :param nova_cena: Nová cena položky
        """
        sql_update_polozka = "update polozka set cena = %s where nazev = %s"
        val_update_polozka = (nova_cena, nazev)
        try:
            self.cursor.execute(sql_update_polozka, val_update_polozka)
            if self.cursor.rowcount == 0:
                print(f"Položka s názvem {nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit položku s názvem {nazev}. Zkontrolujte prosím zda se položka nachází v databázi.")


    def updateKod(self, nazev, novy_kod):
        """
        Metoda změní kód u vybrané položky
        :param nazev: Název položky
        :param novy_kod: Nový unikátní kód položky
        """
        sql_update_polozka = "update polozka set kod = %s where nazev = %s"
        val_update_polozka = (novy_kod, nazev)
        try:
            self.cursor.execute(sql_update_polozka, val_update_polozka)
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit položku s názvem {nazev} a novým kódem {novy_kod}. Zkontrolujte prosím zda vstupní data jsou validní a kód položky je unikátní")

    def updatePocetKs(self, nazev, novy_pocet_ks):
        """
        Metoda změní počet kusů na skladě u vybrané položky
        :param nazev: Název položky
        :param novy_pocet_ks: Nový počet kusů
        """
        sql_update_polozka = "update polozka set pocet_ks = %s where nazev = %s"
        val_update_polozka = (novy_pocet_ks, nazev)
        try:
            self.cursor.execute(sql_update_polozka, val_update_polozka)
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit položku s názvem {nazev}. Zkontrolujte prosím zda se položka nachází v databázi.")

    def updateLokace(self, nazev, nova_lokace):
        """
        Metoda změní název lokace u vybrané položky
        :param nazev: Název položky
        :param nova_lokace: Nová lokace umístění
        """
        sql_update_polozka = "update polozka set lokace_ulozeni_id = (select id from lokace_ulozeni where lokace = %s) where nazev = %s"
        val_update_polozka = (nova_lokace, nazev)
        try:
            self.cursor.execute(sql_update_polozka, val_update_polozka)
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit položku s názvem {nazev}. Zkontrolujte prosím zda se položka a název lokace nachází v databázi.")

    def updateDodavatel(self, nazev, novy_dodavatel):
        """
        Metoda změní název dodavatele u vybrané položky
        :param nazev: Název položky
        :param novy_dodavatel: Název nového dodavatele
        """
        sql_update_polozka = "update polozka set dodavatel_id = (select id from dodavatel where nazev = %s) where nazev = %s"
        val_update_polozka = (novy_dodavatel, nazev)
        try:
            self.cursor.execute(sql_update_polozka, val_update_polozka)
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit položku s názvem {nazev}. Zkontrolujte prosím zda se položka a název dodavatele nachází v databázi.")

    def updateKategorie(self, nazev, nova_kategorie):
        """
        Metoda změní název kategorie u vybrané položky
        :param nazev: Název položky
        :param nova_kategorie: Název nové kategorie
        """
        sql_update_polozka = "update polozka set kategorie_id = (select id from kategorie where nazev = %s) where nazev = %s"
        val_update_polozka = (nova_kategorie, nazev)
        try:
            self.cursor.execute(sql_update_polozka, val_update_polozka)
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit položku s názvem {nazev}. Zkontrolujte prosím zda se položka a název kategorie nachází v databázi.")

    def delete(self, nazev):
        """
        Metoda smaže položku
        :param nazev: Název položky
        """
        sql_update_polozka = "delete from polozka where nazev = %s"
        val_update_polozka = (nazev,)
        try:
            self.cursor.execute(sql_update_polozka, val_update_polozka)
            if self.cursor.rowcount == 0:
                print(f"Položka s názvem {nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se smazat položku s názvem {nazev}.")
