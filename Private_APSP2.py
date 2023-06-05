import networkx as nx
import socket


def ASPS(graph):

    ## phase 0 : connection

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Specify the server's IP address and port number
    server_host = 'localhost'  # Replace with the server's IP address
    server_port = 1234  # Replace with the server's port number

    # Connect to the server
    client_socket.connect((server_host, server_port))

    ## phase 1 : set graph edges to blue
    for u,v in graph.edges:
        graph[u][v]["label"] = "blue"

    ## phase 2 : create the public graph
    public_graph =  nx.complement(graph)
    for u,v in public_graph.nodes:
        public_graph[u][v]["label"] = "blue"
        public_graph[u][v]["weight"] = float('inf')

    # sorted edge for mapping and create mapping
    sorted_edges = sorted(public_graph.edges(data=True), key=lambda x: (x[0], x[1]))
    # Create the mapping dictionary
    mapping = {}
    unmapping = {}
    for i, edge in enumerate(sorted_edges):
        mapping[edge[0], edge[1]] = i
        unmapping[i]= [edge[0] , edge[1]]

    ## phase 3 : find the minimum edge weight for each graph

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
    client_socket.send(str(tempMin).encode())
    # Receive the response from the server
    finalMin = client_socket.recv(1024).decode()


    ## phase 5 : compute S0,S1 just from the blue edges
    S0=[]
    S1=[]
    for edge in public_graph.nodes:
        if public_graph[edge[0]][edge[1]]["label"] == "blue" \
                and public_graph[edge[0]][edge[1]]["weight"] == finalMin:
            S0.append(edge)

    for edge in graph.nodes:
        if public_graph[edge[0]][edge[1]]["label"] == "blue" \
                and public_graph[edge[0]][edge[1]]["weight"] == finalMin:
            S1.append(edge)

    S01=set(S0+S1) # send this to private_union after mapping


    ## phase 6 : activate the private_union for S groups edges

    SO1_mapping = [] # we need to send this to the union
    for s in S01:
        SO1_mapping.append(mapping[s[0],s[1]])

    from unionB import union as union_b
    
    print(union_b(SO1_mapping, public_graph.nodes.size()))
    
k = nx.Graph()
k.add_edge(2,3)
k.add_edge(1,9)
for i in range(0,9):
    k.add_node(i)
ASPS(k)