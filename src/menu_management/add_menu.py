import time
from src.controllers.dodavatel_controller import DodavatelController
from src.controllers.kategorie_controller import KategorieController
from src.controllers.lokace_ulozeni_controller import LokaceUlozeniController
from src.controllers.objednavka_controller import ObjednavkaController
from src.controllers.polozka_controller import PolozkaController
from src.controllers.polozka_v_objednavce_controller import PolozkaVObjednavceController
from src.controllers.zakaznik_controller import ZakaznikController


class AddMenu:
    def __init__(self):
        self.dodavatel = DodavatelController()
        self.kategorie = KategorieController()
        self.lokace = LokaceUlozeniController()
        self.polozka = PolozkaController()
        self.zakaznik = ZakaznikController()
        self.objednavka = ObjednavkaController()
        self.polozka_v_objednavce = PolozkaVObjednavceController()

        self.add_prikazy = {
            "1": self.pridani_dodavatele,
            "2": self.pridani_kategorie,
            "3": self.pridani_lokace,
            "4": self.pridani_polozky,
            "5": self.pridani_zakaznika,
            "6": self.pridani_objednavky_s_jakymkoliv_datem,
            "7": self.pridani_objednavky_s_momentalnim_datem,
            "8": self.pridani_polozky_do_objednavky,
            "0": self.zpet_na_main_menu,
        }
    def odradkovani(self):
        odradkovani = "=" * 20
        print(odradkovani)

    def pridani_dodavatele(self):
        self.odradkovani()
        print("Vytvoření nového dodavatele")
        self.odradkovani()
        self.dodavatel.pridat_dodavatele()

    def pridani_kategorie(self):
        self.odradkovani()
        print("Vytvoření nové kategorie")
        self.odradkovani()
        self.kategorie.pridat_kategorii()

    def pridani_lokace(self):
        self.odradkovani()
        print("Vytvoření nové lokace umístění")
        self.odradkovani()
        self.lokace.pridat_lokaci_ulozeni()

    def pridani_polozky(self):
        self.odradkovani()
        print("Vytvoření nové položky")
        self.odradkovani()
        self.polozka.pridat_polozku()

    def pridani_zakaznika(self):
        self.odradkovani()
        print("Vytvoření nového zákazníka")
        self.odradkovani()
        self.zakaznik.pridat_zakaznika()

    def pridani_objednavky_s_jakymkoliv_datem(self):
        self.odradkovani()
        print("Vytvoření nové objednávky s jakýmoliv datem")
        self.odradkovani()
        self.objednavka.pridat_objednavku_s_jakymkoliv_datem()

    def pridani_objednavky_s_momentalnim_datem(self):
        self.odradkovani()
        print("Vytvoření nové objednávky s momentálním datem")
        self.odradkovani()
        self.objednavka.pridat_objednavku_s_momentálním_datumem()

    def pridani_polozky_do_objednavky(self):
        self.odradkovani()
        print("Přidání nové položky do objednávky")
        self.odradkovani()
        self.polozka_v_objednavce.pridat_polozku_do_objednavky()

    def zpet_na_main_menu(self):
        self.odradkovani()
        from src.menu_management.main_menu import MainMenu
        MainMenu().run_main_menu()

    def display_add_menu(self):
        time.sleep(1)
        print(
            """
    Menu pro přidání:

        1. Nového dodavatele
        2. Novou kategorii
        3. Novou lokaci uložení
        4. Novou položku
        5. Nového zákazníka
        6. Novou objednávku s jakýmkoliv datem
        7. Novou objednávku s momentálním datem
        8. Novou položku do objednávky

        0. Zpět
        """
        )

    def run_add_menu(self):
        while True:
            self.display_add_menu()
            vyber = input("Zadejte svou volbu (1-8, nebo 0 pro návrat na hlavní menu): ")
            if vyber == "0":
                self.zpet_na_main_menu()
                break
            elif vyber in self.add_prikazy:
                self.add_prikazy[vyber]()
            else:
                print("Neplatná volba, prosím zkuste to znovu.")

