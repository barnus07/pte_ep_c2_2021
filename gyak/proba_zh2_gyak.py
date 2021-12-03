from kepviselo_02 import Kepviselo
def beolvasas()->list:
    try:
        lista = []
        f = open("szavazatok.txt","r",encoding="UTF-8")
        for sor in f:
            sor = sor.strip().split()
            sor[0] = int(sor[0])
            sor[1] = int(sor[1])
            lista.append(sor)
        return lista
        f.close()
    except FileNotFoundError:
        print("Hiba!")


def osztaly(lista: list) -> list:

    kepviselok = []

    for sor in lista:

        if sor[4] == "-":
            k = Kepviselo(sor[0],sor[1],sor[2],sor[3],sor[4],"Független")
            kepviselok.append(k)
        if sor[4] == "HEP":
            k = Kepviselo(sor[0], sor[1], sor[2], sor[3], sor[4], "Húsevők pártja")
            kepviselok.append(k)
        if sor[4] == "ZEP":
            k = Kepviselo(sor[0], sor[1], sor[2], sor[3], sor[4], "Zöldségevők pártja")
            kepviselok.append(k)
        if sor[4] == "GYEP":
            k = Kepviselo(sor[0], sor[1], sor[2], sor[3], sor[4], "Gyümölcsevők pártja")
            kepviselok.append(k)
        if sor[4] == "TISZ":
            k = Kepviselo(sor[0], sor[1], sor[2], sor[3], sor[4], "Tejivők szövetsége")
            kepviselok.append(k)

    return kepviselok

#Teszt
lista = beolvasas()
lista2 = osztaly(lista)
#print(lista)
#print(lista2)

def masodik(lista: list):

    print(f"A képviselők száma: {len(lista)}")
#masodik(lista2)

def harmadik(lista: list):
    try:
        elonev = input("Adja meg a képviselő első nevét(pl.:Gipsz): ")
        utonev = input("Adja meg az utónevét(pl.:Jakab)")
    except ValueError:
        print("Hiba!")
    #elonev = elonev.lower()
    #utonev = utonev.lower()
    benne = False
    for sor in lista:
        if sor.nev1.lower() == elonev.lower() and sor.nev2.lower() == utonev.lower():
            print(f"{elonev} {utonev} képviselőnek {sor.votes} szavazata van")
            benne = True
            break
    if benne == False:
        print("Ilyen képviselő nincs")

#harmadik(lista2)

def negyedik(lista: list):
    jogosultak = 12345
    szavazatok = 0
    for sor in lista:
        szavazatok += sor.votes
    print("Az összes szavazat:",szavazatok)
    print("Az összes szavazathoz képest: ",round((szavazatok/jogosultak)*100,2),"%",sep="")

#negyedik(lista2)

def otodik(lista: list):
    sum_votes = 0
    for sor in lista:
        sum_votes += sor.votes
    partok = [0,0,0,0,0]

    for sor in lista:
        if sor.rovpart == "-":
            partok[0] += sor.votes
        if sor.rovpart == "HEP":
            partok[1] += sor.votes
        if sor.rovpart == "ZEP":
            partok[2] += sor.votes
        if sor.rovpart == "TISZ":
            partok[3] += sor.votes
        if sor.rovpart == "GYEP":
            partok[4] += sor.votes


    print("GYEP - ",round((partok[4]/sum_votes)*100,2),"%",sep="")
    print("TISZ - ", round((partok[3] / sum_votes) * 100, 2), "%", sep="")
    print("ZEP - ", round((partok[2] / sum_votes) * 100, 2), "%", sep="")
    print("HEP - ", round((partok[1] / sum_votes) * 100, 2), "%", sep="")
    print("Függetlenek - ", round((partok[0] / sum_votes) * 100, 2), "%", sep="")


#otodik(lista2)

def hatodik(lista: list):
    max_votes = 0
    for sor in lista:
        if sor.votes > max_votes:
            max_votes = sor.votes
    for sor in lista:
        if sor.votes == max_votes:
            print(sor.votes," - ",sor.nev1,sor.nev2,"-",sor.part)
#hatodik(lista2)

def hetedik(lista:list):
    try:
        f = open("kepviselok_2.txt", "w", encoding="UTF-8")
        keruletek = []
        for sor in lista:
            if sor.ker not in keruletek:
                keruletek.append(sor.ker)
        keruletek.sort()

        for elem in keruletek:
                    maxpart = 0
                    for sor in lista:
                        if elem == sor.ker:
                            if sor.votes > maxpart:
                                maxpart = sor.votes
                    for sor in lista:
                        if maxpart == sor.votes:
                            f.write(str(elem)+"-"+str(maxpart)+"-"+sor.nev1+" "+sor.nev2+"-"+sor.part+"\n")
                            break
        print("A file elkészítve")
        f.close()
    except FileExistsError:
        print("Hiba!")


#hetedik(lista2)




