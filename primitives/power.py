def mul(a,b):
    return a*b


def power(x,y):
    print(x,y)
    if(y==0):
        return 1
    if(y==1):
        return x
    if(y==2):
        return x*x

    if(y&1):
        return x *  power(power(x,y//2),2)
    else:
        return power(power(x,y//2),2)



print(power(3,300000))

print(3**300000)

