"""
Önálló függvényekben oldja meg az alábbiakat:
    - Kérjen be tetszőleges mennyiségű valós napi hőmérséklet adatokat. Valósnak tekintsünk minden -40 és +40 °C közötti
      értéket.
    - Számolja ki a hőmérsékletek átlagát és kiírja a képernyőre.
    - Számolja ki azon hőmérsékletek átlagát, melyek magasabbak, mint az átlag, és kiírja a képernyőre.
    - Keresse meg az első olyan hőmérsékletet, mely magasabb az átlaghőmérsékletnél, kiírja a konzolra a sorszámát és
      az értékét is.
    - Keresse meg a legnagyobb megadott hőmérsékletet, kiírja a képernyőre a sorszámát és az értékét.
"""

# A paraméter után ": {típus}" kiegészítéssel megadható, milyen típusúként kezeljük, így elhagyhatjuk a típusvalidációt.
def valos_homerseklet1(adat):
    """Ha az adat paraméter értéke benne van a [-40, 40] intervallumban, akkor True,
       minden más esetben False értékkel tér vissza."""
    valos_homerseklet_e = False
    if (type(adat) == int or type(adat) == float) and -40 <= adat <= 40:
        valos_homerseklet_e = True
    return valos_homerseklet_e


# A paraméternevét követő ": {típus}" jelöléssel megadhatjuk, milyen típusú értéket várunk ide, így a PyCharm jelzi, ha
# nem ilyen értékkel hívjuk meg. Ha adunk meg elvárt típust, nem fontos belül is validálni.
# A "-> {típus}" segítségével a visszatérési érték típusát közvetlenül mi tudjuk megadni.
def valos_homerseklet2(adat: float) -> bool:
    """Ha az adat paraméter értéke benne van a [-40, 40] intervallumban, akkor True,
       minden más esetben False értékkel tér vissza."""
    valos_homerseklet_e = False
    if -40 <= adat <= 40:
        valos_homerseklet_e = True
    return valos_homerseklet_e


def homerseklet_beolvasas():
    """Addig olvassa be a hőmérséklet adatokat, ameddig valós hőmérséklet adatok érkeznek. Valósnak tekintjünk
       a -40 és +40 °C közötti értéket."""
    homerseklet_lista = []
    tovabb_kell_e_olvasni = True  # Azért kell igaz értéket felvennie, hogy legalább egy beolvasás megtörténhessen.
    while tovabb_kell_e_olvasni:
        beolvasott_homerseklet_string = input("Kérek egy hőmérséklet adatot: ")
        try:
            beolvasott_homerseklet_number = float(beolvasott_homerseklet_string)
            if valos_homerseklet1(beolvasott_homerseklet_number):  # Ha valós hőmérséklet, akkor hozzáadjuk a listához.
                homerseklet_lista.append(beolvasott_homerseklet_number)
            else:
                tovabb_kell_e_olvasni = False
        except ValueError:
            tovabb_kell_e_olvasni = False
    return homerseklet_lista


def atlag_homerseklet_kiszamitasa(homerseklet_lista: list) -> float:
    """Kiszámítja egy lista elemeinek átlagát.
       Ha nem listával hívjuk meg, akkor TypeErrort dob, amit a hívónak el kell kapnia egy try-except szerkezettel.
       :raise TypeError: Ha a homerseklet_lista nem 'list' típusú.
       :raise ValueError: Ha a homerseklet_lista nem tartalmaz elemet.
       """
    if type(homerseklet_lista) == list:
        if len(homerseklet_lista) > 0:
            osszeg = 0
            for i in range(len(homerseklet_lista)):
                osszeg += homerseklet_lista[i]
            return osszeg / len(homerseklet_lista)
        else:
            raise ValueError("A homerseklet_lista nem tartalmaz elemet.")  # Saját hiba dobása
    else:
        raise TypeError("A homerseklet_lista csak 'list' típusú lehet.")  # Saját hiba dobása


def magasabb_elemek_kivalasztasa(lista: list[float], limit: float) -> list[float]:
    magasabb_homersekletek = lista.copy()
    for i in range(len(lista)):
        if lista[i] <= limit:
            magasabb_homersekletek.remove(lista[i])
    return magasabb_homersekletek


def elso_magasabb_elem_kivalasztasa(lista: list[float], limit: float):
    magasabb_elem = []
    i = 0
    while i < len(lista) and lista[i] <= limit:
        i += 1
    if i < len(lista) and lista[i] > limit:
        magasabb_elem.append(i)
        magasabb_elem.append(lista[i])
    return magasabb_elem


def maximumhely_kereses(lista: list[float]):
    maximum = [0, lista[0]]
    for i in range(len(lista)):
        if lista[i] > maximum[1]:
            maximum[0] = i
            maximum[1] = lista[i]
    return maximum


def maximum_kereses(lista: list[float]) -> float:
    """
    Megkeresi a lista legnagyobb elemét (maximumát).
    :param lista: Valós számokat tartalmazó lista.
    :return: A lista legnagyobb eleme.
    """
    maximum = lista[0]
    for i in range(len(lista)):
        if lista[i] > maximum:
            maximum = lista[i]
    return maximum


# Programtörzs
# 1. részfeladat
homersekletek = homerseklet_beolvasas()

if len(homersekletek) > 0:
    # 2. részfeladat
    atlag_homerseklet = atlag_homerseklet_kiszamitasa(homersekletek)
    print(f"A hőmérséklet adatok átlaga: {atlag_homerseklet} °C.")

    if len(homersekletek) > 1:
        # 3. részfeladat
        atlagnal_magasabb_homersekletek = magasabb_elemek_kivalasztasa(homersekletek, atlag_homerseklet)
        if len(atlagnal_magasabb_homersekletek) > 0:
            atlagnal_magasabb_homersekletek_atlaga = atlag_homerseklet_kiszamitasa(atlagnal_magasabb_homersekletek)
            print(f"Az átlaghőmérsékletnél magasabb hőmérséklet adatok átlaga:"
                  f" {atlagnal_magasabb_homersekletek_atlaga} °C.")

            # 4. részfeladat
            elso_magasabb = elso_magasabb_elem_kivalasztasa(homersekletek, atlag_homerseklet)
            print(f"Az első, átlaghőmérsékletnél magasabb érték a lista {elso_magasabb[0] + 1}. eleme ({elso_magasabb[0]}."
                  f" pozíció): {elso_magasabb[1]} °C.")
        else:
            print("Mindegyik érték azonos.")
    else:
        print("Nincs elegendő adat az átlagnál magasabb értékek meghatározásához.")

    # 5. részfeladat
    legmagasabb = maximumhely_kereses(homersekletek)
    print(f"A legmagasabb érték a lista {legmagasabb[0] + 1}. eleme ({legmagasabb[0]}. pozíció): {legmagasabb[1]} °C.")
