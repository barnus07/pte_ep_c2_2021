age_lower_limit = 10
age_upper_limit = 12
gender_limit = "f"
error_message = "Sajnálom, de csak 10-12 éves lányok játszhatnak a csapatban."
gender = input("Adja meg a gyermek nemét (m - fiú, f - lány): ")
if gender == gender_limit:
    try:
        age = int(input("Adja meg a gyermek korát: "))
        if age in range(age_lower_limit, age_upper_limit + 1):
            print("Gratulálok, a gyermeke játszhat a csapatban.")
        else:
            print(error_message)
    except ValueError:
        print(error_message)
else:
    print(error_message)
