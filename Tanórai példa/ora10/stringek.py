def megtalal(karakter: str, szoveg: str) -> int:
    pozicio = -1
    for i in range(len(szoveg)):
        if pozicio == -1 and szoveg[i] == karakter:
            pozicio = i
    return pozicio


def kacsanevek(prefixes="JKLMNOPQ", suffix="ack") -> str:
    nevek = ""
    for prefix in prefixes:
        nevek += prefix + suffix + ", "
    return nevek[0:-2]


str1 = "x"
str2 = "hallgató"
print(str2.find(str1), megtalal(str1, str2))
print(kacsanevek())
print(kacsanevek("JKL", "ack"))
