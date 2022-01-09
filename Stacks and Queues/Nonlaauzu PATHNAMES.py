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

def normalize(path):
    path_stack = Stack([])
    for dir in path:
        if(dir==".."):
            path_stack.pop()
        elif(dir!='.'):
            path_stack.push(dir)
    print(path_stack)


x = "/usr/llb/../bin/gcc and scripts//./../scripts/awkscripts/././"

x = "sc//./../tc/awk/././"
path = x.split("/")
normalize(path)