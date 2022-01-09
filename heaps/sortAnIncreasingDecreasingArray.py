import random
import heapq
SortedArrays = [sorted([random.randint(1,100) for i in range(random.randint(1,10))]) for i in range(3)]


k_sortedArray = []

for arr,i in zip(SortedArrays,range(len(SortedArrays))):
    if(i%2==1):
        k_sortedArray = k_sortedArray + arr[::-1]
    else:
        k_sortedArray= k_sortedArray + arr

print(SortedArrays)
##################################################################

files = []

privous = None

tempArray = []
isIncreasing = True

for element,i in zip(k_sortedArray,range(len(k_sortedArray) )):
    if(privous is None):
        privous = element
        tempArray.append(element)
        continue
    
    if(element>=privous and isIncreasing):
        tempArray.append(element)
        privous = element
    elif(element<=privous and not isIncreasing):
        tempArray.append(element)
        privous = element
    else:
        if(not isIncreasing):
            tempArray = tempArray[::-1]
        isIncreasing = not isIncreasing
        files.append(tempArray)
        tempArray = []
        tempArray.append(element)
        privous = element


minOfArray = []

for file,i in zip(files,range(len(files))):
    minOfArray.append((file[0],i))

files = [iter(file) for file in files]
heapq.heapify(minOfArray)

SORTED = []

while(len(minOfArray)>0):
    MIN, i = heapq.heappop(minOfArray)
    SORTED.append(MIN)
    # print(i,files)
    number = next(files[i],None)
    if(number is not None):
        heapq.heappush(minOfArray,(number,i))

print(SORTED)