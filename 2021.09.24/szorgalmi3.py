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
if ido > 59 and ido < 3600:
    print(perc, "minutes and", ido%60, "seconds")
if ido > 3599 and ido < 86400 :
    print(ora, "hour,", perc%60, "minutes","and", ido%60, "seconds")
if ido > 86399 and ido < 31536000:
    print(nap, "day", ora%24, "hour,", perc%60, "minutes", "and", ido%60, "seconds")
if ido > 31535999:
    print(ev, "year,", nap%365, "day,", ora%24, "hour,", perc%60, "minutes and", ido%60, "seconds")