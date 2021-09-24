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

    def merge(self,L1,L2):
        if(not L1):
            self.next = L2
            return 
        if(not L2):
            self.next = L1
            return 
        if(L1.data<L2.data):
            self.next = L1
            L1 = L1.next
        else:
            self.next = L2
            L2 = L2.next
        self.next.merge(L1,L2)

def createLinkedListByList(L):
    lastNode =None
    for x in L[::-1]:
        n = Node(x,lastNode)
        lastNode = n
    return n


L1 = [randint(0, 1000) for _ in range(3)]
L2 = [randint(0, 1000) for _ in range(3)]

L1.sort()
L2.sort()

L1 = createLinkedListByList(L1)
L2 = createLinkedListByList(L2)

L1.print_list()
L2.print_list()

node = Node(None)
node.merge(L1,L2)

node.print_list()









