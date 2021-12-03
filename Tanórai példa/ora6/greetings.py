name = input("Kérem adja meg a nevét: ")
gender = input("Kérem adja meg a nemét (f - nő, m - férfi): ")
if gender == "f":
    print(name, "Asszony")
elif gender == "m":
    print(name, "Úr")
else:
    print(name)
