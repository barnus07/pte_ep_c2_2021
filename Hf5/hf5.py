with open("szamok.txt", "rt", encoding="UTF-8") as f:
    tartalom = [sor.strip() for sor in f]
    print("1. Feladat")
    sum = 0
    i = 0
    while(tartalom):
        print(tartalom[i])
        sum += len(tartalom[i])
        i += 1
        if i == len(tartalom):
            break
    print("A fájl sorainak száma",len(tartalom), "karakterek száma:",sum)
    print("2. Feladat")

with open("szorzotabla.txt", "wt") as f:
    szorzotabla = []
    for i in range(1, 11):
        for y in range(1, 11):
               f.write(str(i*y))
