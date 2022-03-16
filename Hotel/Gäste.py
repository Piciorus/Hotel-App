import pickle
class Gast:
    def __init__(self,vorname,nachname):
        self.vorname = vorname
        self.nachname = nachname
        self.rezervierungen = []

    def __str__(self):
        return f'{self.vorname},{self.nachname}'

class Gastlist:
    def __init__(self):
        self.gastliste = []

    def addGast(self,g1):
        self.gastliste.append(g1)

    def aktualisierennachname(self,old,neue):
        nr = 0
        for i,gast in enumerate(self.gastliste):
             if gast.vorname == old.vorname and gast.nachname == old.nachname:
                gast.nachname = neue.nachname
                nr += 1
        if nr == 0:
            print("Gast nicht gefunden")
        else:
            print("Gast war gefunden " + str(nr) + " " + "mal , und nachname war aktualisiert")

    def loschunggast(self,g1):
        for i,gast in enumerate(self.gastliste):
            if gast.vorname == g1.vorname and gast.nachname == g1.nachname:
                self.gastliste.pop(i)

    def listanzeige(self):
        for guest in self.gastliste:
            print(f'{guest.vorname},{guest.nachname}')

    def find(self,x):
        for i, loc in enumerate(self.gastliste):
            if loc.vorname == x.vorname and loc.nachname == x.nachname:
                return self.gastliste[i]



def gastmenu(list1):
    while True:
        print("""
        1 - "Füge ein neuer Gast hin"
        2 - "Aktualisierennachname eines Gast"
        3 - "Anzeige die Liste des Gaste"
        4 - "Loschung ein Gast aus Liste"
        5 - "Exit"
        """)
        option = int(input("option: "))
        if option == 1:
            vorname = input("vorname: ")
            nachname = input("nachname: ")
            a = Gast(vorname,nachname)
            list1.addGast(a)
        if option == 2:
            vorname = input("vorname: ")
            nachname = input("nachname: ")
            old = Gast(vorname,nachname)
            nachnameneue = input("nachnameneue: ")
            neu = Gast(vorname,nachnameneue)
            list1.aktualisierennachname(old,neu)
        if option == 3:
            list1.listanzeige()
        pickle.dump(list1, open("Gästen.txt", "wb"))
        if option == 4:
            vorname = input("vorname: ")
            nachname = input("nachname: ")
            g1 = Gast(vorname,nachname)
            list1.loschunggast(g1)
        if option == 5:
            return 0







