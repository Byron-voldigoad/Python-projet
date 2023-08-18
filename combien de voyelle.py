
voyelle = ["a","e","y","u","i","o"]
a = input("entrer une chaine de charactere:")


c = 0
mot_min = a.lower()
for a in mot_min:
    if a in voyelle:
        c += 1



print(c)