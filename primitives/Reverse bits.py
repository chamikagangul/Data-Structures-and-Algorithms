x = 3232


print(f"{bin(x)}")

n=64
y=0
while(n):
    y |= ((x & (1<<n)) != 0) << (64-n)
    n = n -1



print(f"%b,%b",bin(x), bin(y))

# def reverse(x):
#     if(x==0):
#         return 0
#     elif(x==1):
#         return 2
#     elif(x==2):
#         return 1
#     elif(x==3):
#         return 3
#     else:

#         return 