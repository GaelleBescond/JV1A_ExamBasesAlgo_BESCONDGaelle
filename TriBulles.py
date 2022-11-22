import random

lengthTable = 0
myTable = [0,5,4,3,2,0,0,0,0,0]

maxTable = 0
Indice = 0
varDecalage= 0

compteur = 0
#Generation de la liste
for i in range (len(myTable)):
    myTable[i] = random.randint(0,100)
print("voici la liste à trier")
print(myTable)

#Boucle de tri
for n in range(len(myTable)-1):
    for i in range (len(myTable)-1):
        if (myTable[i]>myTable[i+1]):
            varDecalage = myTable[i]
            myTable[i] = myTable[i+1]
            myTable[i+1] = varDecalage
        compteur += 1
print("Voici la liste après tri")
print(myTable)
print("Il aura fallu", compteur, "passages")

"""
Le programme est de plus en plus lent au fur et à mesure qu'il est grand. En effet, les itérations requises sont multipliés au carré (boucle de longueur n incluant une autre boucle de sa propre longueur-1 :  (n-1)² )
Pour 2 valeurs dans la liste, il faudra 1 itération.
Pour 6 valeurs dans la liste, il faudra 25 itérations. (Exemple ci-dessus)
Pour 10 valeurs dans la liste, il faudra 81 itérations.
pour 21 valeurs, 400,
pour 31, 900.
etc...
"""