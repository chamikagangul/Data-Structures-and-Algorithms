
import collections


class Stack:


    def __init__(self):
        self.array = []

    def __init__(self,array):
        self.array = array[::-1]

    def __str__(self) -> str:
        return str(self.array)

    def empty(self):
        return len(self.array)==0

    def pop(self):
        if not self.empty():
            return self.array.pop()

    def push(self,e):
        self.array.append(e)

    def len(self):
        return len(self.array)


def evaluate(stack):
    while(stack.len()>1):
        
        A = stack.pop()
        B = stack.pop()
        op = stack.pop()
        if(op == '+'):
            stack.push(A+B)
        elif(op == '-'):
            stack.push(A-B)
        elif(op == 'x'):
            stack.push(A*B)
        elif(op == '/'):
            stack.push(A/B)
        
    else:
        return stack.pop()


stack = Stack([3,4,'+',2,'x',1,'+'])

x = evaluate(stack)

print(x)