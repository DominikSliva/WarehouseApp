from src.db.connection import DatabaseConnector


class HistoriePohybuPolozky:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def findAll(self):
        """
        Metoda vypíše celou historii pohybu položek
        """
        try:
            self.cursor.execute("select p.nazev, h.datum as polozka, l1.lokace as puvodni_lokace, l2.lokace as nova_lokace "
                                "from historie_pohybu_polozky h join polozka p on h.polozka_id = p.id join lokace_ulozeni l1 "
                                "on h.puvodni_lokace_id = l1.id join lokace_ulozeni l2 on h.nova_lokace_id = l2.id order by h.datum desc")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"V historii pohybu položek neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def findByPuvodniLokace(self, nazev_puvodni_lokace):
        """
        Metoda vypíše všechny změny lokací s vybraným názvem původní lokace
        :param nazev_puvodni_lokace: Název původní lokace
        """
        sql_select_historie = "select historie_pohybu_polozky.id, historie_pohybu_polozky.datum, polozka.nazev, " \
                              "puvodni_lokace.lokace as puvodni_lokace, nova_lokace.lokace as nova_lokace from " \
                              "historie_pohybu_polozky historie_pohybu_polozky join polozka polozka on polozka.id = " \
                              "historie_pohybu_polozky.polozka_id join lokace_ulozeni puvodni_lokace on puvodni_lokace.id = " \
                              "historie_pohybu_polozky.puvodni_lokace_id join lokace_ulozeni nova_lokace on nova_lokace.id = " \
                              "historie_pohybu_polozky.nova_lokace_id where puvodni_lokace.id = (select id from lokace_ulozeni " \
                              "where lokace = %s)"
        val_select_historie = (nazev_puvodni_lokace,)
        try:
            self.cursor.execute(sql_select_historie, val_select_historie)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"V historii pohybu položek s původním názvem lokace {nazev_puvodni_lokace} neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání historie pohybu položky:", err)

    def findByNoveLokace(self, nazev_nove_lokace):
        """
        Metoda vypíše všechny změny lokací s vybraným názvem nově přidané lokace
        :param nazev_nove_lokace: Název nově přidané lokace
        """
        sql_select_historie = "select h.id, h.datum, p.nazev as polozka, l1.lokace as stara_lokace, l2.lokace AS nova_lokace " \
                              "from historie_pohybu_polozky h join polozka p on h.polozka_id = p.id join lokace_ulozeni l1 on" \
                              " h.puvodni_lokace_id = l1.id join lokace_ulozeni l2 on h.nova_lokace_id = l2.id where l2.lokace = %s"
        val_select_historie = (nazev_nove_lokace,)
        try:
            self.cursor.execute(sql_select_historie, val_select_historie)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"V historii pohybu položek s novým názvem lokace {nazev_nove_lokace} neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání historie pohybu položky:", err)

    def findByPolozkaOdNejnovejsiho(self, nazev_polozky):
        """
        Metoda vypíše celou historii pohybu pro vybranou položku seřazenou od nejnovejší změny
        :param nazev_polozky: Název položky
        """
        sql_select_historie = "select h.datum, l1.lokace AS puvodni_lokace, l2.lokace as nova_lokace from historie_pohybu_polozky " \
                              "h join polozka p on h.polozka_id = p.id join lokace_ulozeni l1 on h.puvodni_lokace_id = l1.id join " \
                              "lokace_ulozeni l2 on h.nova_lokace_id = l2.id where p.nazev = %s order by h.datum desc"
        val_select_historie = (nazev_polozky,)
        try:
            self.cursor.execute(sql_select_historie, val_select_historie)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"V historii pohybu položek s názvem položky {nazev_polozky} neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání historie pohybu položky:", err)

    def findByPolozkaOdNejstarsiho(self, nazev_polozky):
        """
        Metoda vypíše celou historii pohybu pro vybranou položku seřazenou od nejstarší změny
        :param nazev_polozky: Název položky
        """
        sql_select_historie = "select h.datum, l1.lokace AS puvodni_lokace, l2.lokace as nova_lokace from historie_pohybu_polozky " \
                              "h join polozka p on h.polozka_id = p.id join lokace_ulozeni l1 on h.puvodni_lokace_id = l1.id join " \
                              "lokace_ulozeni l2 on h.nova_lokace_id = l2.id where p.nazev = %s"
        val_select_historie = (nazev_polozky,)
        try:
            self.cursor.execute(sql_select_historie, val_select_historie)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"V historii pohybu položek s názvem položky {nazev_polozky} neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání historie pohybu položky:", err)

