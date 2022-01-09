class BST:

    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if(self.data):
            if(self.data<data):
                if(self.right is None):
                    self.right = BST(data)
                else:
                    self.right.insert(data)
            elif(self.data>data):
                if(self.left is None):
                    self.left = BST(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data
    def __str__(self) -> str:
        return str(self.left.data if self.left else "None" )+ " " + str(self.data)+" " + str(self.right.data if self.right else "None")

