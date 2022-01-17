import random
def quickSort(Array):

    def QuickSortInner(A,left,right):
        if(left>=right):
            return A
        pivot = (left + right) // 2
      
        A[pivot],A[right] = A[right], A[pivot]
        
        i_left= left
        i_right = right-1
        while(True):
            while(i_left < right and A[i_left] <= A[right]):
                i_left+=1
            while(i_right > 0 and A[i_right] >= A[right]):
                i_right -=1
            if(i_left>=i_right):
                break
            A[i_left] , A[i_right] =   A[i_right],A[i_left]
        A[i_left],A[right] = A[right], A[i_left]
        QuickSortInner(A,left,i_left-1)
        QuickSortInner(A,i_left+1,right)
        return A
    Array = QuickSortInner(Array,0,len(Array)-1)
    return Array
    
for i in range(1000):
    MyArr = [ random.randint(0,200) for _ in range(100)]
    
    SortedArr = sorted(MyArr) 
    quickSort(MyArr)
    
    
    if(SortedArr != MyArr):
        print(False)
        break
else:
    print(True)