import elso
import ido
import listak
import allatok
from ora11.time import Time
import sik


"""
#elso.upper_case("Az almak almafan teremnek.")
#ido.szamlalo(30, 3)
szamok = [24, 5, 75, 13, 24, 7, 35, 75, 75]
print(listak.ismetlodesek(szamok))
print(listak.kisebb(szamok, 20))
print("prímtényezők")
listak.primek(36)
print("prímtényezők")
listak.primek(11)

bodri = allatok.Kutya("Bodri", "puli")
kutyus2 = allatok.Kutya("Buksi", "keverék")
bodri.allapot()
kutyus2.allapot()
bodri.jatek(30)
bodri.allapot()
kutyus2.allapot()
print(bodri)

orak = int(input("Óra: "))
percek = int(input("Perc: "))
masodpercek = int(input("Másodperc: "))
ido = Time(orak, percek, masodpercek)
ido.print()"""

p1 = sik.Pont(0, 0)
p2 = sik.Pont(0, 5)
p3 = sik.Pont(2, 6)
print("p1 és p2 távolsága:", p1.tavolsag1(p2))
print("p1 és p3 távolsága:", p1.tavolsag2(p3))

negyzet = sik.Negyzet(sik.Pont(4, 0), sik.Pont(4, 4), sik.Pont(0, 4), p1)
print(negyzet.kerulet())
print(negyzet.terulet())
