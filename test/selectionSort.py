import random
def selectionSort(A):
    
    lenA = len(A)
    for i in range(lenA):
        currentMin = i
        for j in range(i,lenA):
            if(A[currentMin]> A[j]):
                currentMin = j
        
        A[i],A[currentMin] = A[currentMin],A[i]

# MyArr = [ random.randint(0,200) for _ in range(10)]

# SortedArr = sorted(MyArr) 
# selectionSort(MyArr)
# print(MyArr)

for i in range(1000):
    MyArr = [ random.randint(0,2000) for _ in range(10)]
    
    SortedArr = sorted(MyArr) 
    selectionSort(MyArr)
    
    
    if(SortedArr != MyArr):
        print(SortedArr)
        print(MyArr)
        print(False)
        break
else:
    print(True)