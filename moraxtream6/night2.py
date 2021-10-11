import sys
from collections import deque
 

# Python program to print all permutations with
# duplicates allowed
 
 # backtrack
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.

 
# A queue node used in BFS
class Node:
    # (x, y) represents chessboard coordinates
    # `dist` represents its minimum distance from the source
    def __str__(self) -> str:
        return f"{self.x} {self.y}"

    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
 
    # As we are using `Node` as a key in a dictionary,
    # we need to override the `__hash__()` and `__eq__()` function
    def __hash__(self):
        return hash((self.x, self.y, self.dist))
 
    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
 
 
# Below lists detail all eight possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
 
 
# Check if (x, y) is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)
 
 
# Find the minimum number of steps taken by the knight
# from the source to reach the destination using BFS
def findShortestDistance(src1, dest1, N):
    src = Node(src1.x-1,src1.y-1)
    dest = Node(dest1.x-1,dest1.y-1)
    # print(src,dest,N)
 
    # set to check if the matrix cell is visited before or not
    visited = set()
 
    # create a queue and enqueue the first node
    q = deque()
    q.append(src)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and process it
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
 
        # if the destination is reached, return distance
        if x == dest.x and y == dest.y:
            return dist
 
        # skip if the location is visited before
        if node not in visited:
            # mark the current node as visited
            visited.add(node)
 
            # check for all eight possible movements for a knight
            # and enqueue each valid movement
            for i in range(len(row)):
                # get the knight's valid position from the current position on
                # the chessboard and enqueue it with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]
 
                if isValid(x1, y1, N):
                    q.append(Node(x1, y1, dist + 1))
 
    # return infinity if the path is not possible
    return sys.maxsize
 

def createNode(position):
    x= ord(position[0]) -96
    y = int(position[1])
    return Node(x,y)

# def shortest(knight, pieces,n,count):
#     if(count == 0):
#         return 0,0
#     shortestDistance = float('inf')
#     position = None
#     for i in range(len(pieces)):
#         # print(pieces[i])
#         if(i<len(pieces)-1):
#             distance = findShortestDistance(knight, pieces[i], n) + shortest(pieces[i],pieces[:i] + pieces[i+1:],n,count-1)[0]
#         else:
#             distance = findShortestDistance(knight, pieces[i], n) + shortest(pieces[i],pieces[:i],n,count-1)[0]
        
#         if(shortestDistance > distance):
#             shortestDistance = distance
#             position = i
#     return shortestDistance,position

def createTable(pieces,n):
    lenPieces = len(pieces)

    table = [[0 for _ in range(lenPieces)] for _ in range(lenPieces)]
    for i in range(lenPieces):
        for j in range(lenPieces):
            table[i][j] = findShortestDistance(pieces[i], pieces[j], n)

    return table

def calculateDist(a,table):
    dist = 0
    for i in range(1,len(a)):
        # print(f"{table[a[i-1]][a[i]]} " , end=' ')
        dist+= table[a[i-1]][a[i]]
    return dist


def permute(a, l, r):
    global table,pieces,MIN_
    if l==r:
        if(a[0] == 0):
            MIN_ = min(MIN_,calculateDist(a,table))
        return
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            x = permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


if __name__ == '__main__':
    global pieces,MIN_
    MIN_ = float('inf')
    pieces = []

    INPUT = input().strip().split()
    n = int(INPUT[0])
    N = int(INPUT[1])
    pieces.append(createNode(INPUT[2]))

    INPUT = input().strip().split()
    for p in INPUT:
        pieces.append(createNode(p))
        
    if len(pieces) == n*n - 1:
        print(n*n - 1)
    else:
        table = createTable(pieces,n)
        a= [i for i in range(N+1)]
        permute(a, 0, len(a)-1)
        
    # src = Node(3,1)    # source coordinates
    # dest = Node(8,3)   # destination coordinates
 
    # print("The minimum number of steps required is",
    #       findShortestDistance(src, dest, n))

    print(MIN_)