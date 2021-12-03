limit = 10000  # Ft
cheaper_discount = 10  # %
more_expensive_discount = 20  # %
raw_input_data = ""
price = 0
invalid_data = True
while invalid_data:
    try:
        raw_input_data = input("Kérem adja meg a termék árát: ")
        price = float(raw_input_data)
        if price <= 0:
            print("Egy termék ára csak pozitív lehet.")
        else:
            invalid_data = False
    except ValueError:
        print("A megadott érték nem szám.")
discount = 0
discount_price = 0
if price < limit:
    discount = cheaper_discount
else:
    discount = more_expensive_discount
discount = price * discount / 100
discount_price = price - discount
print("A kedvezmény mértéke", discount, "Ft, a kedvezményes ár pedig", discount_price, "Ft.")
