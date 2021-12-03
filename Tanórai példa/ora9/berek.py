brutto_netto = 0.665

def netto(n):
    ertek = 0
    if type(n) == int or type(n) == float:
        ertek = n*brutto_netto
    return ertek

def brutto(n):
    ertek = 0
    if type(n)== int or type(n)== float:
        ertek = n / brutto_netto
    return ertek

print(netto(200000))
print(brutto(133000))
print(brutto(netto(200000)))
