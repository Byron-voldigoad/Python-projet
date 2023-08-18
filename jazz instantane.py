
def jazz(nb:str="7"):
    nb = [nb]

    return nb

def num(nb,a,b,sept):
    sept = [7]
    while a < b:
        nb[a] += str(sept[0])
        a += 1

s = []
p = [7]
c = 0
d = 0
for i in range(1, 6):
    s.append(input("entrer une liste:"))
    c += 1


print(jazz(s), num(s, d, c, p))