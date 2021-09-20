
class Graph:
    def __init__(self,graph):
        self.V = len(graph)
        self.graph = graph

    def findminDistance(self,visited, distance):
        MIN = float('inf')
        index = None
        for i in range(len(distance)):
            if(visited[i]==False and MIN>distance[i]):
                MIN = distance[i]
                index = i
        # print(visited,distance,index)
        return index

    def dijkstra(self,start):
        visited = [False] * self.V
        distance = [float('inf')]*self.V
        distance[start] = 0
        for i in range(self.V):
            m = self.findminDistance(visited, distance)
            visited[m] =True
            # print(distance,visited,m)
            for j in range(self.V):
                if(self.graph[m][j]>0 and visited[j] == False and   distance[j]> distance[m]+self.graph[m][j]):
                    distance[j] = distance[m]+self.graph[m][j]
            
        return distance
            

n,q = list(map(int,input().strip().split()))

graph = [[0 for col in range(n)] for row in range(n)]


for i in range(n-1):
    x,y =list(map(int,input().strip().split()))
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

g = Graph(graph)


Q = []
for i in range(q):
    x = input()
    Q.append(list(map(int,input().strip().split())))


dist =[]
for i in range(len(graph)):
    
    dist.append(g.dijkstra(i))
    print(i)

for q in Q:
    s=0
    for i in range(len(q)-1):
        dis = dist[q[i]-1]
        for j in range(i+1,len(q)):
            
            s+= q[i] * q[j]* dis[q[j]-1]
            # print(q,g.dijkstra(q[i]-1),i,j,s)
            
    print(s%(10**9 +7))