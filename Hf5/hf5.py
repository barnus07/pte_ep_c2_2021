import math

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
               szorzotabla.append(i*y)
    i = 0
    while i < len(szorzotabla):
        f.write(str(szorzotabla[i])+"\t")
        i += 1
        if i%10 == 0:
            f.write('\n')
        if i == len(szorzotabla):
            break



with open("szamrendszer.txt", "wt", encoding="UTF-8") as f:
    szam = int(input("adjon meg egy szamot:"))
    def binary(n):
        s =bin(n)
        s1 = int(s[2:])
        return s1

    def octal(n):
        s = oct(n)
        s1 = int(s[2:])
        return s1

    def hexadecimal(n):
        s = hex(n)
        s1 = str(s[2:])
        return s1

    binaris = binary(szam)
    hexadecimalis = hexadecimal(szam)
    oktalis = octal(szam)
    f.write("A szám 2-es számrendszerben:\t" + str(binaris) + "\n")
    f.write("A szám 8-as számrendszerben:\t" + str(oktalis) + "\n")
    f.write("A szám 16-os számrendszerben:\t" + str(hexadecimalis)+ "\n")