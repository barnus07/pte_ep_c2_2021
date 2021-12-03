menu_command = ""
while menu_command != "0":
    menu_command = input("Kérlek válassz a menüpontok közül:\n\t0 - kilépés\n\t1 - összeadás\n")
    if menu_command == "1":
        is_number = False
        a = 0
        b = 0
        while not is_number:
            try:
                a = float(input("Kérlek add meg az első számot: "))
                is_number = True
            except ValueError:
                print("A megadott érték nem szám.")
        is_number = False
        while not is_number:
            try:
                b = float(input("Kérlek add meg a második számot: "))
                is_number = True
            except ValueError:
                print("A megadott érték nem szám.")
        print("A két szám összege:", a + b)
print("Viszlát!")
