import random
def bsearch(arr,x):
    L,H = 0,len(arr)
    M = (L+H)//2

    while(L<=H):
        
        M = (L+H)//2
        if(arr[M] == x):
            return M
        elif(arr[M] < x):
            L = M+1
        else:
            H = M-1
    else:
        return -1

arr = [random.randint(1,1000) for i in range(1000)]

s = arr[5]
s =500
arr.sort()

# print(arr,s)
index = bsearch(arr,s)
print(index)