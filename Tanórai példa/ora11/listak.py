def ismetlodesek(lista: list[float]) -> list[float]:
    ismetlodo_szamok = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                ismetlodotte_mar = False
                for szam in ismetlodo_szamok:
                    if lista[i] == szam:
                        ismetlodotte_mar = True
                if ismetlodotte_mar == False:
                    ismetlodo_szamok.append(lista[i])
    return ismetlodo_szamok


def kisebb(lista: list[float], limit: float) -> int:
    kisebbek = 0
    for szam in lista:
        if szam < limit:
            kisebbek += 1
    return kisebbek


def primek(szam: int) -> None:
    maradek = szam
    oszto = 2
    while maradek > 1:
        if maradek % oszto == 0:
            maradek = maradek // oszto
            print(oszto)
        else:
            oszto += 1
