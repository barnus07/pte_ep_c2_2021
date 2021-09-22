import math

print("1. feladat:")
r = int(input("Adja meg a kör sugarát:"))
v = (4*(math.pow(r, 3)*math.pi))/3
print("A gömb térfogata:", v,)
print("2. feladat:")

p1 = []
x1 = int(input("adja meg a P1 x értékét:"))
y1 = int(input("adja meg a P1 y értékét:"))
p1 = x1, y1
p2 = []
x2 = int(input("adja meg a P2 x értékét:"))
y2 = int(input("adja meg a P2 y értékét:"))
p2 = x1, y1
d = math.sqrt((x1-x2)**2+(y1-y2)**2)
print("A két pont távolsága:", d)
print("3.feladat:")
s = ["almaszár", "kerékgyártó", "Flóra-pihenő", "Malomvölgy", "Misia", "Égervölgyi tó", "Tenkes", "Zsolnay-kút"]
i = 0

while 0 < len(s):
    if len(s[i]) > 10:
        print(s[i], len(s[i]))
    else:
        print(len(s[i]))
    i = i+1
    if i == len(s):
        break

print("5(4). feladat")
szoba = [75, 2] #1. szükséges festek 2. réteg
festek = [4300, 15] #1.festek ára, 2. m mennyisége
festek_ar = szoba[1]*(szoba[0]/festek[1])*festek[0]
print("A festék értéke:", festek_ar, "Ft")
festo = [13, 1, 2100] #1. munka idő 2. m-nyi haladás 3. munkabér
munka = round(((festo[0]*(szoba[1]*(szoba[0]/festo[1])))/60)*festo[2])
print("A festő munkájájának nettó összege:", munka, "Ft")
vegar = festek_ar + munka
print("A végösszeg Áfá-val:", round(vegar), "Ft")

