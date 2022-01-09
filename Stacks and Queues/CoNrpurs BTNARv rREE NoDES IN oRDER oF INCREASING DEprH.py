import utils


class Queue:

    def __init__(self):
        self.array = []

    def __init__(self,array):
        self.array = array

    def __str__(self) -> str:
        return str(self.array)

    def empty(self):
        return len(self.array)==0

    def pop(self):
        if not self.empty():
            rslt = self.array[0]
            self.array = self.array[1:]
            return rslt
        else:
            return None

    def push(self,e):
        self.array.append(e)

    def len(self):
        return len(self.array)

class Node:
    def __init__(self,data=None,left=None,right=None) -> None:
        super().__init__()
        self.data = data
        self.left = left
        self.right= right

    def __str__(self):
        return str(self.data)


def createTree(X):
    lenX = len(X)
    n = None
    if(lenX):
        n = Node(X[0])
    if(lenX>1):
        n.left = createTree(X[1:1+lenX//2])
    if(lenX>2):
        n.right = createTree(X[1+lenX//2:])
    # print(n,X)
    return n

def createTree1():
    root = Node(314)
    root.left = Node(6)
    root.right = Node(6)

    root.left.left = Node(271)
    root.left.right = Node(561)
    
    root.right.left = Node(2)
    root.right.right = Node(271)
    root.right.right.right = Node(28)

    root.left.left.left = Node(28)
    root.left.left.right = Node(0)

    root.left.right.right = Node(3)
    root.left.right.right.left = Node(17)

    root.right.left.right = Node(1)
    root.right.left.right.left = Node(401)
    root.right.left.right.left.right = Node(641)
    root.right.left.right.right = Node(257)

    return root


def findLevels(root):
    rslt = []
    current = [root]
    while(len(current)):
        rslt.append([c.data for c in current])
        current = [child for c in current for child in (c.left,c.right) if child]
    
    return rslt
        
# <<314>, <6,6), <271,561,2,271>, <28,0,3,1,28>, <17,401.,257>, (641))

if __name__ == "__main__":
    
    root = createTree1()
    # root.left = None
    utils.print_tree(root)

    print(findLevels(root))
