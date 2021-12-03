print(chr(103))
print(chr(65))
print(ord("a"))
print(chr(ord("a")))
A = 65
chr(A)
print(int("A5", base=16))
lista = ["piros", "kék", "zöld"]
print(lista[0])
number = 123.235546
print(round(number))
print(round(number, 5))
print(round(number, 0))




a, b = 2, 4
if a == 4 or b != 4:
    print("nyert")
if a == 4 or b == 4:
    print("majdnem nyert")

number = 4
if number != 2:
    print("vesztett")
elif number == 3:
    print("kis türelmet kérek")
else:
    print("nyert")
