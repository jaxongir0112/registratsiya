import os
import platform
import mysql.connector


class Registratsiya:
    def __init__(self):
        self.name =None
        self.login = None
        self.password = None
        self.yoshi = None

        self.show_info()

    def xabar(self):
        print("""
        1. Registratsiya
        2. Log_in
        """)

    def show_info(self):
        self.xabar()
        tanlov = input("Amalni kiriting: ").strip()
        tanla = ["1","2"]
        while tanlov not in tanla:
            self.clear()
            print("Tanlov notug'ri kiritildi")
            self.show_info()
        if tanlov == "1":
            self.registr()
        elif tanlov == "2":
            self.log_in()



    def registr(self):
        name = input("Ismingizni kiriting: ").strip()
        while not name.isalpha():
            self.clear()
            print("Ism harflardan tashkil topkan bulishi kerag")
            name = input("Ismingizni kiriting: ").strip()

        login = input("Loginni kiriting: ").strip()
        while not login.isalnum():
            self.clear()
            print("Loginda xatolik mavjud")
            login = input("Loginni kiriting: ").strip()

        password = input("Parolni kiriting: ").strip()
        password1 = input("Parolni qaytadan kiriting: ").strip()
        while password1 != password or self.bush(password):
            self.clear()
            print("Parolni boshqatdan kiriting")
            password = input("Parolni kiriting: ").strip()
            password1 = input("Parolni qaytadan kiriting: ").strip()

        while len(password) <=6:
            self.clear()
            print("Parolni boshqatdan kiriting")
            password = input("Parolni kiriting: ").strip()
            password1 = input("Parolni qaytadan kiriting: ").strip()

        yosh = input("Yoshingizni kiriting: ").strip()
        while not yosh.isnumeric():
            self.clear()
            print("Xato kiritildi")
            yosh = input("Yoshingizni kiriting: ").strip()

        self.name = name
        self.login = login
        self.password = password
        self.yoshi = yosh
        self.data_base()

    def data_base(self):
        self.my_db = mysql.connector.connect(
            host='localhost',
            user='jahon',
            password='12345678',
            database='Sayt'
        )

        self.registr = self.my_db.cursor()
        self.create_table()
    def create_table(self):
        self.registr.execute("CREATE TABLE if not exists ruyhat (Id int UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
                     "ismi VARCHAR(30),"
                     "login VARCHAR(39),"
                     "password VARCHAR(20),"
                     "yoshi VARCHAR(3))")
        self.my_db.cursor()
        self.write_base()

    def write_base(self):
        self.registr.execute("INSERT INTO ruyhat (ismi,login,password,yoshi) VALUES ('{}','{}','{}','{}')".format(self.name,self.login,self.password,self.yoshi))
        self.my_db.commit()



    def log_in(self):
        self.kirish_log()

    def kirish_log(self):
        self.my_db = mysql.connector.connect(
            host='localhost',
            user='jahon',
            password='12345678',
            database='Sayt'
        )

        self.registr = self.my_db.cursor()
        k_login = input("Loginni kiriting: ").strip()
        self.registr.execute("Select login FROM ruyhat where login = '{}'".format(k_login))
        rows = self.registr.fetchall()

        if len(rows) != 0:
            if k_login == rows[0][0]:
                self.kirish_parol()
        else:
            self.clear()
            print("Loginda xatolik bor ")
            self.kirish_log()


    def kirish_parol(self):
        self.my_db = mysql.connector.connect(
            host='localhost',
            user='jahon',
            password='12345678',
            database='Sayt'
        )

        self.registr = self.my_db.cursor()
        k_password = input("Parolni  kiriting: ").strip()
        self.registr.execute("Select password FROM ruyhat where password = '{}'".format(k_password))
        row = self.registr.fetchall()

        if len(row) != 0:
            if k_password == row[0][0]:
                print("Xush  kelibsiz")
        else:
            self.clear()
            print("Parolda hatolik bor ")
            self.kirish_parol()


    def clear(self):
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")

    @staticmethod
    def bush(text)-> bool:
        return not text


ob = Registratsiya()
