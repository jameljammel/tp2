u = 1       # on initialise u au premier terme de la suite
n: int = input("donner n:")      # on veut calculer le terme de rang 5
for n in range(1,10):
    b = n-1
    v = 2 ** n
    r = u*b
    u = (v*u*r)+ n
    print(n,u,v)