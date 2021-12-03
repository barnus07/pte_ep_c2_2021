import random
from easygui import *


title = "Számkitaláló"
number = random.randint(1, 100)
back = 6
msgbox("Szia!\nGondoltam egy számra 1 és 99 között. 6 próbálkozásod van eltalálni.",
       ok_button="Induljon a játék!", title=title)
won = False
hint = ""
while not won and back > 0:
    guess = enterbox(f"{hint} Még {back} próbálkozásod maradt.\nKérem a tipped:", title=title)
    if guess is not None:
        back -= 1
        try:
            guess_number = int(guess)
            if guess_number == number:
                msgbox("Gratulálok, nyertél {} lépésből".format(6 - back), title=title)
                won = True
            elif guess_number < number:
                hint = "Nagyobb számra gondoltam!"
            else:
                hint = "Kisebb számra gondoltam!"
        except ValueError:
            hint = "Hibás bemenet, vesztettél egy próbálkozást!"

if not won:
    msgbox("Sajnálom, vesztettél! Én a " + str(number) + " gondoltam.", title=title)
