def tabla_meret(size):

    table = []
    for i in range(size):
        table.append(0)
    return(table)

def tabla(sor, oszlop):

    matrix = []
    for i in range(sor):
        matrix.append(tabla_meret(oszlop))
    return matrix

mx = tabla(3, 3)



while 0 < 9:
    print("Első játékos")
    jatekos1_sor = int(input("X:"))
    jatekos1_oszlop = int(input("Y:"))
    jatekos1_ertek = "X"
    mx[jatekos1_sor][jatekos1_oszlop] = jatekos1_ertek
    print(mx[0][0],mx[0][1], mx[0][2], "\n", mx[1][0], mx[1][1], mx[1][2], "\n", mx[2][0], mx[2][1], mx[2][2])
    print("Második játékos")
    jatekos2_sor = int(input("X:"))
    jatekos2_oszlop = int(input("Y:"))
    jatekos2_ertek = "O"
    mx[jatekos2_sor][jatekos2_oszlop] = jatekos2_ertek
    print(mx[0][0],mx[0][1], mx[0][2], "\n", mx[1][0], mx[1][1], mx[1][2], "\n", mx[2][0], mx[2][1], mx[2][2])
    if mx[0][0] and mx[1][0] and mx[2][0] == "O":
        print("1.jatekos nyert")
        break
    elif mx[0][0] and mx[1][0] and mx[2][0] == "X":
        break
    elif mx[0][1] and mx[1][1] and mx[2][1] == "O":
        break
    elif mx[0][1] and mx[1][1] and mx[2][1] == "X":
        break
    elif mx[0][2] and mx[1][2] and mx[2][2] == "O":
        break
    elif mx[0][2] and mx[1][2] and mx[2][2] == "X":
        break #oszlopos szabaly
    elif mx[0][0] and mx[0][1] and mx[0][2] == "O":
        break
    elif mx[0][0] and mx[0][1] and mx[0][2] == "X":
        break
    elif mx[1][0] and mx[1][1] and mx[1][2] == "O":
        break
    elif mx[1][0] and mx[1][1] and mx[1][2] == "X":
        break
    elif mx[2][0] and mx[2][1] and mx[2][2] == "O":
        break
    elif mx[2][0] and mx[2][1] and mx[2][2] == "X":
        break #soros szabaly
    elif mx[0][0] and mx[1][1] and mx[2][2] == "O":
        break
    elif mx[0][0] and mx[1][1] and mx[2][2] == "X":
        break
    elif mx[2][0] and mx[1][1] and mx[0][2] == "O":
        break
    elif mx[2][0] and mx[1][1] and mx[0][2] == "X":
        break #keresztbe szabaly
#meg nincs kész