x = int(input())

i,j = list(map(int,input().strip().split()))
# x = 511
# i,j = 2,5

mask = ~(1<<i | 1<<j)

y = ((x >> i) &1) <<j | ((x >> j) &1) <<i

r = (mask&x) | y
print(bin(r),r)