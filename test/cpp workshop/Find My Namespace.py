# # finde my namespace

# count = 0
# def find_my_namespace(n):

#     def recAndCheck(n,i,ones):

#         global count
#         if(i==2*n):
#             count =count+1
#             # print(count)
#             return
#         if(i-ones<=ones):
#             recAndCheck(n,i+1,ones)
#             if(ones == n):
#                 return
#             recAndCheck(n,i+1,ones+1)
#     recAndCheck(n,0,0)
    
# # for i in range(1,5):
# #     find_my_namespace(i)
# #     print(count, "-----------------------------")

# #     count = 0 

# n = int(input())
# find_my_namespace(n)

# print(count)



#include <iostream>
#include <cmath>

def is_ok( n,  x):
    zeros = 0
    ones = 0
    for i in range(x):
        b = n >> i & 1
        if (b):
            ones +=1
            if (ones > zeros):
                return False;
        
        else:
            zeros+=1
    
    if (zeros == ones):
        return True
    else:
        return False


def space(n):

    x = 4**n
    total = 0


    for i in range(x//2,x,2):
    
        if (is_ok(i, n * 2)):
            total+=1
    
    print(total)


n = int(input())
   
if (n<1):
    print(0)
else:
    space(n)
    