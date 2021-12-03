"""
Egy kertben egész méterenként ültetünk fákat. Írjon programot,
amiben a fákat koordinátáikkal és típusukkal egy szótárban tárolja és
 a felhasználónak lehetősége van:
- Új fát rögzíteni a hely és fajta megadásával. Pl.: (1, 2) - "nyárfa".
- Lekérdezni az adott koordinátán lévő fa fajtáját.
- Kilistázni a kertben lévő fák koordinátáit és fajtáit.
- Kilistázni a kertben lévő fák fajtáját. Ha több azonos fajta van, akkor csak egyet írjon ki!
- Kilistázni, hogy a kert mely pontjain vannak fák.
- A fajta alapján kilistázni, mely koordinátákon vannak ilyen fák.
"""

def menu_opciok():
    print("Kérem válasszon az alábbi menüpontok közül:\n\t0 - Kilépés"
          "\n\t1 - Új fa regisztrálása\n\t2 - Adott koordinátán lévő fafajta kiíratása"
          "\n\t3 - Fák és koordináták listázása\n\t4 - Fafajták listázása"
          "\n\t6 - Fafajta alapján koordináták listázása")


def egesz_szam_bekerese(koordinata: str) -> int:
    szam = ""
    while szam == "":
        try:
            szam = int(input(f"Kérem adja meg {koordinata} koordinátát: "))
        except ValueError:
            print("Nem pozitív egész számot adott meg.")
    return szam


def fa_regisztralasa(fak: dict):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely not in fak:
        fafajta = input("Kérem adja meg a fa fajtáját: ")
        fak[hely] = fafajta
        print("Sikeres regisztráció.")
    else:
        print("Itt már áll egy fa, nem regisztrálhat új fát ide.")


def fafajta_lekerdezese(fak: dict):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print("Ezen a koordinátán {} fajta fa áll.".format(fak[hely]))
    else:
        print("Ezen koordinátán nincs fa.")


def fafajtak_kiiratasa(fak: dict):
    fajtak = []
    for i in fak:
        if fak[i] not in fajtak:
            print(fak[i])
            fajtak.append(fak[i])


def fafatja_koordinatai(fak: dict):
    fajta = input("Milyen fafajta koordinátákra kíváncsi: ")
    koordinatak = ""
    for i in fak:
        if fak[i] == fajta:
            koordinatak += str(i)
    if koordinatak == "":
        print("Nincs ilyen fafajta a kertben.")
    else:
        print("Ezen koordinátákon vannak {} fák: {}".format(fajta, koordinatak))


def szotar_kiiratasa(filepath: str, fak: dict):
    file = open(filepath, "w")
    for i in fak:
        file.write(str(i[0]))
        file.write("\t")
        file.write(str(i[1]))
        file.write("\t")
        file.write(fak[i])
        file.write("\n")
    file.close()


def szotar_betoltese(filepath: str):
    szotar = {}
    file = open(filepath, "r")
    for sor in file:
        fa_adat = sor.strip().split("\t")
        szotar[(int(fa_adat[0]), int(fa_adat[1]))] = fa_adat[2]
    file.close()
    return szotar


menu = ""
fak_szotar_filepath = "fak.csv"
fak = szotar_betoltese(fak_szotar_filepath)
while menu != "0":
    menu_opciok()
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
        fafatja_koordinatai(fak)
szotar_kiiratasa(fak_szotar_filepath, fak)

