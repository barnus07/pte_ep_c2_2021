def terfogat_db_1(a,b,c):
    terfogat = a*b*c
    print("A hasáb doboz térfogata: ",terfogat)
def terfogat_db_2(a):
    terfogat = a**3
    print("A kocka alakú doboz térfogata: ",terfogat)

try:
    ver = ""
    while ver != "kocka" or ver != "hasáb":
        ver = input("A doboz kocka vagy hasáb?\n")
        if ver != "kocka" and ver != "hasáb":
            print("nem jó válasz")

        if ver == "kocka":
            a = int(input("ajda meg a doboz a oldalát: "))
            terfogat_db_2(a)
        elif ver == "hasáb":
            a = int(input("ajda meg a doboz a oldalát: "))
            b = int(input("adja meg a doboz b oldalát: "))
            c = int(input("adja ameg a doboz c oldalát: "))
            terfogat_db_1(a,b,c)
        contin = input("Szeretné folytatni? igen/nem:\t")
        if contin == "igen":
            continue
        elif contin == "nem":
            print("kilépett")
            break
except ValueError:
    print("nem megfelelő értéket vagy választ adott meg.")