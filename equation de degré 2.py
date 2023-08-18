import math


print("soit lequation ax+bx+c=")
a = int(input("entrer a:"))
b = int(input("entrer b:"))
c = int(input("entrer c:"))
D = (b*b-4*a*c)
if a == 0:
    print("cette equation n'est pas resolvable par le discriminent!!!!!")
    if b == 0:
        print("il ne sagit pas d'une equation de degré 2")
    else:
        X = -c/b
        print("la solution est X=", X)
elif a == b == 0:
  print("il ne sagit pas d'une equation de degré 2")
else:
  if D < 0:
    print("lequation n'admet aucune solution dans R")
  elif D == 0:
    X = (-b/(2*a))
    print("lequation admet une solution double X =", X)
  else:
    X1 = (-b-math.sqrt(D))/(2*a)
    X2 = (-b+math.sqrt(D))/(2*a)
    print("lequation admet deux solution X1 =", X1, "et X2 =", X2)