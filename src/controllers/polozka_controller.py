import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.polozka import Polozka


class PolozkaController:
    def __init__(self):
        self.polozka_model = Polozka()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce polozka: {err}")

    def pridat_polozku(self):
        """
        Metoda kontroluje vstupy a volá metodu pro vytvoření nové položky
        """
        try:
            nazev = input("Zadejte název položky: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")
            if nazev.isspace():
                raise ValueError("Název položky nemůže být prázdný")

            cena = input("Zadejte cenu položky: ")
            if not cena.isnumeric() or int(cena) < 0 or float(cena) < 0:
                raise ValueError("Cena musí být nezáporné číslo větší jak nula.")
            if cena.isspace():
                raise ValueError("Cena položky nemůže být prázdná")

            kod = input("Zadejte pětimístný kód položky: ")
            if not kod.isnumeric() or len(kod) != 5:
                raise ValueError("Kód položky musí být pětimístné číslo.")
            if kod <= 0 or kod is not int:
                raise ValueError("Kód položky musí být celé kladné číslo bez nuly")
            if kod.isspace():
                raise ValueError("Kód položky nemůže být prázdný")

            pocet_ks = input("Zadejte počet kusů položky: ")
            if not pocet_ks.isnumeric() or int(pocet_ks) <= 0:
                raise ValueError("Počet kusů musí být kladné celé číslo větší jak nula.")
            if pocet_ks.isspace():
                raise ValueError("Počet kusů nemůže být prázdný")

            lokace = input("Zadejte název lokace kde položka je uložená: ")
            if lokace.isspace():
                raise ValueError("Lokace nemůže být prázdná")

            dodavatel_nazev = input("Zadejte název dodavatele položky: ")
            if dodavatel_nazev.isnumeric():
                raise ValueError("Název dodavatele nemůže být číslo.")
            if dodavatel_nazev.isspace():
                raise ValueError("Název dodavatele nemůže být prázdný")

            kategorie_nazev = input("Zadejte název kategorie položky: ")
            if kategorie_nazev.isnumeric():
                raise ValueError("Název kategorie nemůže být číslo.")
            if kategorie_nazev.isspace():
                raise ValueError("Název kategorie nemůže být prázdný")

            self.polozka_model.add(nazev, cena, kod, pocet_ks, lokace, dodavatel_nazev, kategorie_nazev)
            logging.info(f"{self.current_time}Vytvoření nové položky")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při vytváření nové položky došlo k chybě: {err}")

        except Exception as err:
            print("Došlo k neznámé chybě: ", err)
            logging.error(f"{self.current_time}Při vytváření nové položky došlo k chybě: {err}")

    def zobrazit_polozky(self):
        self.polozka_model.findAll()

    def zobrazit_polozku_podle_ceny(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení položky podle ceny
        """
        try:
            cena = input("Zadejte cenu položky: ")
            self.polozka_model.findByCena(cena)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_polozku_podle_kodu(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení položky podle kódu
        """
        try:
            kod = input("Zadejte kód položky: ")
            if not kod.isnumeric() or len(kod) != 5:
                raise ValueError("Kód položky musí být pětimístné číslo.")
            self.polozka_model.findByCena(kod)

        except ValueError as err:
            print("Chyba: ", err)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_polozku_podle_poctu_ks(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení položky podle počtu kusů
        """
        try:
            pocet_ks = input("Zadejte počet kusů položky: ")
            if not pocet_ks.isnumeric() or int(pocet_ks) < 0:
                raise ValueError("Počet kusů musí být kladné celé číslo.")
            self.polozka_model.findByPocetKs(pocet_ks)

        except ValueError as err:
            print("Chyba: ", err)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_polozku_podle_lokace_ulozeni(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení položky podle lokace uložení
        """
        try:
            lokace = input("Zadejte název lokace uložení položky: ")
            self.polozka_model.findByLokaceUlozeni(lokace)

        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_polozku_podle_dodavatele(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení položky podle dodavatele
        """
        try:
            dodavatel = input("Zadejte název dodavatele položky: ")
            if dodavatel.isnumeric():
                raise ValueError("Název dodavatele nemůže být číslo.")
            self.polozka_model.findByDodavatel(dodavatel)
        except ValueError as err:
            print("Chyba: ", err)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def zobrazit_polozku_podle_kategorie(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení položky podle kategorie
        """
        try:
            kategorie = input("Zadejte název kategorie položky: ")
            if kategorie.isnumeric():
                raise ValueError("Název kategorie nemůže být číslo.")
            self.polozka_model.findByKategorie(kategorie)
        except ValueError as err:
            print("Chyba: ", err)
        except Exception as e:
            print("Došlo k neznámé chybě: ", e)

    def upravit_cenu_polozky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení ceny položky
        """
        try:
            nazev = input("Zadejte název položky, u které chcete upravit cenu: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")

            nova_cena = input("Zadejte novou cenu položky: ")
            if not nova_cena.isnumeric() or int(nova_cena) < 0 or float(nova_cena) < 0:
                raise ValueError("Cena musí být nezáporné číslo větší jak nula.")

            self.polozka_model.updateCena(nazev, nova_cena)
            logging.info(f"{self.current_time}Upravení ceny položky")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")
        except Exception as err:
            print("Chyba", err, "Zkontrolujte prosím zda se položka nachází v databázi.")
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")

    def upravit_kod_polozky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení kódu položky
        """
        try:
            nazev = input("Zadejte název položky, u které chcete upravit kód: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")
            kod = input("Zadejte nový kód položky: ")
            if not kod.isnumeric() or len(kod) != 5:
                raise ValueError("Kód položky musí být pětimístné číslo.")
            self.polozka_model.updateKod(nazev, kod)
            logging.info(f"{self.current_time}Upravení kódu položky")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err, "Zkontrolujte prosím zda vstupní data jsou validní a kód položky je unikátní")
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")

    def upravit_pocet_ks_polozky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení počtu kusů položky
        """
        try:
            nazev = input("Zadejte název položky, u které chcete upravit počet kusů: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")

            novy_pocet_ks = input("Zadejte nový počet kusů položky: ")
            if not novy_pocet_ks.isnumeric():
                raise ValueError("Počet kusů musí být kladné celé číslo.")

            self.polozka_model.updatePocetKs(nazev, novy_pocet_ks)
            logging.info(f"{self.current_time}Upravení počtu ks položky")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err, "Zkontrolujte prosím zda se položka nachází v databázi.")
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")

    def upravit_lokaci_polozky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení lokace umístění položky
        """
        try:
            nazev = input("Zadejte název položky, u které chcete upravit lokaci uložení: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")
            nova_lokace = input("Zadejte nový název lokace: ")

            self.polozka_model.updateLokace(nazev, nova_lokace)
            logging.info(f"{self.current_time}Upravení lokace umístění položky")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err, "Zkontrolujte prosím zda se položka a název lokace nachází v databázi.")
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")

    def upravit_dodavatele_polozky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení dodavatele položky
        """
        try:
            nazev = input("Zadejte název položky, u které chcete upravit dodavatele: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")

            dodavatel_nazev = input("Zadejte název nového dodavatele položky: ")
            if dodavatel_nazev.isnumeric():
                raise ValueError("Název dodavatele nemůže být číslo.")

            self.polozka_model.updateDodavatel(nazev, dodavatel_nazev)
            logging.info(f"{self.current_time}Upravení dodavatele položky")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err, "Zkontrolujte prosím zda se položka a název dodavatele nachází v databázi.")
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")

    def upravit_kategorii_polozky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení kategorie položky
        """
        try:
            nazev = input("Zadejte název položky, u které chcete upravit kategorii: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")

            kategorie_nazev = input("Zadejte název nové kategorie položky: ")
            if kategorie_nazev.isnumeric():
                raise ValueError("Název kategorie nemůže být číslo.")

            self.polozka_model.updateKategorie(nazev, kategorie_nazev)
            logging.info(f"{self.current_time}Upravení dodavatele položky")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err, "Zkontrolujte prosím zda se položka a název kategorie nachází v databázi")
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")

    def smazani_polozky(self):
        """
        Metoda kontroluje vstupy a volá metodu pro smazání položky
        """
        try:
            nazev = input("Zadejte název položky, u které chcete upravit kategorii: ")
            if nazev.isnumeric():
                raise ValueError("Název položky nemůže být číslo.")
            self.polozka_model.delete(nazev)
            logging.info(f"{self.current_time}Smazání položky")
        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")
        except Exception as err:
            print(f"Nepodařilo se smazat položku: {err}")
            logging.error(f"{self.current_time}Při upravování položky došlo k chybě: {err}")


