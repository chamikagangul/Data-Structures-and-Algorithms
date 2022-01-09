#!/bin/python3

import math
import os
import random
import re
import sys

def poisonousPlants(plants):
    START = 0
    start = 0
    END = 0
    end = 0
    M = 0
    c = 0
    MIN = float('inf')
    for i in range(len(plants)):
        if(MIN>=plants[i]):
            MIN=plants[i]
            start = i
            end=i
        else:
            end+=1
        
        if(end-start>M):
            M = end-start
            START = start
            END = end
    
        # print(start,end,M,START,END)
    plants = plants[START:END+1]
    # print(plants)
    
    c = 0
    while(True):
        nArray = [plants[0]]
        for i in range(1,len(plants)):
            if(plants[i-1]>=plants[i]):
                nArray.append(plants[i])
        # print(nArray)
        
        if(len(nArray) == len(plants)):
            return c
        c+=1
        plants = nArray




if __name__ == '__main__':
    

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)


    

    print(str(result))
    # fptr.write(str(result) + '\n')

    # fptr.close()
