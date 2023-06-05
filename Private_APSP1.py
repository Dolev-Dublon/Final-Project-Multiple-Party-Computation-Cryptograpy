import socket
import networkx as nx


def ASPS(graph):

    ## phase 0 : connection

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Choose a port and bind the socket to it
    server_host = '0.0.0.0'  # listen on all available network interfaces
    server_port = 1234  # choose a port number
    server_socket.bind((server_host, server_port))

    # Listen for incoming connections
    server_socket.listen(1)
    print('Waiting for a connection...')

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print('Connected to:', client_address)

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
    for i, edge in enumerate(sorted_edges):
        mapping[edge[0], edge[1]] = i

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

    tempMin = min(m0,m1)
    received_number = client_socket.recv(1024).decode()
    #print('iteration: ', i, ' ,Received number:', received_number)
    otherMin = int(received_number)
    # Process the number and send a response
    finalMin=min(tempMin,otherMin)
    response = str(finalMin)  # Example: Increment the number by 1
    client_socket.send(response.encode())



    ## phase 5 : compute S0,S1 just from the blue edges
    S0=[]
    S1=[]
    for edge in public_graph.nodes:
        if public_graph[edge[0]][edge[1]]["label"]=="blue"\
                and public_graph[edge[0]][edge[1]]["weight"]==finalMin:
            S0.append(edge)

    for edge in graph.nodes:
        if public_graph[edge[0]][edge[1]]["label"] == "blue" \
                and public_graph[edge[0]][edge[1]]["weight"] == finalMin:
            S1.append(edge)

    S01=set(S0+S1) # send this to private_union after mapping


    ## phase 6 : activate the private_union for S groups edges

    SO1_mapping = []  # we need to send this to the union
    for s in S01:
        SO1_mapping.append(mapping[s[0], s[1]])
        
    import union/