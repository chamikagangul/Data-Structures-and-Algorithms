import functools

def primeNumberList(n):
    """
    Generate a list of prime numbers.
    """
    primes = [2]
    i = 3
    while(len(primes) < n):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i+=2
    return primes

def string_hash(s):
    primes = primeNumberList(26)
    def hash_func(k,c):
        
        rslt =  primes[ord(c) - 97] * k
        
        return rslt
    """
    Hash function for strings.
    """
    
    return functools.reduce(hash_func, s, 1) 


anagramWordList = ["hello","world","helloworld","worldhello","worlhdello"]

angramDict = {}
for word in anagramWordList:
    h = string_hash(word)
    if h in angramDict:
        angramDict[h].append(word)
    else:
        angramDict[h] = [word]

print(angramDict)