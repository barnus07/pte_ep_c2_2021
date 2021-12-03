pontszam = ""
while type(pontszam) == type(""):
    try:
        pontszam = float(input("Kérem adja meg a hallgató pontszámát: "))
    except ValueError:
        print("Nem megfelelő érték.")

if pontszam < 0 or pontszam > 100:
    print("Nem megfelelő érték.")
elif pontszam >= 85:
    print("jeles (5)")
elif pontszam >= 70:
    print("jó (4)")
elif pontszam >= 55:
    print("közepes (3)")
elif pontszam >= 40:
    print("elégséges (2)")
else:
    print("elgételen (1)")

