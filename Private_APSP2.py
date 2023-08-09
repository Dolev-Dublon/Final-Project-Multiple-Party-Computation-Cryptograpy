import math

import networkx as nx
import socket

import numpy as np

from connections import init_connection_apsp2
from hand_shake import hand_shake_APSP2
from unionB import union as union_b
import itertools



num_of_bits = 64
""" 
64 BITS can calculate graph with 1M nodes without problem in the union graph (that need big scale of numbers)
"""
def ASPS(graph):
    client_socket = init_connection_apsp2()

    P_R_edges = []
    P_B_edges = []
    B1_edges = []

    ## phase 1 : set graph edges to blue
    for edge in iter(graph.edges):
        B1_edges.append(edge)
        ##graph[u][v]["label"] = "blue"

    ## phase 2 : create the public graph
    public_graph = nx.Graph()
    for node in graph.nodes:
        public_graph.add_node(node)

    node_combinations = itertools.combinations(public_graph.nodes, 2)
    for u, v in node_combinations:
        public_graph.add_edge(u, v, weight=float("inf"), label="blue")
        P_B_edges.append((u, v))

    # sorted edge for mapping and create mapping
    sorted_edges = sorted(public_graph.edges(), key=lambda x: (x[0], x[1]))
    # Create the mapping dictionary
    mapping = {}
    unmapping = {}
    for i, edge in enumerate(sorted_edges):
        mapping[edge[0], edge[1]] = i
        unmapping[i] = [edge[0], edge[1]]

    ## phase 3 : find the minimum edge weight for each graph
    while True:
        m0 = float("inf")
        m1 = float("inf")
        for edge in P_B_edges:
            if public_graph[edge[0]][edge[1]]["weight"] < m0:
                m0 = public_graph[edge[0]][edge[1]]["weight"]

        for edge in B1_edges:
            if graph[edge[0]][edge[1]]["weight"] < m1:
                m1 = graph[edge[0]][edge[1]]["weight"]

        ## phase 4 : compute the minimum wieght of edge between the 2 partys

        tempMin = min(m0, m1)
        # if not hand_shake_APSP2(client_socket):
        #     print("fail handshake")
        #     break
        if hand_shake_APSP2(client_socket):
            client_socket.send(str(tempMin).encode())
            # Receive the response from the server
            finalMin = client_socket.recv(1024).decode()

            if finalMin == "inf":
                return public_graph

            finalMin = int(finalMin)

            ## phase 5 : compute S0,S1 just from the blue edges
            S0 = []
            S1 = []
            for edge in P_B_edges:
                if public_graph[edge[0]][edge[1]]["weight"] == finalMin:
                    S0.append(edge)

            for edge in B1_edges:
                if graph[edge[0]][edge[1]]["weight"] == finalMin:
                    S1.append(edge)

            S01 = set(S0 + S1)  # send this to private_union after mapping

            ## phase 6 : activate the private_union for S groups edges

            SO1_mapping = []  # we need to send this to the union
            for s in S01:
                SO1_mapping.append(mapping[s[0], s[1]])
   ### remove all the edges equale to minWeight

            # print("S01:",S01)
            # print("S01_mapping:", SO1_mapping)
            n = len(public_graph.nodes)
            print("before union:" , SO1_mapping)
            Union_edge = union_b(SO1_mapping, num_of_bits)
            print("after union:", Union_edge)
            # print("Union_egdes", Union_edge)

            S = []
            for index_edge in Union_edge:
                S.append(unmapping[index_edge])

            # print("Index edge", S)

            for edge in S:
                public_graph[edge[0]][edge[1]]["weight"] = finalMin

                ## phase 7 :
            for edge in S:
                i = edge[0]
                j = edge[1]
                for red_edge in P_R_edges:
                    k = red_edge[1]
                    if red_edge[0] != j:
                        continue
                    if public_graph[i][k]["label"] != "blue":
                        continue
                    w1 = public_graph[i][j]["weight"] + public_graph[j][k]["weight"]
                    w2 = public_graph[k][j]["weight"] + public_graph[j][i]["weight"]
                    w = min(w1, w2)
                    if w < public_graph[i][k]["weight"]:
                        public_graph[i][k]["weight"] = w
            for red_edge in P_R_edges:
                i = red_edge[0]
                j = red_edge[1]
                for edge in S:
                    k = edge[1]
                    if edge[0] != j:
                        continue
                    if public_graph[i][k]["label"] != "blue":
                        continue
                    w1 = public_graph[i][j]["weight"] + public_graph[j][k]["weight"]
                    w2 = public_graph[k][j]["weight"] + public_graph[j][i]["weight"]
                    w = min(w1, w2)
                    if w < public_graph[i][k]["weight"]:
                        public_graph[i][k]["weight"] = w

            for edge in S:
                P_R_edges.append(( edge[0], edge[1] ))
                if tuple(edge) in P_B_edges:
                    P_B_edges.remove(tuple(edge))
                if tuple(edge) in B1_edges:
                    B1_edges.remove(tuple(edge))

                public_graph[edge[0]][edge[1]]["label"] = "red"

            if len(P_B_edges) == 0:
                return public_graph


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    Daniel = nx.Graph()
    Daniel.add_edge("c1", "c2", weight=10)
    Daniel.add_edge("c1", "c3", weight=4)
    Daniel.add_edge("c3", "c4", weight=10)
    Graph_res = ASPS(Daniel)

    print("Nodes:", Graph_res.nodes())
    print("Edges:", Graph_res.edges())
    print("Edge Weights:", [(u, v, Graph_res[u][v]['weight']) for u, v in Graph_res.edges()])

    # Check if all nodes have finite positions
    # pos = nx.spring_layout(Graph_res)
    # for node, coordinates in pos.items():
    #     if not all(map(np.isfinite, coordinates)):
    #         print(f"Node {node} has non-finite coordinates: {coordinates}")
    #
    # # Draw the graph
    # nx.draw(Graph_res, pos, with_labels=True, node_size=700, node_color="skyblue")
    # nx.draw_networkx_edge_labels(Graph_res, pos,
    #                              edge_labels={(u, v): Graph_res[u][v]['weight'] for u, v in Graph_res.edges()})

    # plt.show()
    # print("result Union Graph:",Graph_res.nodes ,"\n" , "Edges: " ,Graph_res.edges, "\n", "Edges values: ", Graph_res.edges.values())
