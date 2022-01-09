def findWalls(L):
    maxLen = 0
    maxSoFar = 0
    maxSoFarI = 0
    left = 0
    right = 0
    for i in range(len(L)-1):
        height = L[i]
        if(i-maxSoFarI>=maxLen):
            maxLen = i-maxSoFarI
            left = maxSoFarI
            right = i
           


        if(maxSoFar<height):
            maxSoFar = height
            maxSoFarI = i
        

    return (left,right)

        


t = int(input())
for _ in range(t):
    V, p = map(int,input().strip().split())
    L = list(map(int,input().strip().split()))
    pillers = findWalls(L)
    a,b = pillers[0],pillers[1]

    cost = 2*V/(b-a) - (L[a] + L[b])
    print(a,b)
    
    print("{:.3f}".format(max(cost,0)))