x = -12312322321241231231413138978097654345678909876543234567890
print(x)  

def myStr(x):
    s = ""
    if(x<0):
        sign = "-"
        x = -x
    
    while(x):
        if(x>0):
            c = chr(x%10 + 48)
            x = x//10
            s+=c
    return sign + s[::-1]
    
print(myStr(x))