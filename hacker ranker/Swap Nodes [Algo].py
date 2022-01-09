#!/bin/python

import math
import os
import random
import re
import sys
sys.setrecursionlimit(1500)
#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    def __init__(self,value):
        self.data=value
        self.children=[] 
        self.left = None
        self.right = None
        self.level=0
        self.parent = None
        self.next =None
        self.previous =None
        

    def __str__(self):
        return str(self.data)

    def getVal(self):
        return self.data

    def printMe(self):
        print("--------------------------------")
        print(f"{self.previous} -- {self.data} -- {self.next}")
        print(f"  {self.left}    {self.right}")
        print("--------------------------------")

    def getNext(self):
        if(len(self.children)):
            return self.children[0]
        else:
            if(self.next):
                return self.next.getNext()
        return None

    def getPrevious(self):
        if(len(self.children)):
            return self.children[-1]
        else:
            if(self.previous):
                return self.previous.getPrevious()
        return self

    def travel(self):
        x = []
        if(self.left != None):
            x +=self.left.travel() 
        x.append(self.data)
        if(self.right != None):
            x +=self.right.travel() 
        return x

def swap(root,index):
    node = root
    while(node.next):
        if(node.level % index == 0):
            node.left,node.right = node.right,node.left
        node = node.next
    return root
    


def createTree(indexes):
    root = Node(1)
    root.level =1
    node = root

    for index in indexes:
        if(node.previous):
            previous=node.previous.getPrevious()
        else:
            previous = node.getPrevious()

        if(index[0]!=-1):
            node.left = Node(index[0])
            node.left.parent = node
            node.left.level = node.level+1
            node.left.previous = previous
            if(previous):
                node.left.previous.next = node.left

            node.children.append(node.left)
        
        if(index[1]!=-1):
            node.right = Node(index[1])
            node.right.parent = node
            node.right.level = node.level+1
            if(index[0]!=-1):
                node.right.previous = node.left
                
            else:
                node.right.previous = previous

            if(previous):
                node.right.previous.next = node.right
            node.children.append(node.right)
        if(node.next==None and len(node.children)>0):
            node.next = node.children[0]
        # node.printMe()
        if(node.next!=None):
            node = node.next
    return root




def swapNodes(indexes, queries):
    # Write your code here
    root = createTree(indexes)

    x= []
    for q in queries:
        root = swap(root,q)
        x.append(root.travel())
    
    return x

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')

    # fptr.close()
