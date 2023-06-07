import networkx as nx
import socket
from unionB import union as union_b
import itertools


def ASPS(graph):

    ## phase 0 : connection

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify the server's IP address and port number
    server_host = 'localhost'  # Replace with the server's IP address
    server_port = 1255  # Replace with the server's port number

    # Connect to the server
    client_socket.connect((server_host, server_port))

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
        public_graph.add_edge(u, v, weight=float('inf'), label='blue')
        P_B_edges.append((u, v))


    # sorted edge for mapping and create mapping
    sorted_edges = sorted(public_graph.edges(data=True), key=lambda x: (x[0], x[1]))
    # Create the mapping dictionary
    mapping = {}
    unmapping = {}
    for i, edge in enumerate(sorted_edges):
        mapping[edge[0], edge[1]] = i
        unmapping[i] = [edge[0], edge[1]]

    ## phase 3 : find the minimum edge weight for each graph
    while (True):
        m0 = float('inf')
        m1 = float('inf')
        for edge in P_B_edges:
            if public_graph[edge[0]][edge[1]]["weight"] < m0:
                m0 = public_graph[edge[0]][edge[1]]["weight"]

        for edge in B1_edges:
            if graph[edge[0]][edge[1]]["weight"] < m1:
                m1 = graph[edge[0]][edge[1]]["weight"]


        ## phase 4 : compute the minimum wieght of edge between the 2 partys

        tempMin = min(m0 , m1)
        client_socket.send(str(tempMin).encode())
        # Receive the response from the server
        finalMin = client_socket.recv(1024).decode()

        ## phase 5 : compute S0,S1 just from the blue edges
        S0 = []
        S1 = []
        for edge in P_B_edges:
            if public_graph[edge[0]][edge[1]]["weight"] == finalMin:
                S0.append(edge)

        for edge in B1_edges:
            if public_graph[edge[0]][edge[1]]["weight"] == finalMin:
                S1.append(edge)
                B1_edges.remove(edge)  ### remove all the edges equale to minWeight

        S01 = set(S0 + S1)  # send this to private_union after mapping

        ## phase 6 : activate the private_union for S groups edges

        SO1_mapping = []  # we need to send this to the union
        for s in S01:
            SO1_mapping.append(mapping[s[0], s[1]])

        Union_edge = union_b(SO1_mapping, len(public_graph.nodes))

        S = []
        for index_edge in Union_edge:
            S.append(unmapping[index_edge])

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
                w = public_graph[i][j]["weight"] + public_graph[j][k]["weight"]
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
                w = public_graph[i][j]["weight"] + public_graph[j][k]["weight"]
                if w < public_graph[i][k]["weight"]:
                    public_graph[i][k]["weight"] = w

        for edge in S:
            P_R_edges.append(public_graph[edge[0]][edge[1]])
            P_B_edges.remove(public_graph[edge[0]][edge[1]])
            public_graph[edge[0]][edge[1]] = "red"

        if len(P_B_edges) == 0:
            print(public_graph)
            break



if __name__ == '__main__':
    Daniel = nx.Graph()
    Daniel.add_edge("c1", "c2", weight=10)
    Daniel.add_edge("c1", "c3", weight=4)
    Daniel.add_edge("c3", "c4", weight=10)
    ASPS(Daniel)