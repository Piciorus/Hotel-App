from Gäste import Gast
from Zimmern import *
from datetime import date
class Rezervierungen:
    def __init__(self,vorname,nachname,nummerzimmer,anfang,end):
        self.nummerzimmer = nummerzimmer
        self.anfang = anfang
        self.end = end
        self.vorname = vorname
        self.nachname = nachname

    def __str__(self):
        return f'Rezervierungen({self.vorname},{self.nachname},{self.nummerzimmer},{self.anfang},{self.end})'

class Rezlist:
    def __init__(self):
        self.rezlist = []

    def addRez(self,rez):
        self.rezlist.append(rez)

    def rezlistanzeige(self):
        for rez in self.rezlist:
            print(f'Vorname:{rez.vorname},Nachname:{rez.nachname},Nummerzimmer:{rez.nummerzimmer},DateAnfang:{rez.anfang},End:{rez.end}')


    def rezlistvonheute(self):
        d = date.today()
        print(d)
        for rez in self.rezlist:
            if str(rez.anfang) >= str(d):
                print(f'Vorname:{rez.vorname},Nachname:{rez.nachname},Nummerzimmer:{rez.nummerzimmer},DateAnfang:{rez.anfang},End:{rez.end}')

    def rezheutefrei(self):
        d = date.today()
        for rez in self.rezlist:
            if str(rez.anfang) > str(d) or str(rez.end) < str(d):
                print("Nummerzimmmer:"+ rez.nummerzimmer)

    def loschungrezlist(self,x):
        for i,rez in enumerate(self.rezlist):
            if rez.nummerzimmer == x:
                self.rezlist.pop(i)

def menurezervierungen(list2,list3):
    while True:
        print("""
        1-Macheinerezervierung
        2-rezeranzeige
        3-filterzimmer mit Preis and Meerblick
        4-rez loschung
        5-rezheutefrei
        6-exit
        """)
        opt = int(input("opt="))
        if opt==1:
            vorname = input("vorname: ")
            nachname = input("nachname: ")
            nummerzimmer = input("nummerzimmer:")
            anfang = input("anfang(yahr-monat-day):")
            end = input("end(yahr-monat-day):")
            list3.addRez(Rezervierungen(vorname,nachname,nummerzimmer,anfang,end))
        if opt==2:
            list3.rezlistvonheute()
        pickle.dump(list3, open("rezlist.txt", "wb"))
        if opt==3:
            preis = input("Zimmer billiger als preis: ")
            meer = input("Meerblick Ya/Nein: ")
            list2.filterzimmer(preis,meer)
        if opt==4:
            num = input("num=")
            list3.loschungrezlist(num)
        if opt==5:
            list3.rezheutefrei()
        pickle.dump(list3, open("rezlist.txt", "wb"))
        if opt==6:
            return 0






