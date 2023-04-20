import mysql

from src.db.connection import DatabaseConnector


class Kategorie:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def add(self, nazev, popis):
        """
        Metoda vytvoří novou kategorii
        :param nazev: Název kategorie
        :param popis: Popis kategorie
        """
        try:
            sql_insert_kategorie = "insert into kategorie(nazev, popis) values (%s,%s)"
            val_insert_kategorie = (nazev, popis)
            self.cursor.execute(sql_insert_kategorie, val_insert_kategorie)
            self.connection.commit()
        except Exception as err:
            print("Došlo k chybě při vkládání nové kategorie do databáze:", err)

    def findAll(self):
        """
        Metoda vypíše všechny kategorie
        """
        try:
            self.cursor.execute("select * from kategorie")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V kategorii neexistuje žádný záznam.")
        except Exception as e:
            print("Došlo k chybě při vyhledávání v tabulce kategorie:", e)

    def updatePopis(self, nazev, novy_popis):
        """
        Metoda změní popis kategorie
        :param nazev: Název kategorie
        :param novy_popis: Nový popis kategorie
        """
        sql_update_kategorie = "update kategorie set popis = %s where nazev = %s"
        val_update_kategorie = (novy_popis, nazev)
        try:
            self.cursor.execute(sql_update_kategorie, val_update_kategorie)
            if self.cursor.rowcount == 0:
                print(f"Kategorie s názvem {nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit popis kategorie {nazev}.")


    def delete(self, nazev):
        """
        Metoda smaže kategorii
        :param nazev: Název kategorie
        """
        sql_delete_kategorie = "delete from kategorie where nazev = %s"
        val_delete_kategorie = (nazev,)
        try:
            self.cursor.execute(sql_delete_kategorie, val_delete_kategorie)
            if self.cursor.rowcount == 0:
                print(f"Kategorie s názvem {nazev} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se smazat kategorie {nazev}.")




