
with open("phonebook.txt", "rt", encoding="UTF-8") as fajl:
    sor = [sor.strip() for sor in fajl]
    fajl.close()
    print(sor)
    Vnev = []
    Knev = []
    Lak = []
    Laksz = []
    Number = []
    Date = []
    i = 0
    while i< len(sor):
        print(sor[i].split("  "))
        Vnev.append(sor[i].split("  ")[0])
        Knev.append(sor[i].split("  ")[1])
        Lak.append(sor[i].split("  ")[2])
        Laksz.append(sor[i].split("  ")[3])
        Number.append(sor[i].split("  ")[4])
        Date.append(sor[i].split("  ")[5])
        i += 1
        if i == "":
            break
    sorok = int(input("Adja meg a cserélendő sort vagy -1 lenymásával begejezi:"))
    while sorok:
        if sorok == -1:
            break
        tipus = str(input("Adja meg a tipust (Vezetéknév, Keresztnév, Lakcím, Körzet,Telszam,Datum:)"))
        if tipus == "Vezetéknév":
            print(sor[sorok])
            valtozas = str(input("Adjon meg egy vezeteknevet: "))
            Vnev[sorok] = valtozas
        if tipus == "Keresztnév":
            print(sor[sorok])
            valtozas = str(input("Adjon meg egy Keresztnevet: "))
            Vnev[sorok] = valtozas
        if tipus == "Lakcím":
            print(sor[sorok])
            valtozas = str(input("Adjon meg egy Lakcímet: "))
            Vnev[sorok] = valtozas
        if tipus == "Körzet":
            print(sor[sorok])
            valtozas = str(input("Adjon meg egy Körzetet: "))
            Vnev[sorok] = valtozas
        if tipus == "Telszam":
            print(sor[sorok])
            valtozas = str(input("Adjon meg egy Telszamot: "))
            Vnev[sorok] = valtozas
        if tipus == "Datum":
            print(sor[sorok])
            valtozas = str(input("Adjon meg egy Datumot: "))
            Vnev[sorok] = valtozas
        sorok = int(input("Adja meg a cserélendő sort vagy -1 lenymásával begejezi:"))
    print(sor)
