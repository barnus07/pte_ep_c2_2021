number = input("Kérem a számot: ")
if number.isnumeric():
    number = int(number)
    if number >= 0:
        print(number ** 0.5)
    else:
        print("Nem tudom meghatározni a négyzetgyökét.")
else:
    print("Nem tudom meghatározni a négyzetgyökét.")
