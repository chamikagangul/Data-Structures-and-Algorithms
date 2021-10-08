from os import close


class Stack:
    def __init__(self):
        self.array = []

    def __init__(self,array):
        self.array = array

    def __str__(self) -> str:
        return str(self.array)

    def empty(self):
        return len(self.array)==0

    def pop(self):
        if not self.empty():
            return self.array.pop()
        else:
            return None

    def push(self,e):
        self.array.append(e)

    def len(self):
        return len(self.array)


def isWeeFormed(x):
    O = ['(','[','{']
    C = [')',']','}']
    open_brackets = Stack(x)
    close_brackets = Stack([])

    while(open_brackets.len()):
        print(open_brackets,close_brackets)
        # input()
        o_bracket = open_brackets.pop()
        if(o_bracket in O):
            o_bracket_index = O.index(o_bracket)
        else:
            o_bracket_index = -1

        if(o_bracket_index>=0):
            c_bracket = close_brackets.pop()
            if(c_bracket in C):
                c_bracket_index = C.index(c_bracket)
            else:
                c_bracket_index = -1
            
            if(o_bracket_index!=c_bracket_index):
                return False
        if(o_bracket in C):
            c_bracket_index = C.index(o_bracket)
        else:
            c_bracket_index = -1
        
        if(c_bracket_index>=0):
            close_brackets.push(o_bracket)
            
    else:
        return True

x = "{} * {}"
x = list(x)
print(isWeeFormed(x))



