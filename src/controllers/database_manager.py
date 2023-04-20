import logging
from datetime import datetime

from src.db.connection import DatabaseConnector
from src.db.restart_db import RestartDB


class DatabaseManager:
    def __init__(self):
        self.restart = RestartDB()
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi", err)
            logging.error(f"{self.current_time}Nepodařilo se připojit k tabulce kategorie: {err}")

    def nahrani_zalohy_databaze(self):
        """
        Metoda restartuje databázi a to tak, že smaže všechny tabulky, trigery a pohledy,
        po té je opět vytvoří a nahraje i s daty, které byly vytvořeny při posledním backupu
        """
        try:
            self.restart.use_db()
            self.restart.smazani_tabulek()
            self.restart.smazani_trigeru()
            self.restart.smazani_pohledu()
        except Exception as err:
            print(f"Chyba při smazání databáze: {err}")
            logging.error(f"{self.current_time}Při nahrávání backupu došlo k chybě při smazávání databáze: {err}")

        try:
            self.restart.vytvoreni_tabulek()
            self.restart.vytvoreni_trigeru()
            self.restart.vytvoreni_pohledu()
            self.restart.import_databaze()
            logging.info(f"{self.current_time}Nahrání backupu do databáze")
        except Exception as err:
            print(f"Chyba při vytváření databáze: {err}")
            logging.error(f"{self.current_time}Při nahrávání backupu došlo k chybě při vytváření databáze a importu dat: {err}")

    def export_dat_databaze(self):
        """
        Metoda zavolá metodu pro export dat databáze
        """
        try:
            self.restart.export_databaze()
            logging.info(f"{self.current_time}Vytvoření backupu dat")
        except Exception as err:
            print(f"Chyba při exportu dat z databáze: {err}")
            logging.error(f"{self.current_time}Při vytváření backupu dat došlo k chybě: {err}")
