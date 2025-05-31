from graph import *
g = Graph(4)

g.add_edge(0,1,4)
g.add_edge(0,2,1)
g.add_edge(0,3,5)
g.add_edge(1,2,6)
g.add_edge(2,3,2)

# get nodes connected to node 3
print(g.get_connected_nodes(3))

# get nodes connected to node 0
print(g.get_connected_nodes(0))
