import time
from src.entity.find_preferences import FindPreferences


class FindPreferencesMenu:
    def __init__(self):
        self.find_preferences = FindPreferences()

        self.find_references_prikazy = {
            "1": self.pohled_polozky_a_lokace,
            "2": self.pohled_na_zasoby,
            "3": self.pohled_expedovatelnost_objednávek,
            "4": self.pohled_historie_pohybu_polozky_,
            "0": self.zpet_na_main_menu,
        }

    def odradkovani(self):
        odradkovani = "=" * 20
        print(odradkovani)

    def pohled_polozky_a_lokace(self):
        self.odradkovani()
        print("Vypisování pohledu pro položky a jejich lokace")
        self.odradkovani()
        self.find_preferences.pohled_polozky_a_lokace()

    def pohled_na_zasoby(self):
        self.odradkovani()
        print("Vypisování pohledu pro zásoby")
        self.odradkovani()
        self.find_preferences.pohled_na_zasoby()

    def pohled_expedovatelnost_objednávek(self):
        self.odradkovani()
        print("Vypisování pohledu pro expedovatelnost objednávek")
        self.odradkovani()
        self.find_preferences.pohled_expedovatelnost_objednávek()

    def pohled_historie_pohybu_polozky_(self):
        self.odradkovani()
        print("Vypisování pohledu pro historii pohybu položek")
        self.odradkovani()
        self.find_preferences.pohled_historie_pohybu_polozky_()

    def zpet_na_main_menu(self):
        self.odradkovani()
        from src.menu_management.main_menu import MainMenu
        MainMenu().run_main_menu()

    def display_find_references_menu(self):
        time.sleep(1)
        print(
            """
    Menu pro vyhledávající předvolby:

        1. Položky a jejich lokace
        2. Zásoby položek
        3. Expedovatelnost objednávek
        4. Historie pohybu položek

        0. Zpět
        """
        )

    def run_find_references_menu(self):
        while True:
            self.display_find_references_menu()
            vyber = input("Zadejte svou volbu (1-4, nebo 0 pro návrat na hlavní menu): ")
            if vyber == "0":
                self.zpet_na_main_menu()
                break
            elif vyber in self.find_references_prikazy:
                self.find_references_prikazy[vyber]()
            else:
                print("Neplatná volba, prosím zkuste to znovu.")
