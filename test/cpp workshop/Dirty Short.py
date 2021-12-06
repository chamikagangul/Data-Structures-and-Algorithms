class Node:
    def __init__(self, data):
        self.data = data
        self.next = []

    def __str__(self) -> str:
        return str(self.next)


t = int(input())

for i in range(t):
    I,C = map(int,input().split())
    nodes = [Node(i) for i in range(I)]
    for j in range(C):
        a,b = map(int,input().split())
        nodes[a-1].next.append(nodes[b-1])
    
    head = nodes[0]

    COUNT = None
    visited = False
    def dfs(node,c):
        global COUNT, visited
        if len(node.next) == 0:
            # print(c,COUNT)
            if COUNT == None:
                COUNT= c
            elif COUNT != c:
                visited = True
                print("YES")
            return

        for i in node.next:
            dfs(i,c+1)
    
        

    dfs(head,0)
    if not visited:
        print("NO")
    