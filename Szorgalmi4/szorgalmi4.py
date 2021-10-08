
Startsystem = int(input("Adja meg a kiindulási rendszert (2,8,10,16):"))
Goalsystem = int(input("Adja meg a célrendszert(2,8,10,16):"))
szam = input("Adjon meg egy számot:")
if int(szam) > 0:
    print("good number")
elif int(szam) < 0:
    print("wrong number")
    quit()
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

if Startsystem == 2 and Goalsystem == 8:
    szam = int(szam, 2)
    print(octal(szam))

if Startsystem == 2 and Goalsystem == 10:
    szam = int(szam, 2)
    print(szam)

if Startsystem == 2 and Goalsystem == 16:
    szam = int(szam, 2)
    print(hexadecimal(szam))

if Startsystem == 8 and Goalsystem == 2:
    szam = int(szam, 8)
    print(binary(szam))

if Startsystem == 8 and Goalsystem == 10:
    szam = int(szam, 8)
    print(szam)

if Startsystem == 8 and Goalsystem == 16:
    szam = int(szam, 8)
    print(hexadecimal(szam))

if Startsystem == 10 and Goalsystem == 2:
    szam = int(szam, 10)
    print(binary(szam))

if Startsystem == 10 and Goalsystem == 8:
    szam = int(szam, 10)
    print(octal(szam))

if Startsystem == 10 and Goalsystem == 16:
    szam = int(szam, 10)
    print(hexadecimal(szam))

if Startsystem == 16 and Goalsystem == 2:
    szam = int(szam, 16)
    print(binary(szam))

if Startsystem == 16 and Goalsystem == 8:
    szam = int(szam, 16)
    print(octal(szam))

if Startsystem == 16 and Goalsystem == 10:
    szam = int(szam, 16)
    print(szam)