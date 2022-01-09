X = ['a','c','a','a']



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
        X = X+ [" " for _ in range(Tlength - lenX)]
    else:
        X= X[:Tlength]

    print(X)

    i-=1
    j = Tlength-1
    while j>0:
        if(X[i] == 'a'):
            X[j-1],X[j] = 'd','d'
            j-=2
        else:
            X[j] = X[i]
            j-=1
        i-=1
            
    print(X)

replaceAndRemove(X)
