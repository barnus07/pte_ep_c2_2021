# Innentől az 5. dia 1. feladat
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()

for j in range(1, 11):
    print(j, end=" ")
print()

for j in range(10):
    print(j + 1, end=" ")
print()

for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(j, end=" ")
print()

# Innentől az 5. dia 2. feladat
i = 1
while i <= 6:
    print(2 * i - 1, end=" ")
    i += 1
print()

for j in range(1, 12, 2):
    print(j, end=" ")
print()

# 5. dia 3. feladat
a1 = 0
a2 = 1
print(a1, a2, end=" ")
i = 0
while i < 8:
    an = a1 + a2
    a1 = a2
    a2 = an
    print(an, end=" ")
    i += 1
