import math

nevek = []
i= 0
while i<5:
    nev = str(input("nev: "))
    nevek.append(nev)
    i +=1
    if i == 5:
        break
for i in range(0,5):
    print(nevek[i],i)
for i in range(0,5):
    nevek.sort()
    print(nevek[i])
print(nevek[3])
ii = int(input("adjon meg egy sorszámot"))
csnev = str(input("adjon meg a cserélendő nevet:"))
nevek[ii] = csnev
for i in range(0,5):
    print(nevek[i])
