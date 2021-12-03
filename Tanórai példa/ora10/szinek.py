def beolvasas(filepath: str):
    szinek = {}
    try:
        fileobject = open(filepath, "r")
        for sor in fileobject:
            sor_adatai = sor.strip().split("\t")
            szinek[sor_adatai[1]] = (sor_adatai[3], sor_adatai[4], sor_adatai[5])
        fileobject.close()
    except FileNotFoundError:
        print("Nem találom a fájlt!")
    return szinek


szin_szotar = beolvasas("color.csv")
print(szin_szotar)
print(type(szin_szotar))

szin = "Narancs"
szin_szotar[szin] = ("0", "0", "0")
if szin in szin_szotar:
    print(szin_szotar[szin])
else:
    print("Nem tartalmazza a szótárunk a {} színt.".format(szin))
