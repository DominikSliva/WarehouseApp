import mysql

from src.db.connection import DatabaseConnector


class PolozkaVObjednavce:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def add(self, objednavka_id, nazev_polozky, pocet_ks):
        """
        Metoda přidá novou položku do objednávky včetně jeho počtu kusů
        :param objednavka_id: ID objednávky
        :param nazev_polozky: Název položky
        :param pocet_ks: Počet kusů
        :return:
        """
        try:
            self.cursor.execute("Start TRANSACTION")
            #self.najdi_objednavky_zakaznika(jmeno, prijmeni)
            #!! VOLAT METODU findObjednavkyByZakaznik z file objednavka

            sql_select_polozka = "SELECT id FROM polozka WHERE nazev = %s"
            val_select_polozka = (nazev_polozky,)

            self.cursor.execute(sql_select_polozka, val_select_polozka)
            polozka_id = self.cursor.fetchone()[0]

            sql_insert_polozka_v_objednavce = "INSERT INTO polozka_v_objednavce (objednavka_id, polozka_id, ks_polozek) VALUES (%s, %s, %s)"
            val_insert_polozka_v_objednavce = (objednavka_id, polozka_id, pocet_ks)
            self.cursor.execute(sql_insert_polozka_v_objednavce, val_insert_polozka_v_objednavce)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print("Došlo k chybě při vkládání nové položky do objednávky:", e)
            print("Zkontrolujte prosím zda vstupní data jsou správně napsaný")

    def findAll(self):
        """
        Metoda vypíše všechny položky v objednávkách
        """
        try:
            self.cursor.execute("select * from polozka_v_objednavce")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V objednaných položkách neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def update_pocet_ks(self, objednavka_id, nazev_polozky, novy_pocet_ks):
        """
        Metoda změní počet objednané položky ve vybrané objednávce
        :param objednavka_id: ID objednávky
        :param nazev_polozky: Název položky
        :param novy_pocet_ks: Nový počet kusů
        """
        # self.najdi_objednavky_zakaznika(jmeno, prijmeni)
        sql_update_polozka_v_objednavce = "UPDATE polozka_v_objednavce SET ks_polozek = %s WHERE objednavka_id = %s AND polozka_id IN (SELECT id FROM polozka WHERE nazev = %s)"
        val_update_polozka_v_objednavce  = (novy_pocet_ks, objednavka_id, nazev_polozky)
        try:
            self.cursor.execute(sql_update_polozka_v_objednavce, val_update_polozka_v_objednavce)
            if self.cursor.rowcount == 0:
                print(f"Položka {nazev_polozky} v objednávce s ID {objednavka_id} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit položku {nazev_polozky} v objednávce s ID {objednavka_id}.")

    def delete(self, objednavka_id, nazev_polozky):
        """
        Metoda odebere vybrané zboží z objednávky
        :param objednavka_id: ID objednávky
        :param nazev_polozky: Název položky
        """
        # self.najdi_objednavky_zakaznika(jmeno, prijmeni)
        global item_in_order_id
        sql_select_polozka_v_objednavce = "SELECT id FROM polozka_v_objednavce WHERE objednavka_id = %s AND polozka_id IN (SELECT id FROM polozka WHERE nazev = %s)"
        val_select_polozka_v_objednavce = (objednavka_id, nazev_polozky)
        try:
            self.cursor.execute(sql_select_polozka_v_objednavce, val_select_polozka_v_objednavce)
            vysledek = self.cursor.fetchall()
            (item_in_order_id,) = vysledek[0]
            if not vysledek:
                print(f"Položka {nazev_polozky} v objednávce s ID {objednavka_id} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání položky v objednávce:", err)

        sql_delete_polozka_v_objednavce = "DELETE FROM polozka_v_objednavce WHERE id = %s"
        val_delete_polozka_v_objednavce = (item_in_order_id,)
        try:
            self.cursor.execute(sql_delete_polozka_v_objednavce, val_delete_polozka_v_objednavce)
            if self.cursor.rowcount == 0:
                print(f"Položka {nazev_polozky} v objednávce s ID {objednavka_id} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se smazat položku {nazev_polozky} v objednávce s ID {objednavka_id}.")



