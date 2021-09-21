p = int(input())
q = int(input())


def kepker(k):
    if(k==1):
        return True
    x= k**2
    s = str(x)
    if(len(s)<=1):
        return False
    a = int(s[:-len(str(k))]) + int(s[-len(str(k)):])
    # if(k==a):
    #     print(k,s[:-len(str(k))] , s[-len(str(k)):])
    return k == a

a = []
for i in range(p,q+1):
    if(kepker(i)):
        a.append(str(i))
if(p>q):
    print("INVALID RANGE")
else:
    if(len(a)==0):
        print("INVALID RANGE")
    else:
        print(" ".join(a))