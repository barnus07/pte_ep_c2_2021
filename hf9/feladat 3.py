szamok = []
def max(szamok):
    max = 0
    for i in range(len(szamok)):
        if szamok[i] > max:
            max = szamok[i]
    return max
for i in range(5):
    szam = int(input(f'adjon meg {i+1}. szamot:' ))
    szamok.append(szam)
print("A legnagyobb szám: ",max(szamok))