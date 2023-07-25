import socket
import networkx as nx
from unionA import union as union_a
from hand_shake import hand_shake_APSP1
import itertools

gayindex = 0


def init_connection_asps():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Choose a port and bind the socket to it
    server_host = "0.0.0.0"  # listen on all available network interfaces
    server_port = 1230  # choose a port number
    server_socket.bind((server_host, server_port))
    # Listen for incoming connections
    server_socket.listen()
    print("Waiting for a connection...")
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)
    return client_socket


def ASPS(graph):
    global gayindex
    gayindex = gayindex + 1
    print("gay index: ", gayindex)
    client_socket = init_connection_asps()

    P_R_edges = []
    P_B_edges = []
    B1_edges = []

    ## phase 1 : set graph edges to blue
    for edge in iter(graph.edges):
        B1_edges.append(edge)
        print("edge:", edge)
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
    sorted_edges = sorted(public_graph.edges(data=True), key=lambda x: (x[0], x[1]))
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
        # print("m0:", m0, " m1:", m1)
        ## phase 4 : compute the minimum wieght of edge between the 2 partys

        tempMin = min(m0, m1)
        if not hand_shake_APSP1(client_socket):
            print("fail handshake")
            break

        received_number = client_socket.recv(1024).decode()
        print("gay2", received_number)
        print("print1")
        # print('iteration: ', i, ' ,Received number:', received_number)
        otherMin = int(received_number)
        # Process the number and send a response
        finalMin = min(tempMin, otherMin)
        response = str(finalMin)  # Example: Increment the number by 1
        client_socket.send(response.encode())
        print("print2")
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
        print("print3")
        ## phase 6 : activate the private_union for S groups edges

        SO1_mapping = []  # we need to send this to the union
        for s in S01:
            SO1_mapping.append(mapping[s[0], s[1]])

        Union_edge = union_a(SO1_mapping, len(public_graph.nodes))

        S = []
        for index_edge in Union_edge:
            S.append(unmapping[index_edge])

        for edge in S:
            public_graph[edge[0]][edge[1]]["weight"] = finalMin
        print("print4")
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
                print("print5")
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
        print("print6")
        for edge in S:
            P_R_edges.append(public_graph[edge[0]][edge[1]])
            P_B_edges.remove(public_graph[edge[0]][edge[1]])
            public_graph[edge[0]][edge[1]] = "red"

        if len(P_B_edges) == 0:
            print(public_graph)
            break
        print("print7")

if __name__ == "__main__":
    Daniel = nx.Graph()
    Daniel.add_edge("c1", "c2", weight=5)
    Daniel.add_edge("c2", "c3", weight=4)
    Daniel.add_edge("c3", "c4", weight=5)
    ASPS(Daniel)
