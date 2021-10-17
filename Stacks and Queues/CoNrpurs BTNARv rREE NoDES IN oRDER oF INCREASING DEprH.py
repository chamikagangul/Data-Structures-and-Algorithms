import utils

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

    root.left.right = Node(2)
    # root.left.left = Node(4)
    root.right.left = Node(2)

    root.left.right.right = Node(3)
    root.right.left.left = Node(3)
    return root

def checkForSymmetric(root):
    def isMirror(n1,n2):
        # print(n1,n2)
        if(n1 and n2):
            return n1.data == n2.data and isMirror(n1.left,n2.right) and isMirror(n1.right,n2.left)
        elif(n1 == None and n2==None):
            return True
        else:
            return False

    return isMirror(root.left,root.right)
        


if __name__ == "__main__":
    
    root = createTree1()
    # root.left = None
    utils.print_tree(root)

    print(checkForSymmetric(root))
