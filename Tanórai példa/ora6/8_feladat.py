a, b = 0, 0
is_number = False
while not is_number:
    try:
        a = int(input("Kezdő érték: "))
        is_number = True
    except ValueError:
        print("invalid érték")

is_number = False
while not is_number:
    try:
        b = int(input("Utolsó érték: "))
        is_number = True
    except ValueError:
        print("invalid érték")

sum_and = 0
sum_or = 0
for number in range(a, b + 1):
    if number % 3 == 0 or number % 5 == 0:
        sum_or += number
    if number % 3 == 0 and number % 5 == 0:
        sum_and += number
print(sum_and)
print(sum_or)
