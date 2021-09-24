import math

ido = int(input("Adja meg az időt másodpercben:"))
perc = math.floor(ido/60)
ora = math.floor(perc/60)
nap = math.floor(ora/24)
ev = math.floor(nap/365)
if ido < 0:
    quit()
if ido == 0:
    print("Now")
if ido < 60:
    print(ido, "seconds")
if ido > 59 and ido < (60*60):
    print(perc, "minutes and", ido%60, "seconds")
if ido > ((60*60)-1) and ido < (60*60*24):
    print(ora, "hour,", perc%60, "minutes","and", ido%60, "seconds")
if ido > ((60*60*24)-1) and ido < (60*60*24*365):
    print(nap, "day", ora%24, "hour,", perc%60, "minutes", "and", ido%60, "seconds")
if ido > ((60*60*24*365)-1):
    print(ev, "year,", nap%365, "day,", ora%24, "hour,", perc%60, "minutes and", ido%60, "seconds")