import random
def bubbleSort(Array):
    ArrLen = len(Array)
    lastSwapIndex = ArrLen
    lastSortIndex = ArrLen
    while(lastSortIndex):
        print(lastSwapIndex)
        lastSortIndex = 0
        for j in range(1,lastSwapIndex):
           
            if(Array[j-1] > Array[j]):
                lastSortIndex = j
                Array[j-1] , Array[j] = Array[j] , Array[j-1]
        lastSwapIndex = lastSortIndex

    print(Array)


MyArr = [ random.randint(0,100) for _ in range(10)]
# MyArr.sort()
bubbleSort(MyArr)