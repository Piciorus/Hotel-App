from Gäste import Gastlist,Gast
from Zimmern import Zimmernliste,Zimmern
from Gemeinsame import Rezlist,Rezervierungen

def test():
    addGasttest()
    aktualisierennachnametest()
    loschunggasttest()
    addZimmerttest()
    aktualisierenpreistest()
    loschungzimmertest()
    addreztest()
    filterzimmertest()

def addGasttest():
    a = Gast("alex","andrei")
    assert a.vorname == "alex" and a.nachname == "andrei"

def aktualisierennachnametest():
    x = Gastlist()
    x.addGast(Gast("alex","andrei"))
    x.aktualisierennachname(Gast("alex","andrei"),Gast("alex","mihai"))
    assert x.find(Gast("alex","mihai"))

def loschunggasttest():
    y = Gastlist()
    y.addGast(Gast("alex","marian"))
    y.loschunggast(Gast("alex","marian"))
    assert not y.find(Gast("alex", "marian"))

def addZimmerttest():
    z = Zimmern("12","3","160","bleu","Ya")
    assert z.nummer == "12" and z.anzahlgasten == "3" and z.preis == "160" and z.farbe == "bleu" and z.meerblick == "Ya"

def aktualisierenpreistest():
    z = Zimmernliste()
    z.addZimmern(Zimmern("12","3","160","bleu","Ya"))
    z.aktualisierenpreis("160","200")
    assert z.find(Zimmern("12","3","200","bleu","Ya"))

def loschungzimmertest():
    z = Zimmernliste()
    z.addZimmern(Zimmern("12","3","160","bleu","Ya"))
    z.loschungzimmer("12")
    assert not z.find(Zimmern("12","3","160","bleu","Ya"))

def addreztest():
    r = Rezervierungen("al","al","8","2021-10-12","2021-10-14")
    assert r.vorname == "al" and r.nachname == "al" and r.nummerzimmer == "8" and r.anfang == "2021-10-12" and r.end == "2021-10-14"

def filterzimmertest():
    r = Zimmernliste()
    r.addZimmern(Zimmern("12","3","160","bleu","Ya"))
    r.addZimmern(Zimmern("13","3","60","rot","Nein"))
    r.addZimmern(Zimmern("14","3","100","gray","Ya"))
    r.filterzimmer("100","Nein")
    assert r.find(Zimmern("13","3","60","rot","Nein"))
