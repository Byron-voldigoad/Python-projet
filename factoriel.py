from math import *
a = int(input("entrer un nombre:"))
b = 1
c = a
while c != 0:
    b = b * c
    c -= 1

d = factorial(a)


print(a,"factorielle =",b)
print(a,"factorielle =",d)