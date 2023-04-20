import time
from src.controllers.dodavatel_controller import DodavatelController
from src.controllers.kategorie_controller import KategorieController
from src.controllers.lokace_ulozeni_controller import LokaceUlozeniController
from src.controllers.objednavka_controller import ObjednavkaController
from src.controllers.polozka_controller import PolozkaController
from src.controllers.polozka_v_objednavce_controller import PolozkaVObjednavceController
from src.controllers.zakaznik_controller import ZakaznikController


class DeleteMenu:
    def __init__(self):
        self.dodavatel = DodavatelController()
        self.kategorie = KategorieController()
        self.lokace = LokaceUlozeniController()
        self.polozka = PolozkaController()
        self.zakaznik = ZakaznikController()
        self.objednavka = ObjednavkaController()
        self.polozka_v_objednavce = PolozkaVObjednavceController()

        self.delete_prikazy = {
            "1": self.smazat_dodavatele,
            "2": self.smazat_kategorii,
            "3": self.smazat_lokaci,
            "4": self.smazani_polozky,
            "5": self.smazat_zakaznika,
            "6": self.smazat_objednavky,
            "7": self.smazani_polozky_z_objednavky,
            "0": self.zpet_na_main_menu,
        }
    def odradkovani(self):
        odradkovani = "=" * 20
        print(odradkovani)

    def smazat_dodavatele(self):
        self.odradkovani()
        print("Smazání dodavatele")
        self.odradkovani()
        self.dodavatel.smazat_dodavatele()

    def smazat_kategorii(self):
        self.odradkovani()
        print("Smazání kategorie")
        self.odradkovani()
        self.kategorie.smazat_kategorii()

    def smazat_lokaci(self):
        self.odradkovani()
        print("Smazání lokace umístění")
        self.odradkovani()
        self.lokace.smazat_lokaci()

    def smazani_polozky(self):
        self.odradkovani()
        print("Smazání položky")
        self.odradkovani()
        self.polozka.smazani_polozky()

    def smazat_zakaznika(self):
        self.odradkovani()
        print("Smazání zákazníka")
        self.odradkovani()
        self.zakaznik.smazat_zakaznika()

    def smazat_objednavky(self):
        self.odradkovani()
        print("Smazání objednávky")
        self.odradkovani()
        self.objednavka.smazat_objednavky()

    def smazani_polozky_z_objednavky(self):
        self.odradkovani()
        print("Smazání položy v objednávce")
        self.odradkovani()
        self.polozka_v_objednavce.smazani_polozky_z_objednavky()

    def zpet_na_main_menu(self):
        self.odradkovani()
        from src.menu_management.main_menu import MainMenu
        MainMenu().run_main_menu()

    def display_delete_menu(self):
        time.sleep(1)
        print(
            """
    Menu pro smazání:

        1. Dodavatele
        2. Kategorie
        3. Lokace uložení
        4. Položky
        5. Zákazníka
        6. Objednávky
        7. Položky z objednávky

        0. Zpět
        """
        )

    def run_delete_menu(self):
        while True:
            self.display_delete_menu()
            vyber = input("Zadejte svou volbu (1-8, nebo 0 pro návrat na hlavní menu): ")
            if vyber == "0":
                self.zpet_na_main_menu()
                break
            elif vyber in self.delete_prikazy:
                self.delete_prikazy[vyber]()
            else:
                print("Neplatná volba, prosím zkuste to znovu.")

