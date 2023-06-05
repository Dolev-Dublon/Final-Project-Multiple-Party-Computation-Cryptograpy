import math
import networkx as nx


def ASPS(graph):

    ## phase 1 : set graph edges to blue
    for u,v in graph.edges:
        graph[u][v]["label"]="blue"

    ## phase 2 : create the public graph
    public_graph =  nx.complement(graph)
    for u,v in public_graph.nodes:
        public_graph[u][v]["label"] = "blue"
        public_graph[u][v]["weight"] = float('inf')

    ## phase 3 : find the minimum edge wight for each graph

    m0=float('inf')
    m1=float('inf')
    for u,v in public_graph.edges:
        if public_graph[u][v]["weight"] < m0:
            m0=public_graph[u][v]["weight"]

    for u,v in graph.edges:
        if graph[u][v]["weight"] < m1:
            m1=graph[u][v]["weight"]

    ## phase 4 : compute the minimum wieght of edge between the 2 partys
    tempMin=min(m0,m1)
    m=tempMin # need to change to real min


    ## phase 5 : compute S0,S1 just from the blue edges
    S0=[]
    S1=[]
    for edge in public_graph.nodes:
        if public_graph[edge[0]][edge[1]]["label"]=="red":
            continue
        else:
            S0.append(edge)

    for edge in graph.nodes:
        if graph[edge[0]][edge[1]]["label"]=="red":
            continue
        else:
            S1.append(edge)
    S01=set(S0+S1) # send this to private_union after maping

    ## phase 6 : activate the private_union for S groups edges