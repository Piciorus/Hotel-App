from Gäste import gastmenu
from Zimmern import *
from Gemeinsame import menurezervierungen
from testing import test

def menu():
    list1 = pickle.load(open("Gästen.txt", "rb"))
    list2 = pickle.load(open("zimmern.txt", "rb"))
    list3 = pickle.load(open("rezlist.txt", "rb"))
    while True:
        print("""
        1-gastmenu
        2-zimmernmenu
        3-gemeinsamemenu
        4-exit
        """)
        opt = int(input("opt="))
        if opt==1:
            gastmenu(list1)
        if opt==2:
            zimmernmenu(list2)
        if opt==3:
            menurezervierungen(list2,list3)
        if opt==4:
            return 0


menu()
test()




