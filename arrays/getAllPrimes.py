def isPrime(primes,n):
    for p in primes:
        if(n%p==0):
            return False
    else:
        return True

def createPrimeArray(n):
    primes = []
    is_Prime = [True for i in range(n)]
    for i in range(2,n):
        if(is_Prime[i]):
            primes.append(i)
            for j in range(i,n,i):
                is_Prime[j] = False
    print(primes)


createPrimeArray(20)