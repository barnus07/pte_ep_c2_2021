ev = 2000
if ev % 4 == 0:
    if ev % 100 == 0:
        if ev % 400 == 0:
            print("szökőév")
        else:
            print("nem szökő év")
    else:
        print("szökőév")
else:
   print("nem szökő év")
