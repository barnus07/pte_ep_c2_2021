is_number = False
while not is_number:
    try:
        number = int(input("Please give me an integer number: "))
        is_number = True
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    except ValueError:
        print("Input is not an integer number.")
