
a = int(input("entrer le nombre d'element de la liste:"))
b = 0
for i in range(a):
    print("entrer le nombre",i)
    nbr = int(input(""))
    if nbr > b:
        b = nbr
    findliste = [nbr]
c = len(str(nbr))
print("le plus gand nombre de votre liste est:",b,c)
'''
lst1 = [1,2,3]
lst2 = [5,3,2]
lst3 = [7,3,2]
z=0
e=0
for a in lst1:
    for b in lst2:
        for c in lst3:
            if (a==b==c):
                z = a
                break
for a in lst1:
    for b in lst2:
        for c in lst3:
            if (a == b == c):
                if a != z:
                    e = a

r = z+e
print(z)
print(e)
print(r)
'''