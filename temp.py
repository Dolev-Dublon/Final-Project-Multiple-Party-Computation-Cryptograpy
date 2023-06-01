import networkx as nx

Daniel = nx.Graph()
Daniel.add_edge("Tel aviv","Jerusalem", weight = 10,label="red")
Daniel.add_edge("a","s",weight=4,label="blue")
Daniel.add_edge("Tel aviv","Petah tikva", weight = 5,label="red")

S0=[]
S1=[]

for edge in Daniel.edges:
    S0.append(edge)
    S1.append(edge)

S0.pop(0)
S1.pop(1)
print(S0)
print(S1)

S=set(S1+S0)
print(S)