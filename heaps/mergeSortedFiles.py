import heapq, random
files = [sorted([random.randint(1,100) for i in range(5)]) for i in range(3)]


def createSortedFile(files):
    minOfAll = []
    files = [iter(file) for file  in files]
    for i,file in enumerate(files):
        element = next(file,None)
        if(element is not None):
            minOfAll.append((element,i))
    
    heapq.heapify(minOfAll)
    SORTED = []
    while(len(minOfAll)>0):
        MIN,i = heapq.heappop(minOfAll)
        SORTED.append(MIN)
        element = next(files[i],None)
        if(element is not None):
            minOfAll.append((element,i))
    return SORTED

    
        
    # return [[heapq.heappop(sortedFile) for _ in range(k)]]

print(files)
sf = createSortedFile(files)

print(sf)


# test = [random.randint(1,100) for i in range(5)]
# k = len(test)
# print(test)
# print([heapq.heappop(test) for _ in range(k)])

