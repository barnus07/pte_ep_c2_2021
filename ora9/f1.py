
def sorrend(list: list[int]) -> list[int]:
    min = 0
    max = 0
    summ = 0
    for i in range(len(list)):
        if list[i] > max: max = list[i]
    min = max
    for i in range(len(list)):
        if list[i] < min: min = list[i]
        summ += list[i]
    avg = summ / len(list)
    return summ,max,min,avg

print(sorrend([1,3,6,8,9,234]))