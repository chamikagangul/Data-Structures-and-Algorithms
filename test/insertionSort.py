import random


def insertionSort(A):
    lenA = len(A)
    for i in range(lenA-1):
        j = i
        while(j>=0 and A[j] > A[j+1]):
            A[j],A[j+1] = A[j+1],A[j]
            j = j-1
    
    return A

# MyArr = [ random.randint(0,200) for _ in range(10)]

# insertionSort(MyArr)
# print(MyArr)

for i in range(1000):
    MyArr = [ random.randint(0,200) for _ in range(100)]
    
    SortedArr = sorted(MyArr) 
    insertionSort(MyArr)
    
    
    if(SortedArr != MyArr):
        print(False)
        break
else:
    print(True)