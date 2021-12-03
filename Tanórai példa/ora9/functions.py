import datetime
import time as time_module

def parose(szam):
    if type(szam) == int:
        if szam % 2 == 0:
            print("páros")
        else:
            print("páratlan")


def tipus(szam):
    if type(szam) == int or type(szam) == float:
        if szam == 0:
            print("A szám nulla.")
        if szam > 0:
            print("A szám pozitív.")
        if szam < 0:
            print("A szám negatív.")
    else:
        print("Nem egy szám.")


def parose2(szam):
    paros = False
    if type(szam) == int:
        if szam % 2 == 0:
            print("páros")
            paros = True
        else:
            print("páratlan")
    return paros


szam = 11
parose(szam)
print(parose(20))
print(parose("alma"))
print(parose2(szam))
print(parose2(20))
print(parose2("alma"))
tipus(0)
tipus(12)
tipus(-1.5)
tipus("Alma")

def time():
    print(datetime.datetime.now())


def wait(seconds):
    if type(seconds) == int:
        time()
        print(f"Várunk {seconds} másodpercet.")
        time_module.sleep(seconds)
        time()

time()
wait(1)
wait(10)
