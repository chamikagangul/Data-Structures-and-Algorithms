import heapq, itertools

def top_k(k,stream):
    min_heap = [(len(s),s) for s in stream]
    heapq.heapify(min_heap)
    print(min_heap)

    # for s in stream:
    #     heapq.heappushpop(min_heap,(len(s),s))
    print(heapq.nsmallest(k,min_heap))


stream = ["a","sdad","dfhjiof22","gyer","ahjkefbe","asjfbek"]
k = 6
top_k(k,stream)