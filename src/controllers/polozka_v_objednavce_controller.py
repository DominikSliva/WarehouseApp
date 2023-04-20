import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.objednavka import Objednavka
from src.entity.polozka_v_objednavce import PolozkaVObjednavce


class PolozkaVObjednavceController:
    def __init__(self):
        self.polozka_v_objednavce_model = PolozkaVObjednavce()
        self.objednavka_model = Objednavka()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce polozka_v_objednavce: {err}")

    def pridat_polozku_do_objednavky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro přidání položky do objednávky
        """
        try:
            jmeno = input("Zadejte jméno zákazníka, pro vyhledání objednávek: ")
            if jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")
            prijmeni = input("Zadejte příjmení zákazníka, pro vyhledání objednávek: ")
            if not self.objednavka_model.findObjednavkyByZakaznik(jmeno, prijmeni):
                return
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            objednavka_id = input("Zadejte ID objednávky, do které budete chtít přidat položku: ")
            if not objednavka_id.isnumeric():
                raise ValueError("ID objednávky musí být číslo")
            if objednavka_id.isspace():
                raise ValueError("ID objednávky nemůže být prázdné")

            nazev_polozky = input("Zadejte název položky: ")
            if nazev_polozky.isnumeric():
                raise ValueError("Název položky nemůže být číslo")
            if nazev_polozky.isspace():
                raise ValueError("Název položky nemůže být prázdný")

            pocet_ks = input("Zadejte počet kusů položky: ")
            if not pocet_ks.isnumeric() or int(pocet_ks) <= 0:
                raise ValueError("Počet kusů musí být kladné celé číslo větší jak nula.")
            if pocet_ks.isspace():
                raise ValueError("Počet kusů položky nemůže být prázdný")
            self.polozka_v_objednavce_model.add(objednavka_id, nazev_polozky, pocet_ks)
            logging.info(f"{self.current_time}Přidání nové položky do objednávky")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při přidávání nové položky do objednávky došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při přidávání nové položky do objednávky došlo k chybě: {err}")

    def zobrazit_polozky_v_objednavce(self):
        self.polozka_v_objednavce_model.findAll()

    def upravit_pocet_ks_polozky_v_objednavce(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení počtu kusů položky v objednávce
        """
        try:
            jmeno = input("Zadejte jméno zákazníka, pro vyhledání objednávek: ")
            prijmeni = input("Zadejte příjmení zákazníka, pro vyhledání objednávek: ")
            if not self.objednavka_model.findObjednavkyByZakaznik(jmeno, prijmeni):
                return

            objednavka_id = input("Zadejte ID objednávky, do které budete chtít přidat položku: ")
            if not objednavka_id.isnumeric():
                raise ValueError("ID objednávky musí být číslo")

            nazev_polozky = input("Zadejte název položky: ")
            if nazev_polozky.isnumeric():
                raise ValueError("Název položky nemůže být číslo")

            novy_pocet_ks = input("Zadejte nový počet kusů položky: ")
            if not novy_pocet_ks.isnumeric() or int(novy_pocet_ks) <= 0:
                raise ValueError("Počet kusů musí být kladné celé číslo větší jak nula.")
            self.polozka_v_objednavce_model.add(objednavka_id, nazev_polozky, novy_pocet_ks)
            logging.info(f"{self.current_time}Upravení počtu kusů položky v objednávce")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování počtu kusů položky v objednávce došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při upravování počtu kusů položky v objednávce došlo k chybě: {err}")

    def smazani_polozky_z_objednavky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro smazaní položky v objednávce
        """
        try:
            jmeno = input("Zadejte jméno zákazníka, pro vyhledání objednávek: ")
            prijmeni = input("Zadejte příjmení zákazníka, pro vyhledání objednávek: ")
            if not self.objednavka_model.findObjednavkyByZakaznik(jmeno, prijmeni):
                return

            objednavka_id = input("Zadejte ID objednávky, do které budete chtít přidat položku: ")
            if not objednavka_id.isnumeric():
                raise ValueError("ID objednávky musí být číslo")

            nazev_polozky = input("Zadejte název položky, kterou chcete odstranit z objednávky: ")
            if nazev_polozky.isnumeric():
                raise ValueError("Název položky nemůže být číslo")
            self.polozka_v_objednavce_model.delete(objednavka_id, nazev_polozky)
            logging.info(f"{self.current_time}Smazání položky z objednávky")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při smazání položky z objednávky došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při smazání položky z objednávky došlo k chybě: {err}")



