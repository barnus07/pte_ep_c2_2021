import easygui


input_str = easygui.enterbox("Adja meg az évszámot:", title="Adatbekérés")
eredmeny_title = "Eredmény"
try:
    ev = int(input_str)
    if ev % 4 == 0:
        if ev % 100 == 0:
            if ev % 400 == 0:
                easygui.msgbox("Ez az év szökőév, mert 400-zal osztható.", title=eredmeny_title)
            else:
                easygui.msgbox("Ez az év nem szökőév, mert 100-zal osztható, de 400-zal nem.",
                               title=eredmeny_title)
        else:
            easygui.msgbox("Ez az év szökőév, mert 4-gyel osztható, de 100-zal nem.", title=eredmeny_title)
    else:
        easygui.msgbox("Ez az év nem szökőév, mert nem osztható 4-gyel.",
                       title=eredmeny_title)
except ValueError:
    easygui.msgbox("Hibás bemenet.", title="Hiba")
