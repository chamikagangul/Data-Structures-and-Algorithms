import random
def bsearch(arr):
    L,H = 0,len(arr)
    M = (L+H)//2

    while(L<=H):
        
        M = (L+H)//2
        if(arr[M] == M):
            return M
        elif(arr[M] < M):
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
index = bsearch(arr)
print(index, arr[index])