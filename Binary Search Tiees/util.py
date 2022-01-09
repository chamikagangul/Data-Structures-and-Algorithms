COUNT = [10]

def print2DUtil(root, space) :
 
    # Base case
    if (root == None) :
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.data)
 
    # Process left child
    print2DUtil(root.left, space)

def getPrimesList(n):
    primes = [2]
    x = 3
    while len(primes) < n:
        for i in primes:
            if x % i == 0:
                break
        else:
            primes.append(x)
        x += 2
    return primes


