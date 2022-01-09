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
        input()
        if(self == None ):
            return
        else:
            print(self.data, end =" ")
            if(self.next):
                self.next.print_list()
            else:
                print()
                return



def createLinkedListByList(L,i_):
    i = len(L) - i_
    # print(i,i_,len(L))
    lastNode =None
    isFirst = True
    count = 0
    for x in L[::-1]:
        n = Node(x,lastNode)
        lastNode = n
        if(isFirst):
            finalNode = lastNode
            isFirst = False
        if(i==count):
            finalNode.next = n
        count+=1
    return n

def isCyclic(LL):
    def getCycleLength(node):
        x = node.next
        count = 1
        while(x!=node):
            x = x.next
            count+=1
        return count
    slow = LL
    fast = LL.next
    go = False
    while(slow!=fast):
        # print("isCyclic- ",slow,fast)
        if(fast == None):
            return None

        fast = fast.next
        if(go):
            slow= slow.next
        go = ~go  
    
    cycleLen = getCycleLength(slow)
    itr1 = LL
    itr2 = LL
    for _ in range(cycleLen):
        itr1 = itr1.next
    
    while(itr1!=itr2):
        itr1,itr2 = itr1.next,itr2.next
    return itr1




L1 = [randint(0, 1000) for _ in range(10)]

print(L1,)
L1 = createLinkedListByList(L1,3)


print(isCyclic(L1))
# L1.print_list()

# L1.print_list()










