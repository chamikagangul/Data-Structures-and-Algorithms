def distance(a,b,graph):
    # print(f"distace between {a} , {b}")
    d=0
    visited = []
    nextVisit =[a]
    distace = {}
    while(True):
        d+=1
        nV =[]
        
        # print(f"visited :{visited}, next :{nextVisit}, dist: {distace} b: {b}")
        
        for v in nextVisit:
            if(len(b)==0):
                return distace
            B = b[:]
            for b_ in range(len(b)):
                # print(B,graph[v])
                if(b[b_] in graph[v]):
                    distace[b[b_]] = d
                    B.pop(b_)
            else:
                for x in graph[v]:
                    if(not x in visited):
                        nV.append(x)
            b=B
        visited = visited + nextVisit
        nextVisit = list(set(nV))

n,q = list(map(int,input().strip().split()))

graph = {}


for i in range(n-1):
    x,y =list(map(int,input().strip().split()))
    if(x in graph):
        graph[x] =graph[x] +[y]
    else:
        graph[x] = [y]

    if(y in graph):
        graph[y] =graph[y] +[x]
    else:
        graph[y] = [x]
    

Q = []
for i in range(q):
    x = input()
    Q.append(list(map(int,input().strip().split())))

# print(graph)


for query in Q:
    # print(f"query = {query}")
    s = 0
    for i in range(len(query)-1):
        a,b = query[i],query[i+1:]
        d = distance(a,b,graph)
        for k,v in d.items():
            s+=a*k*v
        
            
    print(s%(10**9+7))
            