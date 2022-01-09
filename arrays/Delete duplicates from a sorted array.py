X = [2,3,5,5,7,11,11,11,13]

def removeDuplicates(X):
    i=0
    last =None
    for x in X:
        if last != x:
           last = x
           X[i] = x
           i+=1
    
    return X,i


y,i= removeDuplicates(X)

print(y,i)