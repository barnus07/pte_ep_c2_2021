with open("szamok.txt", "rt" , encoding="UTF-8") as fajl:
    szoveg = [sor.strip() for sor in fajl]
    fajl.close()
    Eszam = []
    Mszam = []
    for sor in szoveg:
        Eszam.append(sor.split(".")[0])
        Mszam.append(sor.split(".")[1])

    i = int(input("Adja meg az indexet!:"))
    print(Eszam[i],Mszam[i])





