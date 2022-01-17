import random
def quickSort(Array):

    def QuickSortInner(A,left,right):
        
        if(left>=right):
            return A
        pivot = (left + right) // 2
        
        A[pivot],A[right] = A[right], A[pivot]
        i_left= left
        i_right = right-1
        while i_left < i_right:
            
            while(A[i_left] < A[right]):
                
                i_left+=1
            while(A[i_right] > A[right]):
                i_right -=1
            # print(i_left , i_right,A , left,right)
            if(i_left <= i_right):
                A[i_left] , A[i_right] =   A[i_right],A[i_left]
        
        A[i_left],A[right] = A[right], A[i_left]
        QuickSortInner(A,left,i_left)
        QuickSortInner(A,i_left+1,right)
        
        return A
    Array = QuickSortInner(Array,0,len(Array)-1)
    return Array
    

MyArr = [ random.randint(0,100) for _ in range(10)]
SortedArr = sorted(MyArr) 
quickSort(MyArr)
print(SortedArr)
print(MyArr)
print(SortedArr == MyArr)