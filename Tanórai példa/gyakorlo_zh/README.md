# Feladatkiírás

Eszemiszom városában időközi helyhatósági választásokat írtak ki. A városban összesen 12 345 szavazásra jogosult
állampolgár van, akiket nyolc választókerületbe soroltak. Minden választókerületben több jelölt is indul, de egy jelölt
csak egy választókerületben indulhat. Egy választókerület szavazói az adott választókerületben induló jelöltek közül egy
jelöltre adhatnak le szavazatot, de nem kötelező részt venniük a szavazáson. Minden választókerületben az a jelölt nyer,
aki a legtöbb szavazatot kapja. (Feltételezheti, hogy egyetlen választókerületben sem alakult ki holtverseny.)
A jelöltek vagy egy párt támogatásával, vagy független jelöltként indulhatnak. Az idei évben a Gyümölcsevők Pártja
(GYEP), a Húsevők Pártja (HEP), a Tejivók Szövetsége (TISZ) vagy a Zöldségevők Pártja (ZEP) támogatja a jelölteket.

A szavazás eredményét a _szavazatok.txt_ szóközökkel tagolt fájl tartalmazza, amelynek minden sorában egy-egy
képviselőjelölt adatai láthatók.
Például:
<pre>
5 19 Ablak Antal -
1 120 Alma Dalma GYEP
7 162 Bab Zsuzsanna ZEP
</pre>

Az első két adat a választókerület sorszáma és a képviselőjelöltre leadott szavazatok száma. Ezt a jelölt vezeték- és
utóneve, majd a jelöltet támogató párt hivatalos rövidítése követi. Független jelöltek esetében a párt rövidítése
helyett egy kötőjel szerepel. Minden képviselőjelöltnek pontosan egy utóneve van.

Írjon programot az alábbi feladatok megoldására:
1. Olvassa be a _szavazatok.txt_ fájl adatait, majd ezek felhasználásával oldja meg a következő feladatokat!
2. Hány képviselőjelölt indult a helyhatósági választáson?
3. Kérje be egy képviselőjelölt vezetéknevét és utónevét, majd írja ki a képernyőre, hogy az illető hány szavazatot
kapott! Ha a beolvasott név nem szerepel a nyilvántartásban, úgy jelenjen meg a képernyőn az „Ilyen nevű
képviselőjelölt nem szerepel a nyilvántartásban!” figyelmeztetés! A feladat megoldása során feltételezheti, hogy nem
indult két azonos nevű képviselőjelölt a választáson. Csak vezetéknév keresztnév típusú nevet fogadjon el a
felhasználótól!
4. Határozza meg, hányan adták le szavazatukat, és mennyi volt a részvételi arány! (A részvételi arány azt adja meg,
hogy a jogosultak hány százaléka vett részt a szavazáson.) A részvételi arányt két tizedes jegy pontossággal,
százalékos formában írja ki a képernyőre!
5. Határozza meg és írassa ki a képernyőre az egyes pártokra leadott szavazatok arányát az összes leadott szavazathoz
képest két tizedes jegy pontossággal! A független jelölteket együtt, „Független jelöltek” néven szerepeltesse!
6. Melyik jelölt kapta a legtöbb szavazatot? Jelenítse meg a képernyőn a képviselő vezeték- és utónevét, valamint az őt
támogató párt rövidítését, vagy azt, hogy független! Ha több ilyen képviselő is van, akkor mindegyik adatai jelenjenek
meg!
7. Határozza meg, hogy az egyes választókerületekben kik lettek a képviselők! Írja ki a választókerület sorszámát, a
győztes vezeték- és utónevét, valamint az őt támogató párt rövidítését, vagy azt, hogy független egy-egy szóközzel
elválasztva a _kepviselok.txt_ nevű szöveges fájlba! Az adatok a választókerületek száma szerinti sorrendben jelenjenek
meg! Minden sorba egy képviselő adatai kerüljenek!

A program az alábbi modulokból álljon:
1. _kepviselo_: Egyedül a _Kepviselo_ osztályt tartalmazza. Az osztály attribútumai legyenek: a képviselő neve, választó kerülete,
pártjának teljes megnevezése és rövidítése, valamint a képviselőre leadott szavazatok száma.
2. _valasztas_: Az egyes feladatok megoldása külön függvényekben.
3. _main_: A feladatokat megoldó függvények meghívása.
4. _part_ (szorgalmi feladat): Egyedül a Part enumot tartalmazza. Vegye fel előre a pártok megnevezését és rövidítését
tartalmazó enumokat.

## Megoldás közben ügyeljen az alábbiakra

- A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát!
- Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, milyen értéket vár!
- Ellenőrizze a felhasználó által megadott adatok helyességét, érvényességét!

## Minta a szöveges kimenetek kialakításához

A képernyőre írást nem igénylő feladatok esetén nem szükséges a feladat sorszámát sem kiíratnia.

### Teszteset 1

<pre>
1. feladat: A szavazatok.txt beolvasása.
2. feladat: A helyhatósági választáson 92 képviselőjelölt indult.
3. feladat: Adja meg a képviselő nevét: Ablak Antal
A képviselő 19 szavazatot kapott.
4. feladat: A választáson 4713 állampolgár, a jogosultak 38.18%-a vett részt.
5. feladat: A pártokra leadott szavazatok aránya:
Gyümölcsevők Pártja: 16.36%
Húsevők Pártja: 24.59%
Tejivók Szövetsége: 21,49%
Zöldségevők Pártja: 20.03%
Független jelöltek: 7.53%

6. feladat: A választáson a legtöbb szavazatot szerzett képviselő(k):
Joghurt Jakab (TISZ)
Narancs Edmond (GYEP)
Vadas Marcell (HEP)

7. feladat: A választókerületek képviselőinek mentése a kepviselok.txt fájlba.
</pre>

### Teszteset 2

<pre>
1. feladat: A szavazatok.txt beolvasása.
2. feladat: A helyhatósági választáson 92 képviselőjelölt indult.
3. feladat: Adja meg a képviselő nevét: Birs Alma
Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!
4. feladat: A választáson 4713 állampolgár, a jogosultak 38.18%-a vett részt.
5. feladat: A pártokra leadott szavazatok aránya:
Gyümölcsevők Pártja: 16.36%
Húsevők Pártja: 24.59%
Tejivók Szövetsége: 21,49%
Zöldségevők Pártja: 20.03%
Független jelöltek: 7.53%

6. feladat: A választáson a legtöbb szavazatot szerzett képviselő(k):
Joghurt Jakab (TISZ)
Narancs Edmond (GYEP)
Vadas Marcell (HEP)

7. feladat: A választókerületek képviselőinek mentése a kepviselok.txt fájlba.
</pre>


