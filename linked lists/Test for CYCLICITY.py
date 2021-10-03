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
    isFirst = True
    for x in L[::-1]:
        n = Node(x,lastNode)
        lastNode = n
        if(isFirst):
            finalNode = lastNode
            isFirst = False
    finalNode.next = n
    return n

def isCyclic(LL):
    slow = LL
    fast = LL.next
    go = False
    while(slow!=fast):
        if(fast == None):
            return True

        fast = fast.next
        if(go):
            slow= slow.next
        go = ~go  
    else:
        return False


L1 = [randint(0, 1000) for _ in range(10)]


L1 = createLinkedListByList(L1)


print(isCyclic(L1))
# L1.print_list()










