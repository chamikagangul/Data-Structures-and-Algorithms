import util
import bintrees
import random
from BST import BST


def checkForCorrectness(root,minRange = -float("inf"),maxRange =float("inf")):
    if root is None:
        return True
    elif not  minRange <= root.data <= maxRange:
        return False
    return checkForCorrectness(root.left,minRange,root.data) and checkForCorrectness(root.right,root.data,maxRange)



def main():
    root = BST()
    primes = util.getPrimesList(10)
    random.shuffle(primes)
    for i in primes:
        root.insert(i)
    util.print2DUtil(root,0)
    root.data = 20
    isCorrect = checkForCorrectness(root)
   
    print(isCorrect)
   
if __name__ == "__main__":
    main()