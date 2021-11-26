import random
import time

def uppercase(szoveg: str) -> None:
    for karakter in szoveg:
        if karakter >= 'a' and karakter <= 'z':
            print(chr(ord(karakter)-ord('a')+ord("A")), end="")
        else:
            print(karakter,end="")

def harminc(hossz: int, letptek: int) -> None:
    for i in range(hossz//letptek):
        print(f'\n{random.randint(0,100)}')
        time.sleep(letptek)

def repeat(szoveg: str) -> None:
    repeat = []
    for i in range(len(szoveg)):
        if szoveg.count(szoveg[i]) >= 2:
            if repeat.__contains__(szoveg[i]):
                n = 0
            else:
                repeat.append(szoveg[i])
    print(f'\n{repeat}')

def kissebb(lista: list[float], limit: float)->int:
    kissebbek = 0
    for szam in lista:
        if szam < limit:
            kissebbek += 1
    return kissebbek

def primek(szam: int)-> None:
    maradek = szam
    oszto = 2
    while maradek > 1:
        if maradek % oszto == 0:
            maradek = maradek // oszto
            print(oszto)
        else:
            oszto += 1
