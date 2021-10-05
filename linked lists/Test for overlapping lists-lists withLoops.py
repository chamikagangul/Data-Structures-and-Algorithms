from random import randint

class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)
    
    def search(node,k):
        while node and node.data!=k:
            node = node.next
        return node
    
    def insert(node,new_node):
        new_node.next = node.next
        node.next = new_node

    def delete_after(node):
        node.next = node.next.next

    def print_list(self):
        if(self == None ):
            return
        else:
            print(self.data, end =" ")
            if(self.next):
                self.next.print_list()
            else:
                print()
                return



def createLinkedListByList(L):
    lastNode =None
    isFirst = True
    for x in L[::-1]:
        n = Node(x,lastNode)
        lastNode = n
        if(isFirst):
            finalNode = lastNode
            isFirst = False
    # finalNode.next = n
    return n

def joinLists(L1,L2,n):

    r1,r2 = L1,L2
    while(L1.next):
        # print(L1.data)
        L1 = L1.next
    
    for i in range(n):
        L2 = L2.next
    L1.next = L2

    return r1,r2

def checkForOverlapping(L1,L2):
    r1 = L1
    r2 = L2
    L1Length = 0
    L2Length = 0
    while(L1.next):
        L1Length +=1
        L1 = L1.next
    while(L2.next):
        L2Length +=1
        L2 = L2.next
    
    
    if(L1Length>L2Length):
        L1,L2 = r1,r2
    else:
        L1,L2 = r2,r1


    for i in range(L1Length-L2Length):
        L1 = L1.next
    
    while(L1!=L2):
        L1=L1.next
        L2=L2.next
    else:
        return L1

    



L1 = [randint(0, 1000) for _ in range(10)]
L2 = [randint(0, 1000) for _ in range(10)]


L1 = createLinkedListByList(L1)
L2 = createLinkedListByList(L2)

L1,L2 = joinLists(L1,L2,4)

L1.print_list()
L2.print_list()

print(checkForOverlapping(L1,L2))












