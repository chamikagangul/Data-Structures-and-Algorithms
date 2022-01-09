s =[]
for i in range(3):
    s.append(list(map(int,input().strip().split())))

def getDiff(A,B):
    t = 0
    for i in range(3):
        for j in range(3):
            # print(A[i][j],B[i][j])
            t = t + abs(A[i][j]-B[i][j])
    return t


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

cost = 100

magic = [[[8,1,6],[3,5,7],[4,9,2]], [[6,1,8],[7,5,3],[2,9,4]],[[4,9,2],[3,5,7],[8,1,6]] , [[2,9,4] ,[7,5,3],[6,1,8]]]

for m in magic:
    cost  = min(cost,getDiff(m,s))
    cost  = min(cost,getDiff(transpose(m),s))

print(cost)