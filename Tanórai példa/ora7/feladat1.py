import easygui
import math


diameter_str = easygui.enterbox("A kör átmérője cm-ben:", title="Adatbekérés")
try:
    diameter = float(diameter_str)
    if diameter > 0:
        radius = diameter / 2
        kerulet = 2 * radius * math.pi
        terulet = radius ** 2 * math.pi
        easygui.msgbox(f"A {diameter} cm átmérőjű kör kerülete {kerulet:.3f} cm,"
                       f" területe pedig {terulet:.3f} cm^2.")
    else:
        easygui.msgbox("Nem megfelelő átmérő.", title="Hiba")
except ValueError:
    easygui.msgbox("Nem megfelelő átmérő.", title="Hiba")
