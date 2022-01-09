def weight(x):
    i = 0
    while(x):
        i+=1
        x &= x - 1
    return i


def findSame(x):
    mask1 =  x& -x   
    if(mask1!=1):
        mask = mask1 | mask1>>1
    else:
        mask2 =  ~x& -~x
        mask = mask2 | mask2>>1

    # print(bin(mask1),bin(mask2),bin(mask))
    y = x ^ mask
    return y
# test algo
for i in range(0,10000000):
    # a = i+i
    y = findSame(i)
    if weight(i) != weight(y):
        print("err",i,y,weight(i),weight(y))
        break
else:
    print("all good")

