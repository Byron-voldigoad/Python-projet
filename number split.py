
a = int(input("entrer un nombre:"))
if a%2 == 1:
 b = a+1
 b = b/2
 print(a,"=",b,"+",b+1)
else:
 b = a
 b = b/2
 print(a,"=",b,"+",b)