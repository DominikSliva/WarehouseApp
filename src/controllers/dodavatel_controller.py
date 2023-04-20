import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.dodavatel import Dodavatel
import re

class DodavatelController:
    def __init__(self):
        self.dodavatel_model = Dodavatel()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce dodavatel: {err}")

    def pridat_dodavatele(self):
        """
        Metoda kontroluje vstupy a volá metodu pro přidání nového dodavatele
        """
        try:
            nazev = input("Zadejte název dodavatele: ")
            if nazev.isnumeric():
                raise ValueError("Název dodavatele nemůže být číslo.")
            if nazev.isspace():
                raise ValueError("Název dodavatele nemůže být prázdný")

            adresa = input("Zadejte adresu dodavatele: ")
            if adresa.isspace():
                raise ValueError("Adresa dodavatele nemůže být prázdná")

            telefon = input("Zadejte telefonní číslo dodavatele: ")
            if not re.match("^[0-9]{3}-[0-9]{3}-[0-9]{3}$", telefon):
                raise ValueError("Telefonní číslo musí být ve formátu ###-###-### a obsahovat pouze čísla.")
            if telefon.isspace():
                raise ValueError("Telefonní číslo dodavatele nesmí být prázdné")
            self.dodavatel_model.add(nazev, adresa, telefon)
            logging.info(f"{self.current_time}Vytvoření nového dodavatele")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při vytváření nového dodavatele došlo k chybě: {err}")
        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při vytváření nového dodavatele došlo k chybě: {err}")

    def zobrazit_dodavatele(self):
        self.dodavatel_model.findAll()

    def zobrazit_dodavatele_podle_nazvu(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení dodavatele podle nazvu
        """
        try:
            nazev = input("Zadejte název dodavatele: ")
            self.dodavatel_model.findByName(nazev)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_dodavatele_podle_adresy(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení dodavatele podle adresy
        """
        try:
            adresa = input("Zadejte adresu dodavatele: ")
            self.dodavatel_model.findByAdress(adresa)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_dodavatele_podle_telefonniho_cisla(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení dodavatele podle telefonu
        """
        try:
            telefon = input("Zadejte telefonní číslo dodavatele: ")
            if not telefon.isnumeric():
                raise ValueError("Telefonní číslo dodavatele musí být číslo.")
            self.dodavatel_model.findByPhone(telefon)
        except Exception as e:
            print("Chyba: ", e)

    def upravit_nazev_dodavatele(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení nazvu dodavatele
        """
        try:
            stary_nazev = input("Zadejte název dodavatele, u které chcete upravit název: ")
            novy_nazev = input("Zadejte nový název dodavatele: ")
            if novy_nazev.isnumeric():
                raise ValueError("Název dodavatele nemůže být číslo.")
            self.dodavatel_model.updateName(stary_nazev, novy_nazev)
            logging.info(f"{self.current_time}Upravení názvu dodavatele")
        except Exception as err:
            print(f"Nepodařilo se upravit nazev dodavatele: {err}")
            logging.error(f"{self.current_time}Při upravování názvu dodavatele došlo k chybě: {err}")

    def upravit_adresu_dodavatele(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení adresy dodavatele
        """
        try:
            nazev = input("Zadejte název dodavatele, u které chcete upravit adresu: ")
            adresa = input("Zadejte novou adresu dodavatele: ")
            self.dodavatel_model.updateAdress(nazev, adresa)
            logging.info(f"{self.current_time}Upravení adresy dodavatele")
        except Exception as err:
            print(f"Nepodařilo se upravit adresu dodavatele: {err}")
            logging.error(f"{self.current_time}Při upravování adresy dodavatele došlo k chybě: {err}")


    def upravit_telefonni_cislo_dodavatele(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení telefonu dodavatele
        """
        try:
            nazev = input("Zadejte název dodavatele, u které chcete upravit telefonní číslo: ")
            telefon = input("Zadejte nové telefonní číslo dodavatele: ")
            if not re.match("^[0-9]{3}-[0-9]{3}-[0-9]{3}$", telefon):
                raise ValueError("Telefon musí být ve formátu ###-###-### a obsahovat pouze čísla.")
            self.dodavatel_model.updatePhone(nazev, telefon)
            logging.info(f"{self.current_time}Upravení telefonu dodavatele")
        except Exception as err:
            print(f"Nepodařilo se upravit telefonní číslo dodavatele: {err}")
            logging.error(f"{self.current_time}Při upravování telefonu dodavatele došlo k chybě: {err}")

    def smazat_dodavatele(self):
        """
        Metoda kontroluje vstupy a volá metodu pro smazání dodavatele
        """
        try:
            nazev = input("Zadejte název dodavatele, kterého chcete smazat: ")
            self.dodavatel_model.delete(nazev)
            logging.info(f"{self.current_time}Smazání dodavatele")
        except Exception as err:
            print(f"Nepodařilo se smazat dodavatele: {err}")
            logging.error(f"{self.current_time}Při odstraňování dodavatele došlo k chybě: {err}")

