import util
import bintrees
import random
from BST import BST

def findLargeForGivenInput(input, tree):
    # print(tree.data,input)
    if(tree.data <= input):
        # print("++++++++++++++++ " + str(tree))
        if(tree.right == None):
            return None
        else:
            return findLargeForGivenInput(input, tree.right)
    else:
        # print("-------- ", tree)
        if(tree.left == None):
            return tree.data
        else:
            tempData =  findLargeForGivenInput(input, tree.left)
            if(tempData == None):
                return tree.data
            else:
                return tempData

def main():
    root = BST()
    primes = util.getPrimesList(10)
    random.shuffle(primes)
    for i in primes:
        root.insert(i)
    # util.print2DUtil(root,0)
    
    ans = findLargeForGivenInput(100, root)
    print(ans)
   
    
   
if __name__ == "__main__":
    main()