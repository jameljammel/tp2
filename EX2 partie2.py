import math
from math import *

n = input("donner n:")
U0 = 1
print(n)


def term(n):
     for i in range(1, n+1):
        u = ((n-1) * (pow(2,n)) )+ n
     print(u)


term(n)
