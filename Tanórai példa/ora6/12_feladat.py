erdemjegyek = []
sum = 0
avg = 0
min = 5
max = 1
invalid = False
while not invalid:
    try:
        erdemjegy = int(input("A követekző hallgató érdemjegye: "))
        if erdemjegy >= 1 and erdemjegy <= 5:
            erdemjegyek.append(erdemjegy)
            if min > erdemjegy:
                min = erdemjegy
            if max < erdemjegy:
                max = erdemjegy
            sum += erdemjegy
            avg = sum / len(erdemjegyek)
            print(len(erdemjegyek), avg, max, min)
        else:
            invalid = True
    except ValueError:
        invalid = True
