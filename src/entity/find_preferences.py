from src.db.connection import DatabaseConnector


class FindPreferences:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def pohled_historie_pohybu_polozky_(self):
        """
        Metoda vypíše pohled pro historii pohybu polozek
        """
        try:
            self.cursor.execute("select * from historie_pohybu_polozky_view")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V pohledu pro historii pohybu položek neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def pohled_na_zasoby(self):
        """
        Metoda vypíše pohled pro zásoby
        """
        try:
            self.cursor.execute("select * from pohled_na_zasoby")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V pohledu pro zásoby neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def pohled_polozky_a_lokace(self):
        """
        Metoda vypíše pohled pro položky a jejich lokace
        """
        try:
            self.cursor.execute("select * from polozky_a_lokace")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V pohledu pro položky a jejich lokace neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def pohled_expedovatelnost_objednávek(self):
        """
        Metoda vypíše pohled pro expedovatelnost objednávek
        """
        try:
            self.cursor.execute("select * from vsechny_objednavky")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V pohledu pro expedovatelnost objednávek neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")
