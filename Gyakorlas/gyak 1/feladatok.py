from gyak1 import ember

def read()->list:
    with open("szamok.txt","r",encoding="UTF-8") as f:
       try:
           lista = [sor.strip() for sor in f]

           return lista
       except FileNotFoundError:
           print("Nem létezik ilyen fajl")
