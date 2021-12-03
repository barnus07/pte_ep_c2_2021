input_values = []
while len(input_values) == 0 or input_values[len(input_values) - 1] != "":
    input_values.append(input())
input_values.remove("")
print(input_values)

row = 0
while len(input_values) == 0 or row != "":
    row = input()
    if row != "":
        input_values.append(row)
print(input_values)
