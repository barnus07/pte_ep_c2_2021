import random

random_numbers = []
for number in range(10):
    random_numbers.append(random.randint(1, 100))

even_numbers = []
odd_numbers = []
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        even_numbers.append(random_numbers[i])
    else:
        odd_numbers.append(random_numbers[i])

print("A generált számsor:", random_numbers)
print("A párosak:", even_numbers)
print("A páratlanok:", odd_numbers)
