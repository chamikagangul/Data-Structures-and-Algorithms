import random
A = [random.randint(0, 100) for i in range(10)]
B = [random.randint(0, 100) for i in range(10)]
A = [2,3,3,5,5,6,7,7,8,12]
B = [5,5,6,8,8,9,10,10]
A.sort()
B.sort()
print(A, B)

def ComputeIntersection(A,B):
    i,j =0,0
    intersection = [None]
    while i< len(A) and j<len(B):
        if(A[i] == B[j]):
            if(intersection[-1] != A[i]):
                intersection.append(A[i])
            i+=1
            j+=1
        elif(A[i] <B[j]):
            i+=1
        elif(A[i] >B[j]):
            j+=1
    print(intersection[1:])

ComputeIntersection(A,B)