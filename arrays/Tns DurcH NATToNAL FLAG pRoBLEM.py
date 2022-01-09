# x = [0,2,3,5,3,2,1,4,3,8,7,6,5,3,2,4,5]
# pivot = 3
# x.append(0)
# for i in range(len(x)-1):
#     if x[i]>x[pivot] and i<pivot:
#         x = x[:i] +x[i+1:] +[x[i]]
#         pivot = pivot-1
#     elif x[i]<x[pivot] and i>pivot:
#         x = [x[i]] + x[:i] +x[i+1:]
#         pivot = pivot+1
#     elif x[i]==x[pivot]:
#         y = x[i]
#         x =  x[:i] +x[i+1:]
#         x.insert(pivot,y)
#     print(i,pivot,x)


# x = [0,2,3,5,3,2,1,4,3,8,7,6,5,3,2,4,5]

import random
def dutchFlag(x,pivot):
    small,equal,large = 0,0,len(x)-1
    while(equal<=large):
        if(x[equal]<pivot):
            x[equal],x[small] =x[small],x[equal]
            small,equal = small+1,equal+1
        elif(x[equal]>pivot):
            x[equal],x[large] =x[large],x[equal]
            large-=1
        else:
            equal+=1
    return x


# x = [0,2,3,5,3,2,1,4,3,8,7,6,5,3,2,4,5]

x = [random.randint(0,3) for _ in range(100)]
print(x)

print(dutchFlag(x,1))
print(dutchFlag(x,2))





