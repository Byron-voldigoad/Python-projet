num = int(input("entrer un nombre:"))
a = 1+pow(2,num)
b = 1+2*num
c = a%b
if c == 0:
    print(num, " est un numero curzon")
else:
    print(num, "n'est pas un numero curzon")