import sys
import time
from src.controllers.database_manager import DatabaseManager


class MainMenu:
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.main_prikazy = {
            "1": self.vypsani_menu_pridat,
            "2": self.vypsani_menu_vyhledat,
            "3": self.vypsani_menu_upravit,
            "4": self.vypsani_menu_odstranit,
            "5": self.vypsani_menu_predvoleb,
            "6": self.vypsani_menu_sprava_db,
            "0": self.ukoncit_aplikaci,
        }

    def vypsani_menu_pridat(self):
        from src.menu_management.add_menu import AddMenu
        AddMenu().run_add_menu()

    def vypsani_menu_vyhledat(self):
        from src.menu_management.find_menu import FindMenu
        FindMenu().run_find_menu()

    def vypsani_menu_upravit(self):
        from src.menu_management.update_menu import UpdateMenu
        UpdateMenu().run_update_menu()

    def vypsani_menu_odstranit(self):
        from src.menu_management.delete_menu import DeleteMenu
        DeleteMenu().run_delete_menu()

    def vypsani_menu_predvoleb(self):
        from src.menu_management.find_preferences_menu import FindPreferencesMenu
        FindPreferencesMenu().run_find_references_menu()

    def vypsani_menu_sprava_db(self):
        from src.menu_management.db_manager_menu import DatabaseManagerMenu
        DatabaseManagerMenu().run_db_manager_menu()

    def display_main_menu(self):
        time.sleep(1)
        print(
            """
Vítejte ve WAREHOUSE APPLICATION!

    Menu:

        1. Přidat
        2. Vyhledat
        3. Upravit
        4. Odstranit
        5. Předvolby pro vyhledávání
        6. Správa databáze

        0. Ukončit
        """
        )

    def run_main_menu(self):
        while True:
            self.display_main_menu()
            vyber = input("Zadejte svou volbu (1-6, nebo 0 pro ukončení): ")
            if vyber == "0":
                self.ukoncit_aplikaci()
                break
            elif vyber in self.main_prikazy:
                self.main_prikazy[vyber]()
            else:
                print("Neplatná volba, prosím zkuste to znovu.")

    def ukoncit_aplikaci(self):
        print("Aplikace se ukončuje...")
        sys.exit()

