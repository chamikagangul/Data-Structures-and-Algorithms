import collections


class Stack:
    
    Count = collections.namedtuple("Count",("count","max"))

    def __init__(self):
        self.array = []
        self.count = []

    def empty(self):
        return len(self.array)==0

    def pop(self):
        if not self.empty():
            e = self.array.pop()
            m = self.max()
            if(e==m):
                self.count[-1] = self.Count(self.count[-1].count-1,e)
                if(self.count[-1].count == 0):
                     self.count.pop()
            return e


    def max(self):
        if self.empty():
            raise IndexError('maxO: empty stack') 
        return self.count[-1].max
    
    def push(self,e):
        self.array.append(e)
        if(len(self.count) == 0):
            self.count.append(self.Count(1,e))
        else:
            if(e == self.max()):
                self.count[-1] = self.Count(self.count[-1].count+1,e)
            if(e>self.max()):
                self.count.append(self.Count(1,e))





s =Stack()

s.push(13)
s.push(2)
s.push(13)
s.push(13)
s.push(12)
s.push(23)
s.push(2)
s.push(2)



print(s.array,s.count)

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()

print(s.array,s.count)