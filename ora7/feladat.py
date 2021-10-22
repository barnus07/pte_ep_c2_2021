import math
from easygui import *
evszam_str = enterbox("Adjon meg egy évszámot")
try:
    evszam = int(evszam_str)
    if evszam%4 == 0:
        if evszam%100 == 0:
            if evszam % 400 == 0:
                msgbox("Ez az év szökőév:")
            else:
                msgbox("Ez az év nem szökőév")
        else:
            msgbox("Ez az év nem szökőév")
    else:
        msgbox("Ez az év nem szökőév")
except ValueError:
    print("nem megfeleő a szám")

