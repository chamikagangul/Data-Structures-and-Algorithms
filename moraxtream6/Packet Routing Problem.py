class Node:

    def __str__(self) -> str:
        return f"children :-{self.child} val:- {self.val}"
        
    def __init__(self) -> None:
        self.val = 0
        self.child = []

def clacVal(Nodes,i,end):
    if(end != i):
        for c in Nodes[i].child:
            Nodes[i].val +=clacVal(Nodes,c,end)
        return 0
    else:
        return 1

#creating data
v,e = map(int,input().strip().split())
start,end = map(int,input().strip().split())
Nodes = []
for i in range(v):
    Nodes.append(Node())
    
for i in range(e): 
    p,c = map(int,input().strip().split())
    Nodes[p-1].child.append(c-1)

clacVal(Nodes,start-1,end-1)

MAXVAL = -float('inf')
position = None
for i in range(len(Nodes)):
    
    n = Nodes[i]
    # print(n)
    if(MAXVAL<=n.val):
        MAXVAL=n.val
        position = i

print(position+1)

