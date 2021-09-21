x = 12312322321241231231413138978097654345678909876543234567890
print(x)  

def myStr(x):
    s = ""
    while(x):
        c = chr(x%10 + 48)
        x = x//10
        s+=c
    return s[::-1]
    
print(myStr(x))