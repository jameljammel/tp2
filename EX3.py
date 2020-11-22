
a: int = input("donner a:")
p: int = input("donner p:")
n: int = input("donner n:")
print(a)
print(p)
print(n)
def term(a,p,n):
    U0 = 1
    for n in range(1, p):
        U = (n-1)
        u = (U * (pow(2, n)))
        s = u + n
        print(u)

term(a,p,n)