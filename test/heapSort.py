
import random

def heapify(Arr,i,n):


    larger = i
    left = 2*i + 1
    right = 2*i+2

    if(left<n and Arr[larger] < Arr[left]): 
        larger = left
    if(right<n and Arr[larger] < Arr[right]): 
        larger = right
    if(larger!=i):
        Arr[larger] , Arr[i] = Arr[i], Arr[larger]
        heapify(Arr,larger,n)

def heapSort(A):
    lenA = len(A)
    for i in range(lenA//2-1,-1,-1):
        heapify(A,i,lenA)
    
    for i in range(lenA-1,-1,-1):
        A[i] , A[0] = A[0], A[i]
        
        heapify(A,0,i)
        


MyArr = [ random.randint(0,100) for _ in range(10)]

heapSort(MyArr)
print(MyArr)