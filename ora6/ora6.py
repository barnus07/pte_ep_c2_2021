import random
print(chr(103))
print(chr(65))
print(ord("a"))
print(chr(ord("a")))
A = 65
print(chr(A))
print(int("A5", base=16))
lista = ["alma", "tojás", "sajt"]
print(lista[0])
numbers = 123.235546
print(round(numbers))
print(round(numbers, 5))
print(round(numbers, 0))
a, b = 2, 4
km = int(input("adjon meg egy értéket Km/h-ban:"))
atvaltas = 3.6
ms = km*atvaltas
print("Km/h--->M/s:",ms)
paratlanszamok = []
parosszamok = []
szamok = []
i = 1
while i<=200:
    szamok.append(random.randint(-100, 100))
    i +=1
    if i == 200:
        break
i = 0
while i< len(szamok):
    if szamok[i]%2 == 0:
        parosszamok.append(szamok[i])
    else:
        paratlanszamok.append(szamok[i])
    i += 1
    if i == len(szamok):
        break
print(parosszamok)
print(paratlanszamok)
ertekek = []
ertek = 0
while ertek != "":
    ertek = input("adjon meg egy értéket:")
    ertekek.append(ertek)
    if ertek == "":
        ertekek.remove(ertekek[len(ertekek)-1])
        break
print(ertekek)
szam = []
for i in range(20):
    szam.append(random.randint(1, 100))
min = min(szam)
max = max(szam)
print(szam)
print(min,max)



