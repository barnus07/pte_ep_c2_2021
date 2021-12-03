sides = []
side_name = "a"
for i in range(3):
    side = 0
    while side == 0:
        try:
            side = float(input(f"Kérem adja meg a hárszömg {side_name} oldának értékét: "))
            if side > 0:
                if side_name == "a":
                    side_name = "b"
                else:
                    side_name = "c"
                sides.append(side)
            else:
                side = 0
                print("A háromszög oldala csak pozitív valós szám lehet.")
        except ValueError:
            print("A megadott érték nem megfelelő.")

if sides[0] + sides[1] <= sides[2] or sides[0] + sides[2] <= sides[1] or sides[2] + sides[1] <= sides[0]:
    print("Nem háromszög oldalai.")
else:
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 or \
        sides[0] ** 2 + sides[2] ** 2 == sides[1] ** 2 or \
        sides[2] ** 2 + sides[1] ** 2 == sides[0] ** 2:
        print("derékszögű")
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        print("egyenlőoldalú")
    elif sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1]:
        print("egyenlőszárú")
    else:
        print("általános")
