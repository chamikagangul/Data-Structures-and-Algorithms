# def divide (x , y) :
#     result, power = 0, 32
#     y_power=y<<power
#     while x >= y:
#         while y_power > x:
#             y_power >>= 1
#             power -= 1
#         result += 1 << power
#         x -= y_power
#     return result

# print(divide(100,3))
a,b = 2432423,33
def divide(x,y):
    k = 0
    ans = 0
    while(x>y):
        # print(k,x)
        # input()
        while(x>=(y<<k)):
            # print(x)
            # input()
            x = x - (y<<k)
            ans+=1<<k
            k=k+1
         
        k=k-1
    return ans
print(divide(a,b), a//b)


