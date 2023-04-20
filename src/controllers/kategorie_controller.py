import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.kategorie import Kategorie


class KategorieController:
    def __init__(self):
        self.kategorie_model = Kategorie()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce kategorie: {err}")

    def pridat_kategorii(self):
        """
        Metoda kontroluje vstupy a volá metodu pro přidání nové kategorie
        """
        try:
            nazev = input("Zadejte název kategorie: ")
            if nazev.isnumeric():
                raise ValueError("Název kategorie nemůže být číslo.")
            if nazev.isspace():
                raise ValueError("Název kategorie nemůže být prázdný")

            popis = input("Zadejte popis kategorie: ")
            if popis.isspace():
                raise ValueError("Popis kategorie nemůže být prázdný")
            self.kategorie_model.add(nazev, popis)
            logging.info(f"{self.current_time}Vytvoření nové kategorie")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při vytváření nové kategorie došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při vytváření nové kategorie došlo k chybě: {err}")

    def zobrazit_kategorie(self):
        self.kategorie_model.findAll()

    def upravit_popis_kategorie(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení popisu kategorie
        """
        try:
            nazev = input("Zadejte název kategorie, u které chcete upravit popis: ")
            novy_popis = input("Zadejte nový popis: ")
            self.kategorie_model.updatePopis(nazev, novy_popis)
            logging.info(f"{self.current_time}Upravení popisu kategorie")
        except Exception as err:
            print(f"Nepodařilo se upravit popis kategorie: {err}")
            logging.error(f"{self.current_time}Při upravování popisu kategorie došlo k chybě: {err}")


    def smazat_kategorii(self):
        """
        Metoda kontroluje vstupy a volá metodu pro smazání kategorie
        """
        try:
            nazev = input("Zadejte název kategorie, kterou chcete smazat: ")
            self.kategorie_model.delete(nazev)
            logging.info(f"{self.current_time}Smazání kategorie")

        except Exception as err:
            print(f"Nepodařilo se smazat kategorii: {err}")
            logging.error(f"{self.current_time}Při odstraňování kategorie došlo k chybě: {err}")


