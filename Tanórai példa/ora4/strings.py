text = "Eszperente"
counter = 0
for i in range(len(text)):
    if text[i] == "e" or text[i] == "E":
        counter += 1
print(counter)

counter = 0
for character in text:
    if character == "e" or character == "E":
        counter += 1
print(counter)
