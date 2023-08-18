import datetime
from random import*





jour = int(input("entrer le jour:"))
mois = int(input("entrer le mois:"))
annee = int(input("entrer l'annee:"))
b = datetime.date(annee,mois,jour)
A = 2022

a = datetime.date(2023,12,24)



if a == b:
    print(True)
else:
    print(False)

