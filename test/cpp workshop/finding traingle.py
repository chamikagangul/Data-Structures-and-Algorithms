import math



n1,n2,n3 = map(int,input().split())

# n C r
def nCr(n,r):
    math.factorial
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

V=3
V=V+n1+n2+n3
trainglesOnSide1,trainglesOnSide2,trainglesOnSide3=0,0,0
if (n1!=0):
    n1 = n1+2
    trainglesOnSide1 = nCr(n1,3)
if (n2!=0):
    n2 = n2+2
    trainglesOnSide2 = nCr(n2,3)
if (n3!=0):
    n3 = n3+2
    trainglesOnSide3 = nCr(n3,3)    




total = nCr(V,3)

print(total-trainglesOnSide1-trainglesOnSide2-trainglesOnSide3)