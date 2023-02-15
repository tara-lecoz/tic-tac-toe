gameboard= ["-","-","-",
            "-","-","-",
            "-","-","-"]


def display_gameboard():
    print(gameboard[0],"|",gameboard[1],"|",gameboard[2])
    print(gameboard[3],"|",gameboard[4],"|",gameboard[5])
    print(gameboard[6],"|",gameboard[7],"|",gameboard[8])

def joueurs():
    print("Choisir un signe : X ou O ")
    j1=input("Joueur 1 : ")
    j2=""
    if j1 == "X":
        j2="O"
        print("Joueur 2 : "+ j2)
    elif j1 == "O":
        j2="X"
        print("Joueur 2 : "+ j2)
    elif j1 != "X" or j1 != "O":
        print("Saisir une valeure valide : ")

board = [[1,2,3],[4,5,6],[7,8,9]]
#print(board[1][1])

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, sep="|")
    print()