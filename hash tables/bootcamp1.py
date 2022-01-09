import functools


def string_hash(s,modulus):
    MULT = 997
    def hash_func(k,c):
        
        rslt = (k*MULT+ord(c)) % modulus
        # print(k,c,rslt)
        return rslt
    """
    Hash function for strings.
    """
    
    return functools.reduce(hash_func, s, 0) 

print(string_hash("hello",10000000000000000000000000000000))