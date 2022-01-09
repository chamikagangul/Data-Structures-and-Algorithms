x= 43543534
y=5424533

def add(a,b):
    ans = 0
    cf=0
    x=1
    t1,t2=a,b
    while(t1|t2|cf):
        # print(t1,t2,cf,ans)
        t1=t1>>1
        t2=t2>>1
        if(cf):
            ans = ans| ((a&x)^(b&x)^x)
            cf = (a&x)|(b&x)
        else:
            ans = ans| ((a&x)^(b&x))
            cf = (a&x)&(b&x)

        x = x<<1
        
        # input()
    return ans


def mul(x,y):
    i = 0
    ans = 0
    while(x):
        a = x & 1
        if(a == 1):
            ans = add(ans, y<<i)
        i = add(i,1)
        x = x>>1
        # print(x,y,i,a)
        
    
    return ans

# print(mul(13,22) == )
print(mul(x,y)==x*y)