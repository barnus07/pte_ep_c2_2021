import random


numbers = []
for i in range(20):
    numbers.append(random.randint(1, 100))

min_value = numbers[0]
max_value = numbers[0]
for number in numbers:
    if min_value > number:
        min_value = number
    if max_value < number:
        max_value = number

print(numbers)
print(min_value)
print(max_value)
