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

balanced = True
def isBalanced(root):
    global height , balanced
    
    

    height = None
    def tree_traversal(root,count):
        global height, balanced
        if(not balanced):
            return False
        
        if(root):
            # print(count,root)
            count +=1
            tree_traversal(root.left,count)
            tree_traversal(root.right,count)
            count -=1
        else:
            if(height == None):
                height = count
            else:
                if(abs(height - count)>1):
                    
                    balanced = False
                    return False

            # print(count)
        
    count = 0
    tree_traversal(root,count)


X = "ABCDEFGHIJKLMNOP"
X = list(X)

root = createTree(X)
root.left.right = None
print(isBalanced(root))


