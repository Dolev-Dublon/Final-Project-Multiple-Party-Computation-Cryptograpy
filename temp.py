import networkx as nx

Daniel = nx.Graph()
Daniel.add_edge("Tel aviv","Jerusalem", weight = 10,label="red")
Daniel.add_edge("a","s",weight=4,label="blue")
Daniel.add_edge("Tel aviv","Petah tikva", weight = 5,label="red")

#print(Daniel.edges)
graph= nx.Graph()
for node in Daniel.nodes:
    graph.add_node(node)
for edge in Daniel.edges:
    graph.add_edge(edge[0],edge[1],weight=float('inf'),label="blue")

for edge in iter(graph.edges):
# edge = next(iter(graph.edges))# print(graph[u][v])
    print(edge)
# S0=[]
# S1=[]

import itertools

nodes = [1, 2, 3, 4]  # Example list of nodes
graph = nx.Graph()  # Create an empty graph

# Generate all combinations of nodes (pairs of nodes)
node_combinations = itertools.combinations(nodes, 2)

# Add edges to the graph for each combination of nodes
for u, v in node_combinations:
    graph.add_edge(u, v)

print(len(graph.nodes))
# Print the edges in the graph
#print(graph.edges)



    


# for edge in Daniel.edges:
#     S0.append(edge)
#     S1.append(edge)
#
# S0.pop(0)
# S1.pop(1)
# print(S0)
# print(S1)
#
# S=set(S1+S0)
# print(S)