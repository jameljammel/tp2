u = 1
s = 0
p = 10
n: int = input("donner n:")      # on veut calculer le terme de rang 5
for n in range(0, p+1):
    b = n-1
    v = 2 ** n
    r = u*b
    u = (v*u*r)+ n
    s = u + s
    print(n,u,v,s)