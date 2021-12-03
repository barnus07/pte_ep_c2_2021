number = 5
number2 = number * 2
print("A number változó értéke:", number, "\b. Ha megszorzom kettővel, akkor", number2, "\b-t kapok.")
print("A number változó értéke: ", number, ". Ha megszorzom kettővel, akkor ", number2, "-t kapok.", sep="")
print(f"A number változó értéke: {number}. Ha megszorzom kettővel, akkor {number2}-t kapok.")
print("A number változó értéke: {}. Ha megszorzom kettővel, akkor {}-t kapok.".format(number, number2))

# Igazítások
print(f"A number változó értéke: {number:<3}. Ha megszorzom kettővel, akkor {number2:>4}-t kapok.")
print("A number változó értéke: {:^3}. Ha megszorzom kettővel, akkor {:^4}-t kapok.".format(number, number2))

# Számformátumok
number = 125
print(f"A szám bináris alakja: {number:b}, az oktális alakja: {number:o}, a decimális alakja: {number:d}, "
      f"hexadecimális alakja: {number:x} és {number:X}")
print("A szám bináris alakja: {:b}, az oktális alakja: {:o}, a decimális alakja: {:d}, "
      "hexadecimális alakja: {:x} és {:X}".format(number, number, number, number, number))

# Unicode character
number = 65
print(f"{number:c}")
print("{:c}".format(number))

# Valós számok
number = 100.12345
print(f"Tudományos: {number:e} vagy {number:E}")
print(f"Valós szám: {number:f}")
print(f"3 tizedesjegy pontosság: {number:.3f}")
print(f"15 karakteren: {number:15f}")
print(f"15 karakteren, 3 tizedesjegy pontosság: {number:15.3f}")
print(f"Százalékos érték: {number:%}")
print(f"3 tizedesjegy pontosság: {number:.3%}")
print(f"15 karakteren: {number:15%}")
print(f"15 karakteren, 3 tizedesjegy pontosság: {number:15.3%}")
