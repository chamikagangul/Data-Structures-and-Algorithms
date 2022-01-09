T = int(input())

for _ in range(T):
    K,N = list(map(int, input().split()))
    avblKeys = list(map(int, input().split()))
    roomDict = {} 
    for i in range(N):
        

        LIST = list(map(int, input().split()))
        key, NoOfKeys = LIST[0], LIST[1]
        if(NoOfKeys!=0):
            if(not key in roomDict):
                roomDict[key] = [LIST[2:]]
            else:
                print(LIST)
                
                roomDict[key].append(LIST[2:])
        
    txt = "Case #{}: IMPOSSIBLE"
    print(txt.format(_+1))

    