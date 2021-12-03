def greeting(name):
    if type(name) == str:
        print(f"Szia {name}!")

greeting("Bence")
greeting(input("Hogy hívnak?\n"))
