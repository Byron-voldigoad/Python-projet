from random import *

liste = []
a = int(input("entrer le nombre de valeurs que contient la liste:"))
b = a + 1
for i in range(1, b):
    liste.append(int(input("entrer des nombre:")))



c = input("dans quel ordre doit on classe la liste?:")

if c == "asc":
    print(sorted(liste))
elif c == "des":
    print(sorted(liste,reverse=True))
elif c == "aucun":
    print(sorted(liste))
else:
    print("entrer les critere de croisance demadé")