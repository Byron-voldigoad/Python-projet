import random


nbr_list = [2,2,3,6,5,6,4,8,9]
#random.shuffle(nbr_list)
nbr_list1 = [[nbr_list[0],nbr_list[1],nbr_list[2]],
             [nbr_list[3],nbr_list[4],nbr_list[5]],
             [nbr_list[6],nbr_list[7],nbr_list[8]]]

def verifier_tableau(nbr_list):
    chiffres = set(range(1, 10)) # ensemble des chiffres de 1 à 9
    for chiffre in chiffres:
        if nbr_list.count(chiffre) > 1: # si le chiffre est présent plus d'une fois
            manquant = chiffres - set(nbr_list) # on calcule le chiffre manquant
            nbr_list[nbr_list.index(chiffre)] = manquant.pop() # on remplace le chiffre répété par le chiffre manquant
            break # on sort de la boucle car on a trouvé un chiffre répété et l'a remplacé
    return nbr_list
random.shuffle(nbr_list1)

verifier_tableau(nbr_list)
print(nbr_list)
print(nbr_list1)
