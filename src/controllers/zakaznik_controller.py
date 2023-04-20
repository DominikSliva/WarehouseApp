import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.entity.zakaznik import Zakaznik
import re

class ZakaznikController:
    def __init__(self):
        self.zakaznik_model = Zakaznik()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce zakaznik: {err}")

    def pridat_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro vytvoření zákazníka
        """
        try:
            jmeno = input("Zadejte křestní jméno zákazníka: ")
            if jmeno.isnumeric() or jmeno.isspace():
                raise ValueError("Jméno zákazníka nemůže být číslo a ani být prázdné.")
            if jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")

            prijmeni = input("Zadejte příjmení zákazníka: ")
            if prijmeni.isnumeric() or prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            email = input("Zadejte e-mail zákazníka: ")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise ValueError("Zadaný e-mail není platný.")
            if jmeno.isspace():
                raise ValueError("E-mail nemůže být prázdný")

            adresa = input("Zadejte adresu zákazníka: ")
            if adresa.isspace():
                raise ValueError("Adresa nemůže být prázdná")

            telefon = input("Zadejte telefonní číslo zákazníka (formát: ###-###-###): ")
            if not re.match("^[0-9]{3}-[0-9]{3}-[0-9]{3}$", telefon):
                raise ValueError("Telefonní číslo musí být ve formátu ###-###-### a obsahovat pouze čísla.")
            if telefon.isspace():
                raise ValueError("Telefonní číslo nemůže být prázdné")
            self.zakaznik_model.add(jmeno, prijmeni, email, adresa, telefon)
            logging.info(f"{self.current_time}Vytvoření nového zákazníka")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při vytváření nového zákazníka došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při vytváření nového zákazníka došlo k chybě: {err}")

    def zobrazit_zakaznika(self):
        self.zakaznik_model.findAll()

    def zobrazit_zakaznika_podle_jmena(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení zákazníka podle jména
        """
        try:
            jmeno = input("Zadejte křestní jméno zákazníka: ")
            if jmeno.isnumeric():
                raise ValueError("Jméno nemůže být číslo")
            if jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")
            self.zakaznik_model.findByFirstName(jmeno)
        except Exception as e:
            print("Chyba: ", e)

    def zobrazit_zakaznika_podle_prijmeni(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení zákazníka podle příjmení
        """
        try:
            prijmeni = input("Zadejte příjmení zákazníka: ")
            if prijmeni.isnumeric():
                raise ValueError("Příjmení nemůže být číslo")
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")
            self.zakaznik_model.findByLastName(prijmeni)
        except Exception as e:
            print("Chyba: ", e)

    def zobrazit_zakaznika_podle_emailu(self):
        """
        Metoda kontroluje vstupy a volá metodu zobrazení zákazníka podle e-mailu
        """
        try:
            email = input("Zadejte e-mail zákazníka: ")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise ValueError("Zadaný e-mail není platný.")
            if email.isspace():
                raise ValueError("E-mail nemůže být prázdné")
            self.zakaznik_model.findByEmail(email)
        except Exception as e:
            print("Chyba: ", e)

    def zobrazit_zakaznika_podle_adresy(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení zákazníka podle adresy
        """
        try:
            adresa = input("Zadejte adresu zákazníka: ")
            if adresa.isspace():
                raise ValueError("Adresa nemůže být prázdné")
            self.zakaznik_model.findByAdress(adresa)
        except Exception as e:
            print("Chyba: ", e)

    def zobrazit_zakaznika_podle_telefonu(self):
        """
        Metoda kontroluje vstupy a volá metodu pro zobrazení zákazníka podle telefonu
        """
        try:
            telefon = input("Zadejte telefonní číslo zákazníka: ")
            if not re.match("^[0-9]{3}-[0-9]{3}-[0-9]{3}$", telefon):
                raise ValueError("Telefonní číslo musí být ve formátu ###-###-### a obsahovat pouze čísla.")
            if telefon.isspace():
                raise ValueError("Telefonní číslo nemůže být prázdné")
            self.zakaznik_model.findByPhone(telefon)
        except Exception as e:
            print("Chyba: ", e)

    def upravit_jmeno_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení jména zákazníka
        """
        try:
            stare_jmeno = input("Zadejte křestní jméno zákazníka: ")
            if stare_jmeno.isnumeric() or stare_jmeno.isspace():
                raise ValueError("Jméno zákazníka nemůže být číslo a ani být prázdné.")
            if stare_jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")

            prijmeni = input("Zadejte příjmení zákazníka: ")
            if prijmeni.isnumeric() or prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            nove_jmeno = input("Zadejte nové křestní jméno zákazníka: ")
            if nove_jmeno.isnumeric() or nove_jmeno.isspace():
                raise ValueError("Jméno zákazníka nemůže být číslo a ani být prázdné.")
            if nove_jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")

            self.zakaznik_model.updateFirstName(stare_jmeno, prijmeni, nove_jmeno)
            logging.info(f"{self.current_time}Upravení jména zákazníka")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")

    def upravit_prijmeni_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení příjmení zákazníka
        """
        try:
            stare_prijmeni = input("Zadejte příjmení zákazníka: ")
            if stare_prijmeni.isnumeric() or stare_prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if stare_prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            nove_prijmeni = input("Zadejte nové příjmení zákazníka: ")
            if nove_prijmeni.isnumeric() or nove_prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if nove_prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            self.zakaznik_model.updateLastName(stare_prijmeni, nove_prijmeni)
            logging.info(f"{self.current_time}Upravení příjmení zákazníka")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")

    def upravit_email_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení e-mailu zákazníka
        """
        try:
            jmeno = input("Zadejte křestní jméno zákazníka: ")
            if jmeno.isnumeric() or jmeno.isspace():
                raise ValueError("Jméno zákazníka nemůže být číslo a ani být prázdné.")
            if jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")

            prijmeni = input("Zadejte příjmení zákazníka: ")
            if prijmeni.isnumeric() or prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            novy_email = input("Zadejte nový e-mail zákazníka: ")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", novy_email):
                raise ValueError("Zadaný e-mail není platný.")
            if jmeno.isspace():
                raise ValueError("E-mail nemůže být prázdný")

            self.zakaznik_model.updateEmail(jmeno, prijmeni, novy_email)
            logging.info(f"{self.current_time}Upravení e-mailu zákazníka")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")

    def upravit_adresu_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení adresy zákazníka
        """
        try:
            jmeno = input("Zadejte křestní jméno zákazníka: ")
            if jmeno.isnumeric() or jmeno.isspace():
                raise ValueError("Jméno zákazníka nemůže být číslo a ani být prázdné.")
            if jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")

            prijmeni = input("Zadejte příjmení zákazníka: ")
            if prijmeni.isnumeric() or prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            adresa = input("Zadejte novou adresu zákazníka: ")
            if adresa.isspace():
                raise ValueError("Adresa nemůže být prázdná")

            self.zakaznik_model.updateAdress(jmeno, prijmeni, adresa)
            logging.info(f"{self.current_time}Upravení adresy zákazníka")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")

    def upravit_telefon_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro upravení telefonu zákazníka
        """
        try:
            jmeno = input("Zadejte křestní jméno zákazníka: ")
            if jmeno.isnumeric() or jmeno.isspace():
                raise ValueError("Jméno zákazníka nemůže být číslo a ani být prázdné.")
            if jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")

            prijmeni = input("Zadejte příjmení zákazníka: ")
            if prijmeni.isnumeric() or prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            telefon = input("Zadejte telefonní číslo zákazníka (formát: ###-###-###): ")
            if not re.match("^[0-9]{3}-[0-9]{3}-[0-9]{3}$", telefon):
                raise ValueError("Telefonní číslo musí být ve formátu ###-###-### a obsahovat pouze čísla.")
            if telefon.isspace():
                raise ValueError("Telefonní číslo nemůže být prázdné")

            self.zakaznik_model.updateAdress(jmeno, prijmeni, telefon)
            logging.info(f"{self.current_time}Upravení telefonu zákazníka")

        except ValueError as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")
        except Exception as err:
            print("Chyba: ", err)
            logging.error(f"{self.current_time}Při upravování zákazníka došlo k chybě: {err}")

    def smazat_zakaznika(self):
        """
        Metoda kontroluje vstupy a volá metodu pro smazání zákazníka
        """
        try:
            jmeno = input("Zadejte křestní jméno zákazníka: ")
            if jmeno.isnumeric() or jmeno.isspace():
                raise ValueError("Jméno zákazníka nemůže být číslo a ani být prázdné.")
            if jmeno.isspace():
                raise ValueError("Jméno nemůže být prázdné")

            prijmeni = input("Zadejte příjmení zákazníka: ")
            if prijmeni.isnumeric() or prijmeni.isspace():
                raise ValueError("Příjmení zákazníka nemůže být číslo a ani být prázdné.")
            if prijmeni.isspace():
                raise ValueError("Příjmení nemůže být prázdné")

            self.zakaznik_model.delete(jmeno, prijmeni)
            logging.info(f"{self.current_time}Smazání zákazníka")
        except ValueError as err:
            print("Chyba: ", err)
        except Exception as err:
            print(f"Nepodařilo se smazat zakaznika: {err}")
            logging.error(f"{self.current_time}Při odstraňování zákazníka došlo k chybě: {err}")
