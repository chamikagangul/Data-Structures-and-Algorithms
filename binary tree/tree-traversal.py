class Node:
    def __init__(self,data=None,left=None,right=None) -> None:
        super().__init__()
        self.data = data
        self.left = left
        self.right= right

    def __str__(self) -> str:
        return self.data


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


def tree_traversal(root):

    if(root):
        
        tree_traversal(root.left)
        tree_traversal(root.right)
        print(root.data)

X = "ABCDEFGHIJKLM"
X = list(X)

root = createTree(X)
tree_traversal(root)


