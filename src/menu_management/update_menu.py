import time
from src.controllers.dodavatel_controller import DodavatelController
from src.controllers.kategorie_controller import KategorieController
from src.controllers.lokace_ulozeni_controller import LokaceUlozeniController
from src.controllers.objednavka_controller import ObjednavkaController
from src.controllers.polozka_controller import PolozkaController
from src.controllers.polozka_v_objednavce_controller import PolozkaVObjednavceController
from src.controllers.zakaznik_controller import ZakaznikController


class UpdateMenu:
    def __init__(self):
        self.dodavatel = DodavatelController()
        self.kategorie = KategorieController()
        self.lokace = LokaceUlozeniController()
        self.polozka = PolozkaController()
        self.zakaznik = ZakaznikController()
        self.objednavka = ObjednavkaController()
        self.polozka_v_objednavce = PolozkaVObjednavceController()

        self.update_prikazy = {
            "1": self.upravit_nazev_dodavatele,
            "2": self.upravit_adresu_dodavatele,
            "3": self.upravit_telefonni_cislo_dodavatele,
            "4": self.upravit_popis_kategorie,
            "5": self.upravit_nazev_lokace,
            "6": self.upravit_kapacitu_lokace,
            "7": self.upravit_cenu_polozky,
            "8": self.upravit_kod_polozky,
            "9": self.upravit_pocet_ks_polozky,
            "10": self.upravit_lokaci_polozky,
            "11": self.upravit_dodavatele_polozky,
            "12": self.upravit_kategorii_polozky,
            "13": self.upravit_jmeno_zakaznika,
            "14": self.upravit_prijmeni_zakaznika,
            "15": self.upravit_email_zakaznika,
            "16": self.upravit_adresu_zakaznika,
            "17": self.upravit_telefon_zakaznika,
            "18": self.upravit_objednavku_na_expedovanou,
            "19": self.upravit_objednavku_na_neexpedovanou,
            "20": self.upravit_pocet_ks_polozky_v_objednavce,
            "0": self.zpet_na_main_menu,
        }
    def odradkovani(self):
        odradkovani = "=" * 20
        print(odradkovani)

    def upravit_nazev_dodavatele(self):
        self.odradkovani()
        print("Upravování názvu dodavatele")
        self.odradkovani()
        self.dodavatel.upravit_nazev_dodavatele()

    def upravit_adresu_dodavatele(self):
        self.odradkovani()
        print("Upravování adresy dodavatele")
        self.odradkovani()
        self.dodavatel.upravit_adresu_dodavatele()

    def upravit_telefonni_cislo_dodavatele(self):
        self.odradkovani()
        print("Upravování telefonního čísla dodavatele")
        self.odradkovani()
        self.dodavatel.upravit_telefonni_cislo_dodavatele()

    def upravit_popis_kategorie(self):
        self.odradkovani()
        print("Upravování popisu kategorie")
        self.odradkovani()
        self.kategorie.upravit_popis_kategorie()

    def upravit_nazev_lokace(self):
        self.odradkovani()
        print("Upravování názvu lokace umístění")
        self.odradkovani()
        self.lokace.upravit_nazev_lokace()

    def upravit_kapacitu_lokace(self):
        self.odradkovani()
        print("Upravování kapacity lokace umístění")
        self.odradkovani()
        self.lokace.upravit_kapacitu_lokace()

    def upravit_cenu_polozky(self):
        self.odradkovani()
        print("Upravování ceny položky")
        self.odradkovani()
        self.polozka.upravit_cenu_polozky()

    def upravit_kod_polozky(self):
        self.odradkovani()
        print("Upravování kódu položky")
        self.odradkovani()
        self.polozka.upravit_kod_polozky()

    def upravit_pocet_ks_polozky(self):
        self.odradkovani()
        print("Upravování počtu kusů položky")
        self.odradkovani()
        self.polozka.upravit_pocet_ks_polozky()

    def upravit_lokaci_polozky(self):
        self.odradkovani()
        print("Upravování umístění položky")
        self.odradkovani()
        self.polozka.upravit_lokaci_polozky()

    def upravit_dodavatele_polozky(self):
        self.odradkovani()
        print("Upravování dodavatele položky")
        self.odradkovani()
        self.polozka.upravit_dodavatele_polozky()

    def upravit_kategorii_polozky(self):
        self.odradkovani()
        print("Upravování kategorie položky")
        self.odradkovani()
        self.polozka.upravit_kategorii_polozky()

    def upravit_jmeno_zakaznika(self):
        self.odradkovani()
        print("Upravení jména zákazníka")
        self.odradkovani()
        self.zakaznik.upravit_jmeno_zakaznika()

    def upravit_prijmeni_zakaznika(self):
        self.odradkovani()
        print("Upravení příjmení zákazníka")
        self.odradkovani()
        self.zakaznik.upravit_prijmeni_zakaznika()

    def upravit_email_zakaznika(self):
        self.odradkovani()
        print("Upravení e-mailu zákazníka")
        self.odradkovani()
        self.zakaznik.upravit_email_zakaznika()

    def upravit_adresu_zakaznika(self):
        self.odradkovani()
        print("Upravení adresy zákazníka")
        self.odradkovani()
        self.zakaznik.upravit_adresu_zakaznika()

    def upravit_telefon_zakaznika(self):
        self.odradkovani()
        print("Upravení telefonního čísla zákazníka")
        self.odradkovani()
        self.zakaznik.upravit_telefon_zakaznika()

    def upravit_objednavku_na_expedovanou(self):
        self.odradkovani()
        print("Upravení stavu objednávky na expedovanou")
        self.odradkovani()
        self.objednavka.upravit_objednavku_na_expedovanou()

    def upravit_objednavku_na_neexpedovanou(self):
        self.odradkovani()
        print("Upravení stavu objednávky na neexpedovanou")
        self.odradkovani()
        self.objednavka.upravit_objednavku_na_neexpedovanou()

    def upravit_pocet_ks_polozky_v_objednavce(self):
        self.odradkovani()
        print("Upravení počet kusů objednané položky")
        self.odradkovani()
        self.polozka_v_objednavce.upravit_pocet_ks_polozky_v_objednavce()

    def zpet_na_main_menu(self):
        self.odradkovani()
        from src.menu_management.main_menu import MainMenu
        MainMenu().run_main_menu()

    def display_update_menu(self):
        time.sleep(1)
        print(
            """
    Menu pro upravení:

        1. Názvu dodavatele
        2. Adresy dodavatele
        3. Telefonního čísla dodavatele
           --- --- --- --- --- --- --- ---
        4. Popisu kategorie
           --- --- --- --- --- --- --- ---
        5. Názvu lokace uložení
        6. Kapacity lokace uložení
           --- --- --- --- --- --- --- ---
        7. Ceny položky
        8. Kódu položky
        9. Počtu kusů položky na skladě
        10. Umístení položky
        11. Dodavatele položky
        12. Kategorie položky
           --- --- --- --- --- --- --- ---
        13. Jména zákazníka
        14. Příjmení zákazníka
        15. E-mailu zákazníka
        16. Adresy zákazníka
        17. Telefonního čísla zákazníka
           --- --- --- --- --- --- --- ---
        18. Stavu objednávky na expedovanou
        19. Stavu objednávky na neexpedovanou
           --- --- --- --- --- --- --- ---
        20. Počtu objednané položky

        0. Zpět
        """
        )

    def run_update_menu(self):
        while True:
            self.display_update_menu()
            vyber = input("Zadejte svou volbu (1-20, nebo 0 pro návrat na hlavní menu): ")
            if vyber == "0":
                self.zpet_na_main_menu()
                break
            elif vyber in self.update_prikazy:
                self.update_prikazy[vyber]()
            else:
                print("Neplatná volba, prosím zkuste to znovu.")

