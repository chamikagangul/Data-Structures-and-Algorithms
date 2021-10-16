import random
def computeAlter(x):
    for i in range(len(x)-1):
        if(i%2==0):
            if(x[i]>x[i+1]):
                x[i],x[i+1] = x[i+1],x[i]
        else:
            if(x[i]<x[i+1]):
                x[i],x[i+1] = x[i+1],x[i]
    return x

x = [random.randint(1,100) for i in range(100)]
print(x)
print(computeAlter(x))