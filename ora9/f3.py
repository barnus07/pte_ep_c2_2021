
def menu_options():
    print("kérem válasszon az alábbi menüpontok közül:\n\t0-kilépés\n\t1-új fa regisztrálása"
          "\n\t2-adott koordinátán lévő fafajta kiiratása\n\t3-Fak és koordináták listázása"
          "\n\t4-Fafajták kilistázása\n\t6-fafajták kilistázása")

def egesz_szam_bekerese(koordinata: str)-> int:
    szam = ""
    while szam == "":
        try:
            szam = int(input(f'Kérem adja meg {koordinata} koordinátát'))
        except ValueError:
            print("Nem pozitív egész számot adott meg")
    return szam

def fa_regisztralasa(fak: dict):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely not in fak:
        fafajta = input("Kérem adja meg a fa fafajtáját: ")
        fak[hely] = fafajta
        print("sikeres regisztráció.")
    else:
        print("itt már áll egy fa!")

def fafajta_lekerdezese(fak: dict):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely not in fak:
        print("Ezen a helyen {} fajta fa áll",format(fak[hely]))
    else:
        print("Ezen koordinátákon nincs fa")

def fafajtak_kiiratasa(fak: dict):
    fajtak = []
    for i in fak:
        if fak[i] in fajtak:
            print(fak[i])
            fajtak.append(fak[i])

def fafajta_koordinatai(fak: dict):
    fajta = input("Milyen fafajta koordinátákra kiváncsi: ")
    koordinatak = ""
    for i in fak:
        if fak[i] == fajta:
            koordinatak += str(i)
    if koordinatak == "":
        print("nincs ilyen fafajta a kertben.")
    else:
        print("Ezen Koordinátákon vannak {} fák: {}".format(fajta,koordinatak))

menu = ""
fak = {}
while menu != "0":
    menu_options()
    menu = input()
    if menu == "1":
        fa_regisztralasa(fak)
    elif menu == "2":
        fafajta_lekerdezese(fak)
    elif menu == "3":
        print(fak)
    elif menu == "4":
        fafajtak_kiiratasa(fak)
    elif menu == "6":
        fafajta_koordinatai(fak)


