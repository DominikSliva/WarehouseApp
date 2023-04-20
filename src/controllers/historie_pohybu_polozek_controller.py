import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.historie_pohybu_polozky import HistoriePohybuPolozky


class HistoriePohybuPolozkyController:
    def __init__(self):
        self.historie_pohybu_polozek_model = HistoriePohybuPolozky()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce historie pohybu polozek: {err}")

    def zobrazit_historii_pohybu_polozek(self):
        self.historie_pohybu_polozek_model.findAll()

    def zobrazit_historii_pohybu_polozek_podle_puvodni_lokace(self):
        """
        Metoda kontroluje vstup a volá metodu pro zobrazení historie pohybu polozek podle puvodní lokace
        """
        try:
            nazev_puvodni_lokace = input("Zadejte název původní lokace: ")
            self.historie_pohybu_polozek_model.findByPuvodniLokace(nazev_puvodni_lokace)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_historii_pohybu_polozek_podle_nove_lokace(self):
        """
        Metoda kontroluje vstup a volá metodu pro zobrazení historie pohybu polozek podle nové lokace
        """
        try:
            nazev_nove_lokace = input("Zadejte název nové lokace: ")
            self.historie_pohybu_polozek_model.findByNoveLokace(nazev_nove_lokace)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_historii_pohybu_polozky_od_nejnovejsiho(self):
        """
        Metoda kontroluje vstup a volá metodu pro zobrazení historie pohybu vybrané položky od nejnovějších záznamů
        """
        try:
            nazev_polozky = input("Zadejte název položky: ")
            self.historie_pohybu_polozek_model.findByPolozkaOdNejnovejsiho(nazev_polozky)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_historii_pohybu_polozky_od_nejstarsiho(self):
        """
        Metoda kontroluje vstup a volá metodu pro zobrazení historie pohybu vybrané položky od nejstarších záznamů
        """
        try:
            nazev_polozky = input("Zadejte název položky: ")
            self.historie_pohybu_polozek_model.findByPolozkaOdNejstarsiho(nazev_polozky)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

