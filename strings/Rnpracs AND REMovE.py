X = ['a','c','d','b','b','c','a']



def replaceAndRemove(X):
    print(X)
    i=0
    lenX =  len(X)
    Tlength = lenX
    for x in X:
        if(x=='a'):
            Tlength+=1


        X[i] = x
        if(x=='b'):
            Tlength-=1
        else:
            i+=1
    if(Tlength>=lenX):
        X = X+ [" " for _ in range(lenX-Tlength)]
    else:
        X= X[:Tlength]

    
    print(X)

replaceAndRemove(X)
