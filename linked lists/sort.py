from random import randint

class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next = next_node
    
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
    for x in L[::-1]:
        n = Node(x,lastNode)
        lastNode = n
    return n

def merge(L1,L2):
    root = Node(None)
    
    node = root
    while(L1 or L2):
        if(not L1):
            node.next = L2
            return root.next
        if(not L2):
            node.next = L1
            return root.next
        if(L1.data<L2.data):
            node.next = L1
            L1 = L1.next
        else:
            node.next = L2
            L2 = L2.next
        node = node.next
    return root.next

    

L1 = [randint(0, 1000) for _ in range(50)]
L2 = [randint(0, 1000) for _ in range(50)]

L1.sort()
L2.sort()

L1 = createLinkedListByList(L1)
L2 = createLinkedListByList(L2)

L1.print_list()
L2.print_list()

merge(L1,L2).print_list()







