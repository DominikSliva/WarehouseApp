import mysql
from src.db.connection import DatabaseConnector


class Zakaznik:
    def __init__(self):
        try:
            self.connection, self.cursor = DatabaseConnector().pripojeni()
        except Exception as err:
            print("Došlo k chybě při připojení k databázi")

    def add(self, jmeno, prijmeni, email, adresa, telefon):
        """
        Metoda vytvoří v databázi nového zákazníka
        :param jmeno: Křestní jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param email: E-mail zákazníka
        :param adresa: Adresa zákazníka
        :param telefon: Telefon zákazníka
        """
        try:
            sql_insert_zakaznik = "insert into zakaznik(jmeno, prijmeni, email, adresa, telefon) values (%s,%s,%s,%s,%s)"
            val_insert_zakaznik = (jmeno, prijmeni, email, adresa, telefon)
            self.cursor.execute(sql_insert_zakaznik, val_insert_zakaznik)
            self.connection.commit()
        except Exception as err:
            print("Došlo k chybě při vkládání nového zákazníka do databáze")

    def findAll(self):
        """
        Metoda, pro vypsání všech údajů o všech zákaznících
        """
        try:
            self.cursor.execute("select * from zakaznik")
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print("V zákaznících neexistuje žádný záznam.")
        except Exception as err:
            print("Došlo k chybě při čtení z databáze")

    def findByFirstName(self, jmeno):
        """
        Metoda vypíše všechny zákazníky s vybraným jménem
        :param jmeno: Křestní jméno zákazníka
        """
        sql_select_zakaznik = "select * from zakaznik where jmeno = %s"
        val_select_zakaznik = (jmeno,)
        try:
            self.cursor.execute(sql_select_zakaznik, val_select_zakaznik)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Zákazník s křestním jménem {jmeno} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání zákazníka:", err)

    def findByLastName(self, prijmeni):
        """
        Metoda vypíše všechny zákazníky s vybraným příjmením
        :param prijmeni: Příjmení zákazníka
        """
        sql_select_zakaznik = "select * from zakaznik where prijmeni = %s"
        val_select_zakaznik = (prijmeni,)
        try:
            self.cursor.execute(sql_select_zakaznik, val_select_zakaznik)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Zákazník s příjmením {prijmeni} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání zákazníka:", err)

    def findByEmail(self, email):
        """
        Metoda vypíše všechny zákazníky s vybraným e-mailem
        :param email: E-mail zákazníka
        """
        sql_select_zakaznik = "select * from zakaznik where email = %s"
        val_select_zakaznik = (email,)
        try:
            self.cursor.execute(sql_select_zakaznik, val_select_zakaznik)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Zákazník s e-mailem {email} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání zákazníka:", err)


    def findByAdress(self, adresa):
        """
        Metoda vypíše všechny zákazníky s vybranou adresou
        :param adresa: Adresa zákazníka
        """
        sql_select_zakaznik = "select * from zakaznik where adresa = %s"
        val_select_zakaznik = (adresa,)
        try:
            self.cursor.execute(sql_select_zakaznik, val_select_zakaznik)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Zákazník s adresou {adresa} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání zákazníka:", err)

    def findByPhone(self, telefon):
        """
        Metoda vypíše všechny zákazníky s vybraným telefonním číslem
        :param telefon: Telefonní číslo zákazníka ve formátu ###-###-###
        """
        sql_select_zakaznik = "select * from zakaznik where telefon = %s"
        val_select_zakaznik = (telefon,)
        try:
            self.cursor.execute(sql_select_zakaznik, val_select_zakaznik)
            vysledek = self.cursor.fetchall()
            for x in vysledek:
                print(x)
            if not vysledek:
                print(f"Zákazník s telefonním číslem {telefon} neexistuje.")
        except Exception as err:
            print("Došlo k chybě při vyhledávání zákazníka:", err)

    def updateFirstName(self, stare_jmeno, prijmeni, nove_jmeno):
        """
        Metoda změní křestní jméno vybraného zákazníka
        :param stare_jmeno: Křestní jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param nove_jmeno: Nové křestní jméno zákazníka
        """
        sql_update_zakaznik = "update zakaznik set jmeno = %s where jmeno = %s and prijmeni = %s"
        val_update_zakaznik = (nove_jmeno, stare_jmeno, prijmeni)
        try:
            self.cursor.execute(sql_update_zakaznik, val_update_zakaznik)
            if self.cursor.rowcount == 0:
                print(f"Zákazník s křestním jménem {stare_jmeno} a příjmením {prijmeni} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit zákazníka s křestním jménem {stare_jmeno} a příjmením {prijmeni}.")

    def updateLastName(self, stare_prijmeni, nove_prijmeni):
        """
        Metoda změní příjmení vybraného zákazníka
        :param stare_prijmeni: Příjmení zákazníka
        :param nove_prijmeni: Nové příjmení zákazníka
        """
        sql_update_zakaznik = "update zakaznik set prijmeni = %s where prijmeni = %s"
        val_update_zakaznik = (nove_prijmeni, stare_prijmeni)
        try:
            self.cursor.execute(sql_update_zakaznik, val_update_zakaznik)
            if self.cursor.rowcount == 0:
                print(f"Zákazník s příjmením {stare_prijmeni} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit zákazníka s příjmením {stare_prijmeni}.")

    def updateEmail(self, jmeno, prijmeni, novy_email):
        """
        Metoda změní e-mail vybraného zákazníka
        :param jmeno: Křestní jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param novy_email: Nový e-mail zákazníka
        """
        sql_update_zakaznik = "update zakaznik set email = %s where jmeno = %s and prijmeni = %s"
        val_update_zakaznik = (novy_email, jmeno, prijmeni)
        try:
            self.cursor.execute(sql_update_zakaznik, val_update_zakaznik)
            if self.cursor.rowcount == 0:
                print(f"Zákazník s křestním jménem {jmeno} a příjmením {prijmeni} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit zákazníka s křestním jménem {jmeno} a příjmením {prijmeni}.")

    def updateAdress(self, jmeno, prijmeni, nova_adresa):
        """
        Metoda změní adresu vybraného zákazníka
        :param jmeno: Křestní jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param nova_adresa: Nová adresa zákazníka
        """
        sql_update_zakaznik = "update zakaznik set adresa = %s where jmeno = %s and prijmeni = %s"
        val_update_zakaznik = (nova_adresa, jmeno, prijmeni)
        try:
            self.cursor.execute(sql_update_zakaznik, val_update_zakaznik)
            if self.cursor.rowcount == 0:
                print(f"Zákazník s křestním jménem {jmeno} a příjmením {prijmeni} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit zákazníka s křestním jménem {jmeno} a příjmením {prijmeni}.")

    def updatePhone(self, jmeno, prijmeni, novy_telefon):
        """
        Metoda změní telefonní číslo vybraného zákazníka
        :param jmeno: Křestní jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        :param novy_telefon: Nové telefonní číslo zákazníka
        """
        sql_update_zakaznik = "update zakaznik set telefon = %s where jmeno = %s and prijmeni = %s"
        val_update_zakaznik = (novy_telefon, jmeno, prijmeni)
        try:
            self.cursor.execute(sql_update_zakaznik, val_update_zakaznik)
            if self.cursor.rowcount == 0:
                print(f"Zákazník s křestním jménem {jmeno} a příjmením {prijmeni} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se upravit zákazníka s křestním jménem {jmeno} a příjmením {prijmeni}.")

    def delete(self, jmeno, prijmeni):
        """
        Metoda smaže zákazníka
        :param jmeno: Křestní jméno zákazníka
        :param prijmeni: Příjmení zákazníka
        """
        sql_delete_zakaznik = "delete from zakaznik where jmeno = %s and prijmeni = %s"
        val_delete_zakaznik = (jmeno, prijmeni)
        try:
            self.cursor.execute(sql_delete_zakaznik, val_delete_zakaznik)
            if self.cursor.rowcount == 0:
                print(f"Zákazník s křestním jménem {jmeno} a příjmením {prijmeni} neexistuje.")
            self.connection.commit()
        except mysql.connector.errors.ProgrammingError:
            print(f"Nepodařilo se smazat zákazníka s křestním jménem {jmeno} a příjmením {prijmeni}.")





