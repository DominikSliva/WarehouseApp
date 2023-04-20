import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.lokace_ulozeni import LokaceUlozeni


class LokaceUlozeniController:
    def __init__(self):
        self.lokace_ulozeni_model = LokaceUlozeni()
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
            logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
            now = datetime.now()
            self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce lokace ulozeni: {err}")

    def pridat_lokaci_ulozeni(self):
        """
        Metoda kontroluje vstupy a volá metodu pro vytvoření nové lokace umístění položky
        """
        try:
            lokace = input("Zadejte název lokace: ")
            if lokace.isspace():
                raise ValueError("Název lokace nemůže být prázdný")
            kapacita = input("Zadejte kapacitu lokace: ")
            if kapacita.isspace():
                raise ValueError("Kapacita lokace nemůže být prázdná")
            if kapacita <= 0:
                raise ValueError("Kapacita musí být větší jak 1")
            if not kapacita.isnumeric():
                raise ValueError("Kapacita lokace musí být číslo.")
            self.lokace_ulozeni_model.add(lokace, kapacita)
            logging.info(f"{self.current_time}Vytvoření nového lokace uložení")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při vytváření nové lokace uložení došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při vytváření nové lokace uložení došlo k chybě: {err}")

    def zobrazit_lokace_ulozeni(self):
        self.lokace_ulozeni_model.findAll()

    def zobrazit_lokace_ulozeni_podle_nazvu(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení lokace uložení pro vybraný název
        """
        try:
            lokace = input("Zadejte název lokace: ")
            self.lokace_ulozeni_model.findByLokace(lokace)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_lokace_ulozeni_podle_kapacity(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení lokace uložení podle kapacity
        """
        try:
            kapacita = input("Zadejte kapacitu lokace: ")
            if not kapacita.isnumeric():
                raise ValueError("Kapacita lokace musí být číslo.")

            self.lokace_ulozeni_model.findByKapacita(kapacita)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def upravit_nazev_lokace(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení názvu lokace
        """
        try:
            stara_lokace = input("Zadejte název lokace, u které chcete upravit název: ")
            nova_lokace = input("Zadejte nový název lokace: ")
            self.lokace_ulozeni_model.updateLokace(stara_lokace, nova_lokace)
            logging.info(f"{self.current_time}Upravení názvu lokace uložení")
        except Exception as err:
            print(f"Nepodařilo se upravit nazev lokace uložení: {err}")
            logging.error(f"{self.current_time}Při upravování názvu lokace uložení došlo k chybě: {err}")

    def upravit_kapacitu_lokace(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení kapacity lokace
        """
        try:
            lokace = input("Zadejte název lokace, u které chcete upravit kapacitu: ")
            kapacita = input("Zadejte novou kapacitu lokace: ")
            if not kapacita.isnumeric():
                raise ValueError("Kapacita lokace musí být číslo.")
            self.lokace_ulozeni_model.updateKapacita(lokace, kapacita)
            logging.info(f"{self.current_time}Upravení názvu kapacity lokace uložení")
        except Exception as err:
            print(f"Nepodařilo se upravit kapacitu lokace uložení: {err}")
            logging.error(f"{self.current_time}Při upravování kapacity lokace uložení došlo k chybě: {err}")

    def smazat_lokaci(self):
        """
        Metoda kontroluje vstupy a volá metodu pro smazání lokace
        """
        try:
            lokace = input("Zadejte název lokace, kterou chcete smazat: ")
            self.lokace_ulozeni_model.delete(lokace)
            logging.info(f"{self.current_time}Smazání kapacity lokace")
        except Exception as err:
            print(f"Nepodařilo se smazat lokaci uložení: {err}")
            logging.error(f"{self.current_time}Při smazání lokace uložení došlo k chybě: {err}")


