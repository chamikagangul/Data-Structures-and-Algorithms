X = ['a','c','d','b','b','c','a']



def replaceAndRemove(X):
    i=0
    Tlength = len(X)
    for x in X:
        if(x=='a'):
            Tlength+=1


        X[i] = x
        if(x=='b'):
            Tlength-=1
        else:
            i+=1
    print(X,i)
    return X

replaceAndRemove(X)
