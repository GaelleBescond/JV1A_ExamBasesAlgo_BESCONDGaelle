"""
3 listes l'une par dessus l'autre
On choisit premièrement où placer un jeton (X=1, O=2)
On vérifie si la case est occupée (vide=0)
On place le jeton sur la case voulue

"""
game = True
touche = ''
ligne1 = [0,1,0]
ligne2 = [1,0,2]
ligne3 = [0,2,0]
Listelignes = [ligne1,ligne2,ligne3]

lignechoix = 0
colonnechoix = 0


while(game == True):
    #Demande de la ligne d'action du joueur
    touche = int(input("Sur quelle ligne jouer (1 à 3)?"))

    if(touche == 1 or touche ==2 or touche==3):
        lignechoix = touche
        print("Vous jouer la ligne", lignechoix)
    else:
        print("Veuillez entrer 1, 2 ou 3")

    #Demande de la colonne d'action du joueur
    touche = int(input("Sur quelle colonne jouer (1 à 3)?"))
    if(touche == 1 or touche ==2 or touche==3):
        colonnechoix = touche
        print("Vous jouer la colonne", colonnechoix)
    else:
        print("Veuillez entrer 1, 2 ou 3")

    if (Listelignes[lignechoix-1][colonnechoix-1] == 0):
        Listelignes[lignechoix-1][colonnechoix-1] = 1
    else:
        print("Recommencez sur une case valide!")

    print(ligne1)
    print(ligne2)
    print(ligne3)

"""

Pas terminé


"""