filepath = "lorem.txt"
fileobject = open(filepath, "r")
max_length = 0
max_row = ""
for line in fileobject:
    if len(line) > max_length:
        max_row = line
        max_length = len(line)
print(max_row)
fileobject.close()
