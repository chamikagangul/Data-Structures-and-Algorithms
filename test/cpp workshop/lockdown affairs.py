from collections import defaultdict


class Graph():
    def _init_(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def remove_node(self, node):
        for n, edge in self.edges.items():
            if node in edge:
                edge.remove(node)
                self.weights.pop((n, node))
                self.weights.pop((node, n))
        self.edges.pop(node)

def dijsktra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)
                                   ] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return []

        current_node = min(next_destinations,
                           key=lambda k: next_destinations[k][1])
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path

def getInputs():
    N,E = map(int,input().split())
    edges = []
    locked =[]
    for i in range(E):
        u,v,= map(int,input().split())
        edges.append((u,v,1))
    L = int(input())
    for i in range(L):
        locked.append(int(input()))
    return N,edges,locked

def answer():
    N,edges,locked = getInputs()

    graph = Graph()
    for edge in edges:
        graph.add_edge(*edge)

    for l in locked:
        graph.remove_node(l)

    # print(N,edges,locked)
    route = dijsktra(graph, 0, N-1)
    if(len(route)==0):
        print(-1)
    else:
        print(len(route)-1)

answer()