import sys
from collections import deque
 
 
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


def shortestDist(knight,pieces,n):
    if(len(pieces) ==  0):
        return 0
    MIN_dist = float('inf')
    for i in range(len(pieces)):
        if(i<len(pieces)-1):
            d = findShortestDistance(knight, pieces[i], n) + shortestDist(pieces[i],pieces[:i] + pieces[i+1:],n)
        else:
            d = findShortestDistance(knight, pieces[i], n) + shortestDist(pieces[i],pieces[:i],n);
        MIN_dist = min(MIN_dist,d)
    return MIN_dist

if __name__ == '__main__':
    
    pieces = []

    INPUT = input().strip().split()
    n = int(INPUT[0])
    N = int(INPUT[1])
    knight = createNode(INPUT[2])

    INPUT = input().strip().split()
    for p in INPUT:
        pieces.append(createNode(p))

    # print(shortestDist(knight,pieces,n))

    position = None
    SUM = []
    ## calculating min disstance and move
    for k in range(N):
        pieces
        while(len(pieces)):
            shortestDistance = float('inf')
            # print(shortestDistance)
            for i in range(len(pieces)):
                # print(pieces[i])
                distance = findShortestDistance(knight, pieces[i], n)
                if(shortestDistance > distance):
                    shortestDistance = distance
                    position = i
            
            SUM+=(shortestDistance)
            knight = pieces[position]
            del pieces[position]
 

    # src = Node(3,1)    # source coordinates
    # dest = Node(8,3)   # destination coordinates
 
    # print("The minimum number of steps required is",
    #       findShortestDistance(src, dest, n))