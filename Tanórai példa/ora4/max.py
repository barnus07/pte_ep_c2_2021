import random

my_list = []
for i in range(20):
    my_list.append(random.randint(1, 101))

print(my_list)
max = my_list[0]
for i in range(len(my_list)):
    if max < my_list[i]:
        max = my_list[i]
print(max)

my_list.sort(reverse=True)
print(my_list[0])
