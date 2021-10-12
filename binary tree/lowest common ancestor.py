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




def getLCA(root,n1,n2):
    DATA = ["",None,None]
    def travelAndFind(root,n1,n2):
        if(DATA[1] and DATA[2]):
            return
        # print(root,DATA)
        if(root == n1):
            DATA[1] = DATA[0]
            return
        if(root == n2):
            DATA[2] = DATA[0]
            return 
        x = DATA[0]
        if(root.left):
            DATA[0] = x + "0"
            travelAndFind(root.left,n1,n2)
        if(root.right):
            DATA[0] = x + "1"
            travelAndFind(root.right,n1,n2)
        DATA[0] = x
        
        
    travelAndFind(root,n1,n2)
    x = ""
    for a,b in zip(DATA[1],DATA[2]):
        if(a==b):
            x+=a
        else:
            break
    for n in x:
        if(n=="0"):
            root = root.left
        elif(n=="1"):
            root = root.right
    
    return root



if __name__ == "__main__":
    
    X = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345"
    X = list(X)
    root = createTree(X)
    # root.left = None
    utils.print_tree(root)

    n1 = root.right.right.left.right
    n2 =  root.right.right.right.left
    print(n1,n2)
    print(getLCA(root, n1,n2))

