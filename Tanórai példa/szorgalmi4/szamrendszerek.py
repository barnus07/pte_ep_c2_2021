start_number_system = 0
start_number = ""
end_number_system = 0
end_number = ""
raw_input_data = ""
invalid_value = True
while invalid_value:
    raw_input_data = input("Kérem adja meg a kiinduló számrendszert: ")
    if raw_input_data.isnumeric():
        start_number_system = int(raw_input_data)
        if start_number_system > 1:
            invalid_value = False
        else:
            print("A megadott érték nem egy egynél nagyobb pozitív egész szám.")
    else:
        print("A megadott érték nem egy egynél nagyobb pozitív egész szám.")

invalid_value = True
while invalid_value:
    start_number = input("Kérem adja meg az átalakítandó számot: ")
    if start_number.isalnum():
        invalid_value = False
        for i in range(len(start_number)):
            if start_number[i].isnumeric():
                value2 = int(start_number[i])
            else:
                value2 = ord(start_number[i].upper()) - 65 + 10
            if value2 >= start_number_system:
                invalid_value = True
                print("Nem a kiindulási számrendszerbeli szám.")
    else:
        print("A megadott érték nem csak számjegyeket és betűket tartalmaz.")


invalid_value = True
while invalid_value:
    raw_input_data = input("Kérem adja meg a cél számrendszert: ")
    if raw_input_data.isnumeric():
        end_number_system = int(raw_input_data)
        if end_number_system > 1:
            invalid_value = False
        else:
            print("A megadott érték nem egy egynél nagyobb pozitív egész szám.")
    else:
        print("A megadott érték nem egy egynél nagyobb pozitív egész szám.")

number = 0
value = 0
for i in range(len(start_number)):
    if start_number[i].isnumeric():
        value = int(start_number[i])
    else:
        value = ord(start_number[i].upper()) - 65 + 10
    number += value * start_number_system ** (len(start_number) - i - 1)

while number > 0:
    remainder = number % end_number_system
    if remainder < 10:
        end_number = str(remainder) + end_number
    else:
        end_number = chr(remainder + 65 - 10) + end_number
    number = number // end_number_system
print("A szám értéke a cél számrendszerben:", end_number)
