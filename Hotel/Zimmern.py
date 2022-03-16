import pickle
class Zimmern:
    def __init__(self,nummer,anzahlgasten,preis,farbe,meerblick):
        self.nummer = nummer
        self.anzahlgasten = anzahlgasten
        self.preis = preis
        self.farbe = farbe
        self.meerblick = meerblick

    def __str__(self):
        return f'Zimmer nummer:{self.nummer},Anzahlgasten: {self.anzahlgasten},Preis zimmer:{self.preis},Farbe zimmer:{self.farbe},Meerblick zimmer:{self.meerblick}'

class Zimmernliste:
    def __init__(self):
        self.zimmernliste = []

    def addZimmern(self,z):
        self.zimmernliste.append(z)

    def aktualisierenpreis(self,zimmer,neu):
        for i,zimmer1 in enumerate(self.zimmernliste):
            if zimmer1.nummer == zimmer:
                zimmer1.preis = neu

    def zimmeranzeige(self):
        for zimmer in self.zimmernliste:
            print(f'Zimmer nummer:{zimmer.nummer},Anzahlgasten: {zimmer.anzahlgasten},Preis zimmer:{zimmer.preis},Farbe zimmer:{zimmer.farbe},Meerblick zimmer:{zimmer.meerblick}')

    def loschungzimmer(self,x):
        for i,zimmer in enumerate(self.zimmernliste):
            if zimmer.nummer == x:
                self.zimmernliste.pop(i)

    def filterzimmer(self,preis,meer):
        liste = list(filter(lambda zimmer: zimmer.preis <= preis , self.zimmernliste))
        if meer == "Ya":
            liste = list(filter(lambda zimmer : (zimmer.preis <= preis and zimmer.meerblick == meer),liste))
            print("Zimmer mit preis billiger als:", preis, "und Meerblick: Ya")
            for i in liste:
                 print(f'Zimmer nummer:{i.nummer},Anzahlgasten:{i.anzahlgasten},Zimmer preis:{i.preis},Zimmer farbe:{i.farbe},Zimmer meerblick:{i.meerblick}')
        elif meer =="Nein":
            liste = list(filter(lambda zimmer: (zimmer.preis <= preis and zimmer.meerblick == meer), liste))
            print("Zimmer mit preis billiger als:", preis, "und Meerblick: Nein")
            for i in liste:
                print(f'Zimmer nummer:{i.nummer},Anzahlgasten:{i.anzahlgasten},Zimmer preis:{i.preis},Zimmer farbe:{i.farbe},Zimmer meerblick:{i.meerblick}')
        else:
            print("Schreib für Meerblick:Ya/Nein")

    def find(self,z):
        for i,coc in enumerate(self.zimmernliste):
            if coc.nummer == z.nummer:
                return self.zimmernliste[i]

def zimmernmenu(list2):
    while True:
        print("""
            1-addzimmern
            2-aktualisierenpreis
            3-zimmeranzeige
            4-loschungzimmer
            5-exit
            """)
        opt = int(input("opt="))
        if opt==1:
            nummer = input("nummer:")
            anzahlgasten = int(input("anzahlgasten:"))
            preis = input("preis:")
            farbe = input("farbe:")
            meerblick = input("Ya/Nein:meerblick:")
            z1 = Zimmern(nummer,anzahlgasten,preis,farbe,meerblick)
            list2.addZimmern(z1)
        if opt==2:
            num = input("nummer:")
            neu = input("neupreis:")
            list2.aktualisierenpreis(num,neu)
        if opt==3:
            list2.zimmeranzeige()
        pickle.dump(list2, open("zimmern.txt", "wb"))
        if opt==4:
            num = input("nummer:")
            list2.loschungzimmer(num)
        if opt==5:
            return 0




