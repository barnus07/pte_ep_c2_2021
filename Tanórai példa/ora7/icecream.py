from easygui import *


user_response = msgbox("Hello There!", title="Hello", ok_button="Hi", image="python_logo.png")
print(user_response)

flavor = buttonbox("What is your favorite ice cream flavor?", title="Icecream",
                           choices=['Vanilla', 'Chocolate', 'Strawberry', "Cherry"],
                           default_choice="Vanilla")
msgbox("You picked " + flavor)

flavor = choicebox("What is your favorite ice cream flavor?", title="Icecream2",
                   choices=['Vanilla', 'Chocolate', 'Strawberry', "Cherry"], preselect=1)
msgbox("You picked " + flavor)

flavor = enterbox("What is your favorite ice cream flavor?", title="Icecream3",
                  default="körte", image="python_logo.png")
if flavor is not None:
    msgbox("You picked " + flavor)
else:
    print("Cancel gombra nyomott a felhasználó.")
