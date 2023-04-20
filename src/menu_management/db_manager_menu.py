import time
from src.controllers.database_manager import DatabaseManager


class DatabaseManagerMenu:
    def __init__(self):
        self.database_manager = DatabaseManager()

        self.db_manager_prikazy = {
            "1": self.nahrani_zalohy_databaze,
            "2": self.export_dat_databaze,
            "0": self.zpet_na_main_menu,
        }
    def odradkovani(self):
        odradkovani = "=" * 20
        print(odradkovani)

    def nahrani_zalohy_databaze(self):
        self.odradkovani()
        print("Nahrávání zálohy dat do databáze")
        self.odradkovani()
        self.database_manager.nahrani_zalohy_databaze()


    def export_dat_databaze(self):
        self.odradkovani()
        print("Vytváření nové zálohy dat z databáze")
        self.odradkovani()
        self.database_manager.export_dat_databaze()

    def zpet_na_main_menu(self):
        self.odradkovani()
        from src.menu_management.main_menu import MainMenu
        MainMenu().run_main_menu()

    def display_db_manager_menu(self):
        time.sleep(1)
        print(
            """
    Menu pro správu databáze:

        1. Nahrání zálohy dat do databáze
        2. Vytvořit novou zálohu dat z databáze

        0. Zpět
        """
        )

    def run_db_manager_menu(self):
        while True:
            self.display_db_manager_menu()
            vyber = input("Zadejte svou volbu (1-2, nebo 0 pro návrat na hlavní menu): ")
            if vyber == "0":
                self.zpet_na_main_menu()
                break
            elif vyber in self.db_manager_prikazy:
                self.db_manager_prikazy[vyber]()
            else:
                print("Neplatná volba, prosím zkuste to znovu.")

