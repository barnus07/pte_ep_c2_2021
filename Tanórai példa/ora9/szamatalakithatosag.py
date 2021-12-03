def atalakithato_szamma(string):
    """Eldönti, hogy a string paramétert át lehet-e alakítani számmá. Ez akkor lehetséges, ha:
       \t- Az 1. karakter +, -, . vagy számjegy. Ha + vagy -, akkor legalább 2 karakterből kell, hogy álljon a string.
       \t- Legfeljebb egyetlen . karaktert tartalmaz.
       \t- Minden további karakter csak és kizárólag számjegy.
       A függvény tovább bővíthető: https://docs.python.org/3/library/functions.html#float.
    """
    result = False  # Arra az esetre, ha nem string típusú lenne az érték, amivel meghívják a függvényt.
    if type(string) == str:
        trimmed_string = string.strip()
        """Itt fordítjuk a logikát és azt feltételezzük, hogy a string alapértelemezetten átalakítható számmá. Azt 
           keressük, van-e olyan karakter, ami miatt ez nem lehetséges."""
        # Az 1. karakter +, - vagy számjegy. Ha + vagy -, akkor legalább 2 karakterből kell, hogy álljon a string.
        result = trimmed_string[0].isnumeric()\
                 or ((trimmed_string[0] == "+" or trimmed_string[0] == "-" or trimmed_string[0] == ".")
                      and len(trimmed_string) > 1)
        i = 1  # Az 1. karaktert már megvizsgáltuk, így elegendő a 2. karaktertől vizsgálni
        pontok_szama = 0
        while result and i < len(trimmed_string):
            if not trimmed_string[i].isnumeric():
                # Pont esetén meg kell győződni arról is, hogy számjegy áll előtte.
                if trimmed_string[i] != ".":
                    result = False
                else:
                    pontok_szama += 1
                    if pontok_szama > 1:
                        result = False
            i += 1
    return result


def atalakitas(string):
    if atalakithato_szamma(string):
        print(f"A '{string}' átalakítható számmá: {float(string)}")
    else:
        print(f"A '{string}' nem alakítható számmá.")

# Teszteljük az átalakítást:
atalakitas("nem szám")
atalakitas(" 10    ")
atalakitas("10")
atalakitas("-10")
atalakitas("+10")
atalakitas("1.0")
atalakitas(".5")
atalakitas("-6.")
atalakitas("123456789.987654321")
atalakitas("1.2.1")
atalakitas("1+5")
atalakitas("3-2")
atalakitas("1+")
atalakitas("3-")
atalakitas("        +.5")
atalakitas("-.6   ")