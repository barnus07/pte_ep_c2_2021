import random


def haromszog(a,b,c):
       if a == b or b == c or c == a:
           print("Egyenlőszárú háromszög")
       else:
           print("Általános")

       if a+b == c or c+b == a or a+c == b:
           print("Derékszögű")

aoldal = input("adja meg a háromszög a oldalát")
boldal = input("adja meg a háromszög b oldalát")
coldal = input("adja meg a háromszög c oldalát")
haromszog(aoldal,boldal,coldal)

point = float(input("Adja meg a pontszámot:"))
if point >= 85:
    print("jeles")
elif point >= 70:
    print("jó")
elif point >=55:
    print("közepes")
elif point >=40:
    print("elégséges")
elif point < 40:
    print("eggyes")

erdemjegyek =[]
invalid = False
max = 1
min = 0
avg = 0
summ = 0
while not invalid:
    try:
        erdemjegy = int(input("A következő hallható érdemjegye:"))
        if erdemjegyek >=1 and erdemjegyek <=5:
            erdemjegyek.append(erdemjegy)
            if min > erdemjegy:
                min = erdemjegy
            if max < erdemjegy:
                max = erdemjegy
            summ += erdemjegy
            avg = summ/sum
    except ValueError:
        invalid = True
        print("nem megfelelő érték")
