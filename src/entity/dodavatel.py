import mysql
from src.db.connection import DatabaseConnector


class Dodavatel:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def add(self, nazev, adresa, telefon):
        """
        Metoda vytvoří nového dodavatele
        :param nazev: Název dodavatele
        :param adresa: Adresa dodavatele
        :param telefon: Telefonní číslo dodavatele (format ###-###-###)
        """
        try:
            sql_insert_dodavatel = "insert into dodavatel(nazev, adresa, telefon) values (%s,%s,%s)"
            val_insert_dodavatel = (nazev, adresa, telefon)
            self.cursor.execute(sql_insert_dodavatel, val_insert_dodavatel)
            self.connection.commit()
        except Exception as err:
            print("Došlo k chybě při vkládání nového dodavatele do databáze",err)

    def findAll(self):
        """
        Metoda vypíše všechny dodavatele
        """
        try:
            self.cursor.execute("select * from dodavatel")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V dodavatelech neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def findByName(self, nazev):
        """
        Metoda vypíše dodavatele s vybraným názvem
        :param nazev: Název dodavatele
        """
        sql_select_dodavatel = "select * from dodavatel where nazev = %s"
        val_select_dodavatel = (nazev,)

        try:
            self.cursor.execute(sql_select_dodavatel, val_select_dodavatel)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Dodavatel s názvem {nazev} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání dodavatele:", err)

    def findByAdress(self, adresa):
        """
        Metoda vypíše dodavatele s vybranou adresou
        :param adresa: Adresa dodavatele
        """
        sql_select_dodavatel = "select * from dodavatel where adresa = %s"
        val_select_dodavatel = (adresa,)
        try:
            self.cursor.execute(sql_select_dodavatel, val_select_dodavatel)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Dodavatel s adresou {adresa} neexistuje.")
        except Exception as e:
            print("Došlo k chybě při vyhledávání dodavatele:", e)

    def findByPhone(self, telefon):
        """
        Metoda vypíše dodavatele s vybraným telefonním číslem
        :param telefon: Telefonní číslo dodavatele
        """
        sql_select_dodavatel = "select * from dodavatel where telefon = %s"
        val_select_dodavatel = (telefon,)
        try:
            self.cursor.execute(sql_select_dodavatel, val_select_dodavatel)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Dodavatel s telefonním číslem {telefon} neexistuje.")
        except Exception as e:
            print("Došlo k chybě při vyhledávání dodavatele:", e)

    def updateName(self, stary_nazev, novy_nazev):
        """
        Metoda přepíše název dodavatele
        :param stary_nazev: Název dodavatele
        :param novy_nazev: Nový název dodavatele
        """
        sql_update_dodavatel = "update dodavatel set nazev = %s where nazev = %s"
        val_update_dodavatel = (novy_nazev, stary_nazev)
        try:
            self.cursor.execute(sql_update_dodavatel, val_update_dodavatel)
            if self.cursor.rowcount == 0:
                print(f"Dodavatel s názvem {stary_nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit dodavatele s názvem {stary_nazev}.")

    def updateAdress(self, nazev, adresa):
        """
        Metoda přepíše adresu dodavatele
        :param nazev: Název dodavatele
        :param adresa: Nová adresa dodavatele
        """
        sql_update_dodavatel = "update dodavatel set adresa = %s where nazev = %s"
        val_update_dodavatel = (adresa, nazev)
        try:
            self.cursor.execute(sql_update_dodavatel, val_update_dodavatel)
            if self.cursor.rowcount == 0:
                print(f"Dodavatel s názvem {nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit dodavatele s názvem {nazev}.")

    def updatePhone(self, nazev, telefon):
        """
        Metoda přepíše telefonní číslo dodavatele
        :param nazev: Název dodavatele
        :param telefon: Nové telefonní číslo
        """
        sql_update_dodavatel = "update dodavatel set telefon = %s where nazev = %s"
        val_update_dodavatel = (telefon, nazev)
        try:
            self.cursor.execute(sql_update_dodavatel, val_update_dodavatel)
            if self.cursor.rowcount == 0:
                print(f"Dodavatel s názvem {nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit dodavatele s názvem {nazev}.")

    def delete(self, nazev):
        """
        Metoda smaže dodavatele
        :param nazev: Název dodavatele
        """
        sql_delete_dodavatel = "delete from dodavatel where nazev = %s"
        val_delete_dodavatel = (nazev,)
        try:
            self.cursor.execute(sql_delete_dodavatel, val_delete_dodavatel)
            if self.cursor.rowcount == 0:
                print(f"Dodavatel s názvem {nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se smazat dodavatele s názvem {nazev}.")


