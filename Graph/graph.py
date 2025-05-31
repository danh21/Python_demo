class Graph:
    def __init__ (self, n):
        self.nodes = n
        self.list = [[] for i in range (self.nodes)]
    
    def add_edge (self, s, e, w):
        self.list[s].append((e, w))
        self.list[e].append((s, w))

    def get_connected_nodes (self, s):
        return [edge[0] for edge in self.list[s]]