# x = [1,243,5,45,4,346,3,532,4,325,43,6,4,63,7,56,8,78,6,9,6,6,43,35,3]

# MAX = x.pop()


# while(x):
#     MAX = max(MAX,x.pop())

# print(MAX)

import collections


class Stack:
    ElementWithCasedMax = collections.namedtuple("ElementWithCashedMax",("element","max"))

    def __init__(self):
        self.array = []

    def empty(self):
        return len(self.array)==0

    def pop(self):
        if not self.empty():
            self.array.pop()

    def max(self):
        if self.empty():
            raise IndexError('maxO: empty stack') 
        return self.array[-1].max
    
    def push(self,e):
        self.array.append(self.ElementWithCasedMax(e,e if self.empty() else max(e,self.max())))


s =Stack()

s.push(13)
s.push(12)
s.push(23)
s.push(2)
s.push(2)



print(s.max())