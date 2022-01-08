import itertools
import random

def findLargestSubArraySum(array):
    acc = itertools.accumulate(array)

    val = next(acc,None)
    MIN = val
    MAX = 0
    while(val!=None):
        MIN = min(MIN,val)
        MAX = max(MAX,val-MIN)
        print(val,MIN,MAX)
        val = next(acc,None)

    return MAX

array = [random.randint(-100,100) for i in range(10)]

print(array)
maxSum = findLargestSubArraySum(array)

print(maxSum)