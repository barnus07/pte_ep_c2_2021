import random
from easygui import *
buttonbox("Számkitalálós játék", choices=['induljon a játék!'])
msgbox("A szám (1-99) között fog szerepelni! és 6 lehetősége lesz a játékosnak")
szam = random.randint(1,99)
i = 0
try:
    tipp = enterbox(f'adjon meg egy tippet:{i+6}')
    while i<=5:
        index = 5-i
        if int(tipp) == szam:
            if tipp is None:
                msgbox('A játékos nem adott meg egy számot')
            elif int(tipp) < 1:
                msgbox("Az adott szám kissebb mint 1")
            elif int(tipp) > 99:
                msgbox("Az adott szám nagyobb mint 99")
            msgbox("nyert")
        elif i == 5:
            msgbox("maga nem nyert")
        else:
            msgbox("nemnyert")
            tipp = enterbox(f'adjon meg egy tippet: Lehetőségek száma:{index}')
        i+=1
    msgbox("A kitalált szám: "+str(szam))
except ValueError:
    msgbox("nem jó a szám")


