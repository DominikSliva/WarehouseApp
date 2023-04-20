import mysql

from src.db.connection import DatabaseConnector


class LokaceUlozeni:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def add(self, lokace, kapacita):
        """
        Metoda vytvoří novou lokaci pro uložení položek
        :param lokace: Název lokace
        :param kapacita: Kapacita lokace
        """
        try:
            sql_insert_lokace_ulozeni = "insert into lokace_ulozeni(lokace, kapacita) values (%s,%s)"
            val_insert_lokace_ulozeni = (lokace, kapacita)
            self.cursor.execute(sql_insert_lokace_ulozeni, val_insert_lokace_ulozeni)
            self.connection.commit()
        except Exception as err:
            print("Došlo k chybě při vkládání nové lokace uložení do databáze")

    def findAll(self):
        """
        Metoda vypíše všechny lokace
        """
        try:
            self.cursor.execute("select * from lokace_ulozeni")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V lokacích uložení neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def findByLokace(self, lokace):
        """
        Metoda vypíše lokaci a vybraným názvem lokace
        :param lokace: Název lokace
        """
        sql_select_lokace_ulozeni = "select * from lokace_ulozeni where lokace = %s"
        val_select_lokace_ulozeni = (lokace,)
        try:
            self.cursor.execute(sql_select_lokace_ulozeni, val_select_lokace_ulozeni)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Lokace s názvem {lokace} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání lokace uložení:", err)


    def findByKapacita(self, kapacita):
        """
        Metoda vypíše lokace podle zadané kapacity
        :param kapacita: Kapacita lokace
        """
        sql_select_lokace_ulozeni = "select * from lokace_ulozeni where kapacita = %s"
        val_select_lokace_ulozeni = (kapacita,)
        try:
            self.cursor.execute(sql_select_lokace_ulozeni, val_select_lokace_ulozeni)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Lokace s kapacitou {kapacita} neexistuje.")
        except Exception as e:
            print("Došlo k chybě při vyhledávání lokace uložení:", e)

    def updateLokace(self, stara_lokace, nova_lokace):
        """
        Metoda změní název lokace
        :param stara_lokace: Název lokace, který chceme změnit
        :param nova_lokace: Nový název lokace
        """
        sql_update_lokace_ulozeni = "update lokace_ulozeni set lokace = %s where lokace = %s"
        val_update_lokace_ulozeni = (nova_lokace, stara_lokace)
        try:
            self.cursor.execute(sql_update_lokace_ulozeni, val_update_lokace_ulozeni)
            if self.cursor.rowcount == 0:
                print(f"Lokace uložení s názvem {stara_lokace} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit lokaci s názvem {stara_lokace}.")

    def updateKapacita(self, lokace, nova_kapacita):
        """
        Metoda změní kapacitu lokace
        :param lokace: Název lokace
        :param nova_kapacita: Nová kapacita lokace
        """
        sql_update_lokace_ulozeni = "update lokace_ulozeni set kapacita = %s where lokace = %s"
        val_update_lokace_ulozeni = (nova_kapacita, lokace)
        try:
            self.cursor.execute(sql_update_lokace_ulozeni, val_update_lokace_ulozeni)
            if self.cursor.rowcount == 0:
                print(f"Lokace uložení s názvem {lokace} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit kapacitu lokace s názvem {lokace}.")

    def delete(self, lokace):
        """
        Metoda smaže lokaci
        :param lokace: Název lokace
        """
        sql_delete_lokace_ulozeni = "delete from lokace_ulozeni where lokace = %s"
        val_delete_lokace_ulozeni = (lokace,)
        try:
            self.cursor.execute(sql_delete_lokace_ulozeni, val_delete_lokace_ulozeni)
            if self.cursor.rowcount == 0:
                print(f"Lokace uložení s názvem {lokace} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se smazat lokaci uložení {lokace}.")





