import mysql

from src.db.connection import DatabaseConnector


class Objednavka:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def addDateNow(self, jmeno_zakaznika, prijmeni_zakaznika):
        """
        Metoda vytvoří novou objednávku s momentálním datumem a přiřadí jí vybranému zákazníkovi
        :param jmeno_zakaznika: Jméno zákazníka
        :param prijmeni_zakaznika: Příjmení zákazníka
        :return:
        """
        sql_insert_objednavka = "insert into objednavka (zakaznik_id) values ((SELECT id FROM zakaznik WHERE jmeno = %s AND prijmeni = %s)) "
        val_insert_objednavka = (jmeno_zakaznika, prijmeni_zakaznika)
        try:
            self.cursor.execute(sql_insert_objednavka, val_insert_objednavka)
            self.connection.commit()
        except Exception as err:
            print("Došlo k chybě při vkládání nové objednávky do databáze, "
                  "zkontrolujte zda se uživatel nachází v databázi. Pokud ne, musíte nejprve vytvořit nového zákazníka.")

    def addAnyDate(self, jmeno_zakaznika, prijmeni_zakaznika, datum_objednavky):
        """
        Metoda vytvoří novou objednávku, přiřadí jí vybranému zákazníkovi a datum si zvolí uživatel
        :param jmeno_zakaznika: Jméno zákazníka
        :param prijmeni_zakaznika: Příjmení zákazníka
        :param datum_objednavky: Datum objednávky (formát YYYY-MM-DD)
        """
        sql_insert_objednavka = "insert into objednavka (datum_objednavky, zakaznik_id) values (%s,(SELECT id FROM zakaznik WHERE jmeno = %s AND prijmeni = %s)) "
        val_insert_objednavka = (datum_objednavky, jmeno_zakaznika, prijmeni_zakaznika)
        try:
            self.cursor.execute(sql_insert_objednavka, val_insert_objednavka)
            self.connection.commit()
        except Exception as err:
            print("Došlo k chybě při vkládání nové objednávky do databáze, "
                  "zkontrolujte zda se uživatel nachází v databázi. Pokud ne, musíte nejprve vytvořit nového zákazníka.")
    def findAll(self):
        """
        Metoda vypíše všechny objednávky
        """
        try:
            self.cursor.execute("select * from objednavka")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V objednávkách neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def findObjednavkyByZakaznik(self, jmeno, prijmeni):
        """
        Metoda vypíše všechny objednávky, které vlastní vybraný zákazník
        :param jmeno: Jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        """
        global vysledek
        sql_select_objednavka = "SELECT objednavka.* FROM objednavka JOIN zakaznik ON " \
                                "objednavka.zakaznik_id = zakaznik.id WHERE zakaznik.jmeno = %s " \
                                "AND zakaznik.prijmeni = %s"
        val_select_objednavka = (jmeno, prijmeni)
        try:
            self.cursor.execute(sql_select_objednavka, val_select_objednavka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"U zákazník {jmeno} {prijmeni} neexistuje žádná objednávka.")
                return False
            return True
        except Exception as err:
            print("Došlo k chybě při vyhledávání objednávky zákazníka:", err)

    def findByNeexpedovano(self):
        """
        Metoda vypíše všechny neexpedované objednávky
        """
        try:
            self.cursor.execute("select * from objednavka where expedovana_objednavka = 0")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Žádné objednávky nejsou neexpedované.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání objednávky zákazníka:", err)

    def findByExpedovano(self):
        """
        Metoda vypíše všechny expedované objednávky
        """
        try:
            self.cursor.execute("select * from objednavka where expedovana_objednavka = 1")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Žádné objednávky nejsou expedované.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání objednávky zákazníka:", err)

    def findByDatum(self, datum):
        """
        Metoda vypíše všechny objednávky s vybraným datumem
        :param datum: Datum objednávky (formát YYYY-MM-DD)
        """
        sql_select_objednavka = "select * from objednavka where datum_objednavky = %s"
        val_select_objednavka = (datum,)
        try:
            self.cursor.execute(sql_select_objednavka, val_select_objednavka)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Objednávka s datem {datum} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání objednávky:", err)

    def updateNaExpedovano(self, jmeno, prijmeni, objednavka_id ):
        """
        Metoda změní objednávku na expedovanou
        :param jmeno: Jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param objednavka_id: ID objednávky
        """
        # !! VOLAT METODU findObjednavkyByZakaznik z file objednavka
        sql_update_objednavka = "UPDATE objednavka SET expedovana_objednavka = 1 " \
                                "WHERE zakaznik_id = (SELECT id FROM zakaznik " \
                                "WHERE jmeno = %s AND prijmeni = %s) " \
                                "AND id = %s"
        val_update_objednavka = (jmeno, prijmeni, objednavka_id)
        try:
            self.cursor.execute(sql_update_objednavka, val_update_objednavka)
            if self.cursor.rowcount == 0:
                print(f"Objednávka zákazníka {jmeno} {prijmeni} s ID objednávky {objednavka_id} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit objednávku zákazníka {jmeno} {prijmeni}.")

    def updateNaNeexpedovano(self, jmeno, prijmeni, objednavka_id ):
        """
        Metoda změní objednávku na neexpedovanou
        :param jmeno: Jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param objednavka_id: ID objednávky
        """
        # !! VOLAT METODU findObjednavkyByZakaznik z file objednavka
        sql_update_objednavka = "UPDATE objednavka SET expedovana_objednavka = 0 " \
                                "WHERE zakaznik_id = (SELECT id FROM zakaznik " \
                                "WHERE jmeno = %s AND prijmeni = %s) " \
                                "AND id = %s"
        val_update_objednavka = (jmeno, prijmeni, objednavka_id)
        try:
            self.cursor.execute(sql_update_objednavka, val_update_objednavka)
            if self.cursor.rowcount == 0:
                print(f"Objednávka zákazníka {jmeno} {prijmeni} s ID objednávky {objednavka_id} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit objednávku zákazníka {jmeno} {prijmeni}.")

    def delete(self, jmeno, prijmeni, objednavka_id):
        """
        Metoda smaže objednávku
        :param jmeno: Jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param objednavka_id: ID objednávky
        """
        # !! VOLAT METODU findObjednavkyByZakaznik z file objednavka
        sql_delete_objednavka = "DELETE FROM objednavka WHERE zakaznik_id = (SELECT id FROM zakaznik WHERE jmeno = %s AND prijmeni = %s) AND id = %s"
        val_delete_objednavka = (jmeno, prijmeni, objednavka_id)
        try:
            self.cursor.execute(sql_delete_objednavka, val_delete_objednavka)
            if self.cursor.rowcount == 0:
                print(f"Objednávka zákazníka {jmeno} {prijmeni} s ID objednávky {objednavka_id} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se smazat objednávku zákazníka {jmeno} {prijmeni}.")

