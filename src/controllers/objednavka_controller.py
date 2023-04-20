import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.objednavka import Objednavka
import re

class ObjednavkaController:
    def __init__(self):
        self.objednavka_model = Objednavka()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce objednavka: {err}")

    def pridat_objednavku_s_momentálním_datumem(self):
        """
        Metoda kontroluje vstupy a volá metodu pro vytvoření nové objednávky s momentálním datumem
        """

        jmeno_zakaznika = input("Pro vytvoření objednávky zadejte prosím jméno zákazníka: ")
        if jmeno_zakaznika.isnumeric():
            raise ValueError("Jméno zákazníka nemůže být číslo")
        if jmeno_zakaznika.isspace():
            raise ValueError("Jméno zákazníka nemůže být prázdné")
        prijmeni_zakaznika = input("Pro vytvoření objednávky zadejte prosím příjmení zákazníka: ")
        if prijmeni_zakaznika.isnumeric():
            raise ValueError("Příjmení zákazníka nemůže být číslo")
        if prijmeni_zakaznika.isspace():
            raise ValueError("Příjmení zákazníka nemůže být prázdné")
        self.objednavka_model.addDateNow(jmeno_zakaznika, prijmeni_zakaznika)
        logging.info(f"{self.current_time}Vytvoření nové objednávky s momentálním datem")

    def pridat_objednavku_s_jakymkoliv_datem(self):
        """
        Metoda kontroluje vstupy a volá metodu pro vytvoření nové objednávky s vybraným datumem
        """
        try:
            jmeno_zakaznika = input("Pro vytvoření objednávky zadejte jméno zákazníka: ")
            prijmeni_zakaznika = input("Pro vytvoření objednávky zadejte příjmení zákazníka: ")
            datum = input("Zadejte datum vytvoření objednávky (YYYY-MM-DD): ")

            if not re.match("^\d{4}-\d{2}-\d{2}$", datum):
                raise ValueError("Datum musí být ve formátu YYYY-MM-DD a obsahovat pouze čísla.")

            self.objednavka_model.addAnyDate(jmeno_zakaznika, prijmeni_zakaznika, datum)
            logging.info(f"{self.current_time}Vytvoření nové objednávky se zvoleným datem")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při vytváření nové objednávky došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při vytváření nové objednávky došlo k chybě: {err}")

    def zobrazit_objednavky(self):
        self.objednavka_model.findAll()

    def zobrazit_objednavky_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení objednávek vybraného zákazníka
        """
        try:
            jmeno = input("Zadejte jméno zákazníka: ")
            prijmeni = input("Zadejte příjmení zákazníka: ")

            if jmeno.isnumeric():
                raise ValueError("Jméno zákazníka nemůže být číslo")
            if prijmeni.isnumeric():
                raise ValueError("Příjmení zákazníka nemůže být číslo")

            self.objednavka_model.findObjednavkyByZakaznik(jmeno, prijmeni)
        except ValueError as err:
            print("Chyba: ", err)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_neexpedovane_objednavky(self):
        self.objednavka_model.findByNeexpedovano()

    def zobrazit_expedovane_objednavky(self):
        self.objednavka_model.findByExpedovano()

    def zobrazit_podle_data_objednavky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení objednávek podle vybraného data
        """
        try:
            datum = input("Zadejte datum objednávky (YYYY-MM-DD): ")

            if not re.match("^\d{4}-\d{2}-\d{2}$", datum):
                raise ValueError("Datum musí být ve formátu YYYY-MM-DD a obsahovat pouze čísla.")

            self.objednavka_model.findByDatum(datum)

        except ValueError as err:
            print("Chyba: ", err)
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)

    def upravit_objednavku_na_expedovanou(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení stavu objednávky na expedovanou
        """
        try:
            jmeno = input("Zadejte jméno zákazníka, pro vyhledání objednávek: ")
            prijmeni = input("Zadejte příjmení zákazníka, pro vyhledání objednávek: ")
            self.objednavka_model.findObjednavkyByZakaznik(jmeno, prijmeni)

            id_objednavky = input("Zadejte id objednávky, kterou bude chtít upravit expedovanou objednávku: ")
            if not id_objednavky.isnumeric():
                raise ValueError("ID objednávky musí být číslo")

            self.objednavka_model.updateNaExpedovano(jmeno, prijmeni, id_objednavky)
            logging.info(f"{self.current_time}Upravování objednávky na stav expedováno")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování objednávky na stav expedováno došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při upravování objednávky na stav expedováno došlo k chybě: {err}")

    def upravit_objednavku_na_neexpedovanou(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení stavu objednávky na neexpedovanou
        """
        try:
            jmeno = input("Zadejte jméno zákazníka, pro vyhledání objednávek: ")
            prijmeni = input("Zadejte příjmení zákazníka, pro vyhledání objednávek: ")
            self.objednavka_model.findObjednavkyByZakaznik(jmeno, prijmeni)

            id_objednavky = input("Zadejte id objednávky, kterou bude chtít upravit na neexpedovanou objednávku: ")
            if not id_objednavky.isnumeric():
                raise ValueError("ID objednávky musí být číslo")

            self.objednavka_model.updateNaNeexpedovano(jmeno, prijmeni, id_objednavky)
            logging.info(f"{self.current_time}Upravování objednávky na stav neexpedováno")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování objednávky na stav neexpedováno došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při upravování objednávky na stav neexpedováno došlo k chybě: {err}")

    def smazat_objednavky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro smazání objednávky
        """
        try:
            jmeno = input("Zadejte jméno zákazníka, pro vyhledání objednávek: ")
            prijmeni = input("Zadejte příjmení zákazníka, pro vyhledání objednávek: ")
            self.objednavka_model.findObjednavkyByZakaznik(jmeno, prijmeni)

            id_objednavky = input("Zadejte id objednávky, kterou bude chtít smazat: ")
            if not id_objednavky.isnumeric():
                raise ValueError("ID objednávky musí být číslo")

            self.objednavka_model.delete(jmeno, prijmeni, id_objednavky)
            logging.info(f"{self.current_time}Smazání objednávky")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při smazání objednávky došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při smazání objednávky došlo k chybě: {err}")

