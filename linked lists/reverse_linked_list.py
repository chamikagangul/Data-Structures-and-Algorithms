
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
    def reverseList(self,s,f):
        node = self
        
        y=None
        head = Node(0)
        head.next = self
        x = head
        prev = None
        while(True):
            
            n = node.next

            if(node.index == s-1):
                x = node
            elif(node.index == s):
                y  = node
            elif(node.index == f):
                if s==0:
                    head.next = node
                
                x.next=node
                y.next=node.next
                node.next = prev
                break
            elif(s<node.index and node.index < f):
                node.next = prev

            prev = node
            node = n

        root = head.next
        root.print_list()

def createLinkedListByList(L):
    lastNode =None
    i=len(L)
    for x in L[::-1]:
        n = Node(x,lastNode)
        i-=1
        n.index = i
        lastNode = n
        

    return n



x = [1,2,3,4,5,6,7,8,9]

root = createLinkedListByList(x)

root.print_list()

root.reverseList(0,5)
