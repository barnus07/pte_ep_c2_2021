def rendezes(lista: list[int]) -> list[int]:
    rendezett_lista = lista.copy()
    for i in range(len(rendezett_lista)):
        for j in range(i + 1, len(rendezett_lista)):
            if rendezett_lista[i] > rendezett_lista[j]:
                seged = rendezett_lista[i]
                rendezett_lista[i] = rendezett_lista[j]
                rendezett_lista[j] = seged
    return rendezett_lista


def minimum(lista: list[int]) -> int:
    minimum = lista[0]
    for szam in lista:
        if szam < minimum:
            minimum = szam
    return minimum


def maximum(lista: list[int]) -> int:
    maximum = lista[0]
    for szam in lista:
        if szam > maximum:
            maximum = szam
    return maximum


def osszeg(lista: list[int]) -> int:
    osszeg = 0
    for szam in lista:
        osszeg += szam
    return osszeg


def atlag(lista: list[int]) -> float:
    return osszeg(lista) / len(lista)


def minimum2(lista: list[int], hanyadik=1) -> int:
    rendezett_lista = rendezes(lista)
    return rendezett_lista[hanyadik - 1]


def maximum2(lista: list[int], hanyadik=1) -> int:
    rendezett_lista = rendezes(lista)
    return rendezett_lista[-hanyadik]



szamok = [24, 7, 1, 45, 23, 4]
print(rendezes(szamok))
print(minimum(szamok))
print(maximum(szamok))
print(osszeg(szamok))
print(atlag(szamok))
print(minimum2(szamok))
print(maximum2(szamok))
print(minimum2(szamok, hanyadik=3))
print(maximum2(szamok, hanyadik=3))
