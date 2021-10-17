import utils

class Node:
    def __init__(self,data=None,left=None,right=None,parent = None) -> None:
        super().__init__()
        
        self.data = data
        self.left = left
        self.right= right
        self.parent = parent

    def __str__(self):
        return str(self.data)


def createTree(X):
    lenX = len(X)
    n = None
    if(lenX):
        n = Node(X[0])
    if(lenX>1):
        n.left = createTree(X[1:1+lenX//2])
        n.left.parent = n
    if(lenX>2):
        n.right = createTree(X[1+lenX//2:])
        n.right.parent = n
    # print(n,X)
    return n




def getLCA(n1,n2):
    DATA = ["",""]
    while(n1.parent):
        if(n1.parent.left == n1):
            DATA[0] += "0"
        if(n1.parent.right == n1):
            DATA[0] += "1"
        n1= n1.parent

    while(n2.parent):
        if(n2.parent.left == n2):
            DATA[1] += "0"
        if(n2.parent.right == n2):
            DATA[1] += "1"
        n2= n2.parent
        
    
    DATA[0] = DATA[0][::-1]
    DATA[1] = DATA[1][::-1]
    # print(DATA)
    root = n1
    x = ""
    for a,b in zip(DATA[0],DATA[1]):
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
    n2 =  root.left.right.right.left
    print(n1,n2)
    print(getLCA(n1,n2))

