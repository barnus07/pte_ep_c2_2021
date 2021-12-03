filepath = input("Kérem adja meg a fájl nevét: ")
try:
    file = open(filepath, "a+", encoding="UTF-8")
    menu = -1
    while menu != "0":
        menu = input("Kérem válasszon a következő műveletek közül:"
                     "\n\t1 - új sorok rögzítése\n\t2 - tartalom kiíratása\n\t0 - kilépés\n")
        if menu == "1":
            print("Kérem adja meg a rögzíteni kívánt sorokat:")
            row = input()
            while row != "":
                file.write(row + "\n")
                file.flush()
                row = input()
        elif menu == "2":
            file.seek(0, 0)
            print(file.read())
    file.close()
except OSError:
    print("Probléma merült fel a fájl megnyitása közben.")
