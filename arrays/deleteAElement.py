
X = [4,5,2,3,5,7,8,5,4,2,4,5,7,8,3]

def deleteAElement(A,k):
    writeIndex = 0
    v = A[k]
    for y in A:
        if y!=v:
            A[writeIndex] = y
            writeIndex+=1


    return writeIndex

n = deleteAElement(X,0)

print(n,X)