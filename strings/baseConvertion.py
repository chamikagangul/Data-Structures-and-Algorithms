x = "615"

b1 = 7
b2 = 13

def convertBase(x,b1,b2):
    y=""
    temp = 0
    m = 1
    for e in x[::-1]:
        
        temp += (ord(e) - ord('0')) * m
        m *=b1
        
    while(temp):
        a = temp%b2
        if(a<=9):
            y+= chr(a+ord('0'))
        else:
            y+= chr(a+ord('A')-10)
        temp = temp//b2
    return y[::-1]

y = convertBase(x,b1,b2)

print(y)