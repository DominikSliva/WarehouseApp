import json
import logging
from datetime import datetime
import mysql.connector


class DatabaseConnector:
    def __init__(self):
        logging.basicConfig(filename='log/logging.log', level=logging.DEBUG)
        now = datetime.now()
        self.current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    def nacteni_configu(self, file_path):
        """
        Metoda načítá data k přístupu k databázi na serveru
        :param file_path: Cesta ke konfiguračnímu souboru
        :return: Vrací údaje k připojení ze souboru
        """
        try:
            with open(file_path, "r") as config:
                config_data = json.load(config)

                host = config_data["host"]
                database = config_data["database"]
                user = config_data["user"]
                password = config_data["password"]
            return host, database, user, password

        except Exception as err:
            print("Došlo k chybě při čtení z konfiguračního souboru", err)
            logging.error(f"{self.current_time}Při čtení konfiguračního souboru došlo k chybě: {err}")


    def pripojeni(self):
        """
        Metoda se připojuje k databázi
        :return: Vrací připojení a cursor
        """
        try:
            host, database, user, password = self.nacteni_configu("conf/config.json")
            #Přepsat adresu pro config na ../conf/config.json
            connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            cursor = connection.cursor()

        except mysql.connector.Error as err:
            if isinstance(err, mysql.connector.errors.ProgrammingError) and err.errno == 1044:
                print("Chyba: Databáze nenalezena")
                logging.error(f"{self.current_time}Databáze nenalezena: {err}")

            elif isinstance(err, mysql.connector.errors.ProgrammingError) and err.errno == 1045:
                print("Chyba: Chybné uživatelské jméno nebo heslo")
                logging.error(f"{self.current_time}Nesprávné přihlašovací údaje")

            elif isinstance(err, mysql.connector.errors.DatabaseError) and err.errno == 2005:
                print("Chyba: Chybná adresa databáze")
                logging.error(f"{self.current_time}Nesprávná adresa databáze: {err}")
            else:
                print("Chyba: ", err.msg)
                logging.error(f"{self.current_time}Chybné připojení k databázi: {err}")

        except FileNotFoundError:
            print("Soubor nebyl nalezen")
            logging.error(f"{self.current_time}Konfigurační soubor nebyl nalezel")

        else:
            return connection, cursor

