from easygui import *

user_response = msgbox("Hello there", title="Hello", ok_button="Hi")
print(user_response)

flavor = buttonbox("what is your favourite ice cream flavor?", title="Icecream",
                           choices=['Vanilla', 'Chocolate', 'Strawberry'],
                           default_choice="Vanilla")
msgbox("You picked "+flavor)
flavor = choicebox("What is your favourite ice cream flavor?", title="Icecream2",
                            choices=['Vanilla', 'Chocolate', 'Strawberry'], preselect=1)
msgbox("You picked "+flavor)
flavor = enterbox("what is your favourite ice cream flavor?", title="Icecream3", default="körte",)
if flavor is not None:
    msgbox("You picked: "+ flavor)
else:
    print("Cancel gombra nyomott a felhasználó.")
    msgbox("Viszlát",)