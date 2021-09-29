print("1. Feladat")
szoveg = "Programozni tanulok."
print(szoveg.upper())
print("2. Feladat")
ar = int(input("Adjon meg egy szamot:"))
if ar > 10000:
    ar = ar*0.8
else:
    ar = ar*0.9

print("A termek ára:", ar, "Ft")
print("3.feladat")
nem = str(input("Adja meg a nemét(Fiu = m Lány = f):"))
kor = 0
if nem == "f":
    kor = int(input("Adja meg az életkorát:"))
elif nem == "m":
    print("nem felel meg a focicsapat követelmények")
if kor > 12 or kor < 10:
    print("nem felel meg a focicsapat követelmények")
print("A játékos neme:", nem)
print("A játékos életkora:", kor)
if nem == "f" and kor == 10 or 11 or 12:
    print("A játékos megfelel a követelménynek!")







