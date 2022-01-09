x = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

def getEncodingIndex(x):
    x = x.lower()[::-1]
    index = 0
    base = 1
    for i in x:
        index += (ord(i) - ord('a')+1)*base
        base*=26

    return index


i = getEncodingIndex(x)

print(i)