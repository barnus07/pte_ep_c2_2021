import random

raw_input_data = input("Adj meg számot: ")
try:
    number = int(raw_input_data)
    if number < 10:
        print("Ez a szám kisebb, mint 10.")
    else:
        print("Ez a szám nagyobb vagy egyenlő 10-zel.")
    if number > 100:
        print("Ez a szám nagyobb, mint 100.")
    else:
        print("Ez a szám nem nagyobb, mint 100.")

    if number % 2 > 0:
        print("A szám páratlan.")
    else:
        print("A szám páros.")

    number2 = 101
    if number % number2 == 0:
        print("A", number2, "osztója a", number)
    else:
        if number2 % number == 0:
            print("A", number, "osztója a", number2)
        else:
            print("Egyik sem osztója a másiknak")
except ValueError:
    print("De én egy számot kértem!")

str = "alma."
if str[0] == str[-1]:
    print("Az első és az utolsó karakter megegyezik.")
else:
    print("Az első és az utolsó karakter nem egyezik meg.")

number = -30
if number > 0:
    print("pozitív")
else:
    if number < 0:
        print("negatív")
    else:
        print("nulla")

if number > 0:
    print("pozitív")
elif number < 0:
    print("negatív")
else:
    print("nulla")

str = "Alma"
if str[0].isupper():
    print("Nagybetűvel kezdődik.")
else:
    print("Nem nagybetűvel kezdődik.")

if str[0] == str[0].upper():
    print("Nagybetűvel kezdődik.")
else:
    print("Nem nagybetűvel kezdődik.")

str2 = "almafa"
str = "almafszár"
if str[0:5] == str2[0:5]:
    print("Az első 5 karakter azonos.")
else:
    print("Nem azonos az első 5 karakter.")

number = 17
if number >= 3 and number < 17:
    print("Beleesik a szám a [3, 17) intervallumba.")
else:
    print("A szám nem esik bele a [3, 17) intervallumba.")

a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
print(a, b, c)
if a + b > c and a + c > b and b + c > a:
    print("Lehet ezen oldalhosszakkal háromszöget szerkeszteni.")
else:
    print("Nem lehet ezen oldalhosszakkal háromszöget szerkeszteni.")

if a >= b and a >= c:
    print("Az a változó értéke a legnagyobb.")
    if b >= c:
        print("A c változó értéke a legkisebb.")
    else:
        print("A b változó értéke a legkisebb.")
else:
    if b >= c:
        print("A b változó értéke a legnagyobb.")
        if a >= c:
            print("A c változó értéke a legkisebb.")
        else:
            print("Az a változó értéke a legkisebb.")
    else:
        print("A c változó értéke a legnagyobb.")
        if a >= b:
            print("A b változó értéke a legkisebb.")
        else:
            print("Az a változó értéke a legkisebb.")


if a >= b and a >= c and b >= c:
    print("Az a változó értéke a legnagyobb.")
    print("A c változó értéke a legkisebb.")
elif a >= b and a >= c and c >= b:
    print("Az a változó értéke a legnagyobb.")
    print("A b változó értéke a legkisebb.")
elif b >= a and b >= c and c >= a:
    print("A b változó értéke a legnagyobb.")
    print("Az a változó értéke a legkisebb.")
elif b >= a and b >= c and a >= c:
    print("A b változó értéke a legnagyobb.")
    print("A c változó értéke a legkisebb.")
elif c >= a and c >= b and a >= b:
    print("A c változó értéke a legnagyobb.")
    print("A b változó értéke a legkisebb.")
else:
    print("A c változó értéke a legnagyobb.")
    print("Az a változó értéke a legkisebb.")

character = "."
vowels = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
numbers = "0123456789"
ponctuation_marks = ",.;:?"
if vowels.find(character) >= 0:
    print("magánhangzó")
elif numbers.find(character) >= 0:
    print("számjegy")
elif ponctuation_marks.find(character) >= 0:
    print("írásjel")

number = 19
if number % 3 == 0 and number % 5 == 0:
    print("Osztható 3-mal is és 5-tel is")
elif number % 3 == 0:
    print("Csak 3-mal osztható")
elif number % 5 == 0:
    print("Csak 5-tel osztható")
else:
    print("Nem osztható sem 3-mal, sem 5-tel")

grade = random.randint(1, 5)
if grade == 5:
    print("kiváló")
elif grade == 4:
    print("jó")
elif grade == 3:
    print("közepes")
elif grade == 2:
    print("elégséges")
elif grade == 1:
    print("elégtelen")
else:
    print("nem megfelelő érték")

print(random.random())
