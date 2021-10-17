import utils

class Node:
    def __init__(self,data=None,left=None,right=None) -> None:
        super().__init__()
        self.data = data
        self.left = left
        self.right= right

    def __str__(self):
        return str(self.data)


def createTree(X,d):
    lenX = len(X)
    n = None
    if(lenX):
        n = Node(d)
    if(lenX>1):
        n.left = createTree(X[1:1+lenX//2],"0")
    if(lenX>2):
        n.right = createTree(X[1+lenX//2:],"1")
    # print(n,X)
    return n




def getSUM(root):
    def calcSUM(root,path):
        if(root):
            return calcSUM(root.left,path+root.data) + calcSUM(root.right,path+root.data)
        else:
            # print(path)
            return int("0b"+path,2)
    return calcSUM(root,root.data)


if __name__ == "__main__":
    
    X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345"
    X = list(X)
    root = createTree(X,"1")
    # root.left = None
    utils.print_tree(root)

  
    print(getSUM(root))

