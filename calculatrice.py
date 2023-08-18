def addition(a, b):
    return a+b


def multiplication(a, b):
    return a*b


def division(a, b):
    return a/b

def soustraction(a, b):
    return a-b


a = int(input("entrer le premier nombre:"))
x = input("entrer le signe de l'opperation(+,-,* ou /):")
b = int(input("entrer le second nombre:"))

if x == "+":
    print(a,"+",b,"=",addition(a, b))
elif x == "-":
    print(a,"-",b,"=",soustraction(a, b))
elif x == "/":
    print(a,"/",b,"=",division(a, b))
elif x == "*":
    print(a,"*",b,"=",multiplication(a, b))
else:
    print("il ne sagit pas d'un opperateur")


