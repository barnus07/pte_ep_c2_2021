fileobject = open("lorem.txt", "a", encoding="UTF-8")
fileobject.write("körte")
fileobject.flush()
fileobject.close()
