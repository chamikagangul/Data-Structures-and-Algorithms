# x = int(input())
# y = x & (x-1) 
# z = x| (((x ^ y)) -1)
# print(bin(x),bin(z))\


# x = int(input())
# for i in range(100,1000):
#     if(i%x != i & (x-1)):
#         print("false")
#         break
#     else:
#         print(i)


    
x = int(input())
y = x & (x-1) 
print(y==0)
