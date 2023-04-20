import time
from src.controllers.dodavatel_controller import DodavatelController
from src.controllers.historie_pohybu_polozek_controller import HistoriePohybuPolozkyController
from src.controllers.kategorie_controller import KategorieController
from src.controllers.lokace_ulozeni_controller import LokaceUlozeniController
from src.controllers.objednavka_controller import ObjednavkaController
from src.controllers.polozka_controller import PolozkaController
from src.controllers.polozka_v_objednavce_controller import PolozkaVObjednavceController
from src.controllers.zakaznik_controller import ZakaznikController


class FindMenu:
    def __init__(self):
        self.dodavatel = DodavatelController()
        self.kategorie = KategorieController()
        self.lokace = LokaceUlozeniController()
        self.polozka = PolozkaController()
        self.zakaznik = ZakaznikController()
        self.objednavka = ObjednavkaController()
        self.polozka_v_objednavce = PolozkaVObjednavceController()
        self.historie_pohybu_polozek = HistoriePohybuPolozkyController()

        self.find_prikazy = {
            "1": self.zobrazit_dodavatele,
            "2": self.zobrazit_dodavatele_podle_nazvu,
            "3": self.zobrazit_dodavatele_podle_adresy,
            "4": self.zobrazit_dodavatele_podle_telefonniho_cisla,
            "5": self.zobrazit_kategorie,
            "6": self.zobrazit_lokace,
            "7": self.zobrazit_lokace_podle_nazvu,
            "8": self.zobrazit_lokace_podle_kapacity,
            "9": self.zobrazit_polozky,
            "10": self.zobrazit_polozky_podle_ceny,
            "11": self.zobrazit_polozky_podle_kodu,
            "12": self.zobrazit_polozky_podle_poctu_ks,
            "13": self.zobrazit_polozky_podle_lokace,
            "14": self.zobrazit_polozky_podle_dodavatele,
            "15": self.zobrazit_polozky_podle_kategorie,
            "16": self.zobrazit_zakaznika,
            "17": self.zobrazit_zakaznika_podle_jmena,
            "18": self.zobrazit_zakaznika_podle_prijmeni,
            "19": self.zobrazit_zakaznika_podle_emailu,
            "20": self.zobrazit_zakaznika_podle_adresy,
            "21": self.zobrazit_zakaznika_podle_telefonu,
            "22": self.zobrazit_objednavky,
            "23": self.zobrazit_objednavky_zakaznika,
            "24": self.zobrazit_neexpedovane_objednavky,
            "25": self.zobrazit_expedovane_objednavky,
            "26": self.zobrazit_podle_data_objednavky,
            "27": self.zobrazit_polozky_v_objednavce,
            "28": self.zobrazit_historii_pohybu_polozek,
            "29": self.zobrazit_historii_pohybu_polozek_podle_puvodni_lokace,
            "30": self.zobrazit_historii_pohybu_polozek_podle_nove_lokace,
            "31": self.zobrazit_historii_pohybu_polozky_od_nejnovejsiho,
            "32": self.zobrazit_historii_pohybu_polozky_od_nejstarsiho,
            "0": self.zpet_na_main_menu
        }
    def odradkovani(self):
        odradkovani = "=" * 20
        print(odradkovani)

    def zobrazit_dodavatele(self):
        self.odradkovani()
        print("Zobrazení všech dodavatelů")
        self.odradkovani()
        self.dodavatel.zobrazit_dodavatele()

    def zobrazit_dodavatele_podle_nazvu(self):
        self.odradkovani()
        print("Zobrazení dodavatelů podle názvu")
        self.odradkovani()
        self.dodavatel.zobrazit_dodavatele_podle_nazvu()

    def zobrazit_dodavatele_podle_adresy(self):
        self.odradkovani()
        print("Zobrazení dodavatelů podle adresy")
        self.odradkovani()
        self.dodavatel.zobrazit_dodavatele_podle_adresy()

    def zobrazit_dodavatele_podle_telefonniho_cisla(self):
        self.odradkovani()
        print("Zobrazení dodavatelů podle telefonního čísla")
        self.odradkovani()
        self.dodavatel.zobrazit_dodavatele_podle_telefonniho_cisla()

    def zobrazit_kategorie(self):
        self.odradkovani()
        print("Zobrazení všech kategorií")
        self.odradkovani()
        self.kategorie.zobrazit_kategorie()

    def zobrazit_lokace(self):
        self.odradkovani()
        print("Zobrazení všech lokací")
        self.odradkovani()
        self.lokace.zobrazit_lokace_ulozeni()

    def zobrazit_lokace_podle_nazvu(self):
        self.odradkovani()
        print("Zobrazení lokací podle názvu")
        self.odradkovani()
        self.lokace.zobrazit_lokace_ulozeni_podle_nazvu()

    def zobrazit_lokace_podle_kapacity(self):
        self.odradkovani()
        print("Zobrazení lokací podle kapacity")
        self.odradkovani()
        self.lokace.zobrazit_lokace_ulozeni_podle_kapacity()

    def zobrazit_polozky(self):
        self.odradkovani()
        print("Zobrazení všech položek")
        self.odradkovani()
        self.polozka.zobrazit_polozky()

    def zobrazit_polozky_podle_ceny(self):
        self.odradkovani()
        print("Zobrazení položek podle ceny")
        self.odradkovani()
        self.polozka.zobrazit_polozku_podle_ceny()

    def zobrazit_polozky_podle_kodu(self):
        self.odradkovani()
        print("Zobrazení položek podle kódu")
        self.odradkovani()
        self.polozka.zobrazit_polozku_podle_kodu()

    def zobrazit_polozky_podle_poctu_ks(self):
        self.odradkovani()
        print("Zobrazení položek podle počtu kusů na skladě")
        self.odradkovani()
        self.polozka.zobrazit_polozku_podle_poctu_ks()

    def zobrazit_polozky_podle_lokace(self):
        self.odradkovani()
        print("Zobrazení položek podle lokace uložení")
        self.odradkovani()
        self.polozka.zobrazit_polozku_podle_lokace_ulozeni()

    def zobrazit_polozky_podle_dodavatele(self):
        self.odradkovani()
        print("Zobrazení položek podle dodavatele")
        self.odradkovani()
        self.polozka.zobrazit_polozku_podle_dodavatele()

    def zobrazit_polozky_podle_kategorie(self):
        self.odradkovani()
        print("Zobrazení položek podle kategorie")
        self.odradkovani()
        self.polozka.zobrazit_polozku_podle_kategorie()

    def zobrazit_zakaznika(self):
        self.odradkovani()
        print("Zobrazení všech zákazníků")
        self.odradkovani()
        self.zakaznik.zobrazit_zakaznika()

    def zobrazit_zakaznika_podle_jmena(self):
        self.odradkovani()
        print("Zobrazení zákazníka podle jména")
        self.odradkovani()
        self.zakaznik.zobrazit_zakaznika_podle_jmena()

    def zobrazit_zakaznika_podle_prijmeni(self):
        self.odradkovani()
        print("Zobrazení zákazníka podle příjmení")
        self.odradkovani()
        self.zakaznik.zobrazit_zakaznika_podle_prijmeni()

    def zobrazit_zakaznika_podle_emailu(self):
        self.odradkovani()
        print("Zobrazení zákazníka podle e-mailu")
        self.odradkovani()
        self.zakaznik.zobrazit_zakaznika_podle_emailu()

    def zobrazit_zakaznika_podle_adresy(self):
        self.odradkovani()
        print("Zobrazení zákazníka podle adresy")
        self.odradkovani()
        self.zakaznik.zobrazit_zakaznika_podle_adresy()

    def zobrazit_zakaznika_podle_telefonu(self):
        self.odradkovani()
        print("Zobrazení zákazníka podle telefonního čísla")
        self.odradkovani()
        self.zakaznik.zobrazit_zakaznika_podle_telefonu()

    def zobrazit_objednavky(self):
        self.odradkovani()
        print("Zobrazení všech objednávek")
        self.odradkovani()
        self.objednavka.zobrazit_objednavky()

    def zobrazit_objednavky_zakaznika(self):
        self.odradkovani()
        print("Zobrazení objednávek zákazníka")
        self.odradkovani()
        self.objednavka.zobrazit_objednavky_zakaznika()

    def zobrazit_neexpedovane_objednavky(self):
        self.odradkovani()
        print("Zobrazení neexpedoanách objednávek")
        self.odradkovani()
        self.objednavka.zobrazit_neexpedovane_objednavky()

    def zobrazit_expedovane_objednavky(self):
        self.odradkovani()
        print("Zobrazení expedovaných objednávek")
        self.odradkovani()
        self.objednavka.zobrazit_expedovane_objednavky()

    def zobrazit_podle_data_objednavky(self):
        self.odradkovani()
        print("Zobrazení objednávek podle data")
        self.odradkovani()
        self.objednavka.zobrazit_podle_data_objednavky()

    def zobrazit_polozky_v_objednavce(self):
        self.odradkovani()
        print("Zobrazení všech položek v objednávkách")
        self.odradkovani()
        self.polozka_v_objednavce.zobrazit_polozky_v_objednavce()

    def zobrazit_historii_pohybu_polozek(self):
        self.odradkovani()
        print("Zobrazení celé historie pohybu položek")
        self.odradkovani()
        self.historie_pohybu_polozek.zobrazit_historii_pohybu_polozek()

    def zobrazit_historii_pohybu_polozek_podle_puvodni_lokace(self):
        self.odradkovani()
        print("Zobrazení historie pohybu položek podle původní lokace")
        self.odradkovani()
        self.historie_pohybu_polozek.zobrazit_historii_pohybu_polozek_podle_puvodni_lokace()

    def zobrazit_historii_pohybu_polozek_podle_nove_lokace(self):
        self.odradkovani()
        print("Zobrazení historie pohybu položek podle nové lokace")
        self.odradkovani()
        self.historie_pohybu_polozek.zobrazit_historii_pohybu_polozek_podle_nove_lokace()

    def zobrazit_historii_pohybu_polozky_od_nejnovejsiho(self):
        self.odradkovani()
        print("Zobrazení historie pohybu položek seřazená od nějnovějšího")
        self.odradkovani()
        self.historie_pohybu_polozek.zobrazit_historii_pohybu_polozky_od_nejnovejsiho()

    def zobrazit_historii_pohybu_polozky_od_nejstarsiho(self):
        self.odradkovani()
        print("Zobrazení historie pohybu položek seřazená od nejstaršího")
        self.odradkovani()
        self.historie_pohybu_polozek.zobrazit_historii_pohybu_polozky_od_nejstarsiho()

    def zpet_na_main_menu(self):
        self.odradkovani()
        from src.menu_management.main_menu import MainMenu
        MainMenu().run_main_menu()

    def display_find_menu(self):
        time.sleep(1)
        print(
            """
    Menu pro zobrazení:

        1. Všech dodavatelů
        2. Dodavatelů podle názvu
        3. Dodavatelů podle adresy
        4. Dodavatelů podle telefonního čísla
           --- --- --- --- --- --- --- ---
        5. Všech kategorií
           --- --- --- --- --- --- --- ---
        6. Všech lokací uložení
        7. Lokací uložení podle názvu
        8. Lokací uložení podle kapacity
           --- --- --- --- --- --- --- ---
        9. Všech položek
        10. Položky podle ceny
        11. Položky podle kódu
        12. Položky podle počtu kusů
        13. Položky podle lokace uložení
        14. Položky podle dodavatele
        15. Položky podle kategorie
           --- --- --- --- --- --- --- ---
        16. Všech zákazníků
        17. Zákazníka podle jména
        18. Zákazníka podle příjmení
        19. Zákazníka podle e-mailu
        20. Zákazníka podle adresy
        21. Zákazníka podle telefonního čísla
           --- --- --- --- --- --- --- ---
        22. Všech objednávek
        23. Objednávek zákazníka
        24. Neexpedovaných objednávek
        25. Expedovaných objednávek
        26. Objednávek podle datumu
           --- --- --- --- --- --- --- ---
        27. Všech položek v objednávkách
           --- --- --- --- --- --- --- ---
        28. Celé historie pohybu položek
        29. Historie pohybu položek podle původní lokace
        30. Historie pohybu položek podle nové lokace
        31. Historie pohybu položky seřazená od nejnovějšího
        32. Historie pohybu položky seřazená od nejstaršího

        0. Zpět
        """
        )

    def run_find_menu(self):
        while True:
            self.display_find_menu()
            vyber = input("Zadejte svou volbu (1-32, nebo 0 pro návrat na hlavní menu): ")
            if vyber == "0":
                self.zpet_na_main_menu()
                break
            elif vyber in self.find_prikazy:
                self.find_prikazy[vyber]()
            else:
                print("Neplatná volba, prosím zkuste to znovu.")

