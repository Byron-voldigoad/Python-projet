import math
from math import *

a = int(input("entrer un nombre:"))
number_parity = a%2
b = [int(a) for a in str(a)]
c = sum(b)
digits_parity = c%2
if digits_parity == number_parity:
    print(True)
else:
    print(False)