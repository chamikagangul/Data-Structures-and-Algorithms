import random
A = [random.randint(0, 100) for i in range(10)]
B = [random.randint(0, 100) for i in range(10)]

A.sort()
B.sort()
A = A
print(A, B)

def mergeTwoSortedArrays(A,B):
    i,j = len(A)-1,len(B)-1
    
    A = A  + [float('inf') for _ in range(j+1)]
    k = i+j+1
    while(i + j>=-1):
       
        if(i<0):
            A[j] = B[j] 
            j-=1
        elif(j<0):
            A[i] = A[i]
            i-=1
        elif(A[i] > B[j]):
            A[k] = A[i]
            i-=1
        else:
            A[k] = B[j]
            j-=1
        k-=1
    
    print(A,B,i,j)

mergeTwoSortedArrays(A,B)