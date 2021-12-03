# Feladatkiírás

Írj programot, ami a másodperceket emberbarát formátummá alakít:
- A program bemenete egy nem negatív egész szám.
- Amennyiben a bement értéke 0, írja ki, hogy "now", ellenben a megfelelő kombinációban tartalmazza a "years", "days",
"hours", "minutes" és "seconds" szavakat és értékeket.
- Az egyszerűség kedvéért tekintsük az éveket fixen 365 naposnak.
- Az egységek az angol nyelvtani szabályok szerint egyes számban szerepeljenek, ha az értékük 1 és többes számban, 
ha ettől nagyobb.
- A komponensek ", " elválasztással legyenek elválasztva egymástól, kivéve az utolsó 2 komponenst, azok " and " 
karakterlánccal.
- Az egységnek csökkenő sorrendben kell megjelenniük a képernyőn.
- Egy egység egyetlen egyszer szerepelhet.
- Csak azon időegységeket írja ki a program, amelyek nem 0 értékkel rendelkeznek.
- Az összes lehetséges átváltást el kell végezni.

# Példák, tesztesetek

Bemenet   | Elvárt kimenet
----------|---------------
0         | now
1         | 1 second
2         | 2 seconds
59        | 59 seconds
60        | 1 minute
61        | 1 minute and 1 second
119       | 1 minute and 59 seconds
121       | 2 minutes and 1 second
3 690     | 1 hour, 1 minute and 30 seconds
31 700 000| 1 year, 1 day, 21 hours, 33 minutes and 20 seconds
65 000 000| 2 years, 22 days, 7 hours, 33 minutes and 20 seconds
