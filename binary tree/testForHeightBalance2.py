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
balanced = True
def isBalanced(root):
    def tree_traversal(root):         
        if(root):
            # print(count,root)
            leftHeight,Lbalaced = tree_traversal(root.left)
            rightHeight,Rbalaced = tree_traversal(root.right)
            if(Lbalaced and Rbalaced and abs(leftHeight-rightHeight)<=0):
                return max(leftHeight,rightHeight)+1, True
            else:
                # print(root,leftHeight,Lbalaced,rightHeight,Rbalaced)
                return 0,False
        else:
            return 0,True

            # print(count)
    return tree_traversal(root)


X = "ABCDEFGHIJKLMNO"
X = list(X)

root = createTree(X)
# root.left.right = None
utils.print_tree(root)

print(isBalanced(root))


