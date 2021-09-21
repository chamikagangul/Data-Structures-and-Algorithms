n,m= list(map(int,(input().strip().split())))

abk = []
s= []

for _ in range(m):
    x = list(map(int,(input().strip().split())))
    # x[0],x[1] = x[0]-1,x[1]-1
    s += [[x[0],x[2]],[x[1]+0.5,-x[2]]]

s.sort(key = lambda x: x[0])
# print(s)
M = -float('inf')
v = 0
for q in s:
    v+=q[1]
    # print(q[0],q[1],v)
    M = max(v,M)
print(M)
