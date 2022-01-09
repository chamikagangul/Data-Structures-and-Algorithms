import random
def bsearch(arr,s):
    x,y = 0,len(arr)-1
    gessIndex = int((x+y)/2)
    while arr[gessIndex] != s  and x!=gessIndex and y!=gessIndex: 
        print(gessIndex)
        
        if(arr[gessIndex]<s):
            x = gessIndex+1
        elif(arr[gessIndex]>s):
            y = gessIndex-1
        else:
            break
        gessIndex = int((x+y)/2)
        
    
    
    if(arr[gessIndex] == s):
        gessIndex = gessIndex
    elif(arr[x] == s):
        gessIndex = x
    elif(arr[y] == s):
        gessIndex = y
    else:
        gessIndex = None
    
    


    if(gessIndex == None):
        print(gessIndex)
    else:
        print(gessIndex, arr[gessIndex])


arr = [random.randint(1,1000) for i in range(1000)]

s = arr[5]
s =500
arr.sort()

print(arr,s)
bsearch(arr,s)