import math

print("1.feladat")
for i in range(1, 11):
    for y in range(1, 11):
        print('{:3}'.format(i*y), end=' ')

    print()
print("2.feladat")
print("3.feladat")
nsor = []
n = int(input("Adja meg az N sort:"))
for i in range(0,n+1):
    nsor.append(math.factorial(n)/(math.factorial(i)*(math.factorial(n-i))))
print(nsor)
print("4.feladat")
