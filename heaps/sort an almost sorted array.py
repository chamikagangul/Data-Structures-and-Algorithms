import heapq
k=2
kSortedArray = [3,-1,2,6,4,5,8]


def sortKSortedArray(kSortedArray, k):
    heapList = kSortedArray[:k+1]
    heapq.heapify(heapList)
    
    for i in range(k+1, len(kSortedArray)):
        
        kSortedArray[i-k-1] = heapq.heappop(heapList)
        heapq.heappush(heapList, kSortedArray[i])

    for i in range(len(kSortedArray)-k-1, len(kSortedArray)):
        kSortedArray[i] = heapq.heappop(heapList)
    return kSortedArray
    

sortedArray = sortKSortedArray(kSortedArray, k)

print(sortedArray)

