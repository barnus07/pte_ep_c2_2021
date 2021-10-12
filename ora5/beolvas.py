import random
with open("szamok.txt", "rt", encoding="UTF-8") as fajl:
    szoveg = [sor.strip() for sor in fajl]
    fajl.close()
    Eszam = []
    Mszam = []
    for sor in szoveg:
        Eszam.append(sor.split(".")[0])
        Mszam.append(sor.split(".")[1])

    sorvege = len(Eszam)
    i = int(input(f'Adja meg az indexet!(1-{sorvege})között:'))
    print(Eszam[i-1],Mszam[i-1])
    i = 0
    count = 1
    while 1 < 10:
        print(f'{count}.',Eszam[i], Mszam[i])
        i += 1
        count += 1
        if i == 10:
            break

    i = str(input("adja meg az első számot:"))
    sorszam = Eszam.index(i)
    print("Az első szám párja a",f'{Mszam[sorszam]}.')

    i = 0

    i = str(input("adja meg az második számot:"))
    sorszam = Mszam.index(i)
    print("Az második szám párja a", f'{Eszam[sorszam]}.')

