import random
def bsearch(arr,x):
    def findFirstOccurance(array,i):
        x = array[i]
        while(array[i] == x and i>=0):
            i = i-1
        return i+1

    L,H = 0,len(arr)
    M = (L+H)//2

    while(L<=H):
        
        M = (L+H)//2
        if(arr[M] == x):
            return findFirstOccurance(arr,M)
        elif(arr[M] < x):
            L = M+1
        else:
            H = M-1
    else:
        return -1

arr = [random.randint(1,1000) for i in range(1000)]

s = arr[5]
arr = [44,500,500,500,500,500,3224,4,500,500,500]
s =500
arr.sort()

# print(arr,s)
index = bsearch(arr,s)
print(index,arr)