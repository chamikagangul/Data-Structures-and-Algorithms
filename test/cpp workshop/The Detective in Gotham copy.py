# travel to all nodes in the graph

class  Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.distances = {}

    def add_node(self, value):
        self.nodes.append(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges.append((from_node, to_node, distance))
        self.distances[(from_node, to_node)] = distance

    def get_edges(self):
        return self.edges

    def get_distances(self):
        return self.distances

    def get_nodes(self):
        return self.nodes
    
    def get_path(self, from_node, to_node):
        return self.distances[(from_node, to_node)]
        