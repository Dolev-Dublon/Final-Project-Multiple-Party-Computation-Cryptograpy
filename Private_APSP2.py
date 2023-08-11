import networkx as nx
from connections import Init_client_connection
from unionB import unionB
import itertools

num_of_bits = 64
""" 
64 BITS can calculate graph with 1M nodes without problem in the union graph (that need big scale of numbers)
"""


def sort_graph_edges(graph):
    """
    Sort the edges and nodes of a graph based on lexicographical order and return a new graph.
    """
    # Extract edges from the graph along with their weights
    edges = [(u, v, graph[u][v]["weight"]) for u, v in graph.edges()]
    # Sort edges based on the smallest node first, then the larger node
    sorted_edges = sorted(
        edges, key=lambda edge: (min(edge[0], edge[1]), max(edge[0], edge[1]))
    )
    # Create a new graph and add the sorted nodes first
    sorted_graph = nx.Graph()
    for node in sorted(graph.nodes()):
        sorted_graph.add_node(node)
    # Then add the sorted edges
    for edge in sorted_edges:
        # Ensure the smaller node is the source node
        u, v = min(edge[0], edge[1]), max(edge[0], edge[1])
        sorted_graph.add_edge(u, v, weight=edge[2])

    return sorted_graph


def ASPS2(graph_):
    client_socket = Init_client_connection()
    graph = sort_graph_edges(graph_)

    P_R_edges = []
    P_B_edges = []
    B1_edges = []
    ## phase 1 : set graph edges to blue
    for edge in iter(graph.edges):
        B1_edges.append(edge)

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
        print("before union:", SO1_mapping)
        Union_edge = unionB(SO1_mapping, num_of_bits)
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
            i = 0
            j = 0
            for t in range(2):
                if t == 0:
                    i = edge[0]
                    j = edge[1]
                else:
                    j = edge[0]
                    i = edge[1]
                for red_edge in P_R_edges:
                    k = 0
                    if red_edge[0] == j:
                        k = red_edge[1]
                    elif red_edge[1] == j:
                        k = red_edge[0]
                    else:
                        continue
                    if public_graph[i][k]["label"] != "blue":
                        continue
                    w = public_graph[i][j]["weight"] + public_graph[j][k]["weight"]
                    if w < public_graph[i][k]["weight"]:
                        public_graph[i][k]["weight"] = w

        for red_edge in P_R_edges:
            i = 0
            j = 0
            for t in range(2):
                if t == 0:
                    i = red_edge[0]
                    j = red_edge[1]
                else:
                    j = red_edge[0]
                    i = red_edge[1]
            for edge in S:
                k = 0
                if edge[0] == j:
                    k = edge[1]
                elif edge[1] == j:
                    k = edge[0]
                else:
                    continue
                if public_graph[i][k]["label"] != "blue":
                    continue
                w = public_graph[i][j]["weight"] + public_graph[j][k]["weight"]
                if w < public_graph[i][k]["weight"]:
                    public_graph[i][k]["weight"] = w
        for edge in S:
            P_R_edges.append((edge[0], edge[1]))
            if tuple(edge) in P_B_edges:
                P_B_edges.remove(tuple(edge))
            if tuple(edge) in B1_edges:
                B1_edges.remove(tuple(edge))

            public_graph[edge[0]][edge[1]]["label"] = "red"

        if len(P_B_edges) == 0:
            client_socket.close()
            return public_graph


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    """ G1 """
    # graph = nx.Graph()
    # graph.add_edge("c1", "c2", weight=10)
    # graph.add_edge("c1", "c3", weight=4)
    # graph.add_edge("c3", "c4", weight=10)
    # # Daniel.add_edge("c5", "c4", weight=1)
    # Graph_res = ASPS2(graph)
    #
    # print("Nodes:", Graph_res.nodes())
    # print("Edges:", Graph_res.edges())
    # print("Edge Weights:", [(u, v, Graph_res[u][v]['weight']) for u, v in Graph_res.edges()])

    # import matplotlib.pyplot as plt
    #
    # pos = nx.spring_layout(graph)
    # labels = nx.get_edge_attributes(graph, 'weight')
    # nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='pink', font_size=15, width=3)
    # nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=15)
    # plt.title("Mystica Realm Magical Portals")
    # plt.show()

    """ G2 """
    # graph = nx.Graph()
    # graph.add_edge("a", "b", weight=2)
    # graph.add_edge("a", "d", weight=8)
    # graph.add_edge("b", "d", weight=9)
    # graph.add_edge("c", "d", weight=3)
    # Graph_res = ASPS2(graph)
    #
    # print("Nodes:", Graph_res.nodes())
    # print("Edges:", Graph_res.edges())
    # print("Edge Weights:", [(u, v, Graph_res[u][v]['weight']) for u, v in Graph_res.edges()])

    # """ G3 """
    # graph = nx.Graph()
    # graph.add_edge("a", "b", weight=8)
    # graph.add_edge("a", "c", weight=7)
    # graph.add_edge("b", "c", weight=1)
    # graph.add_edge("c", "d", weight=3)
    # graph.add_edge("d", "e", weight=4)
    # graph.add_edge("e", "f", weight=7)
    # Graph_res = ASPS2(graph)
    #
    # print("Nodes:", Graph_res.nodes())
    # print("Edges:", Graph_res.edges())
    # print("Edge Weights:", [(u, v, Graph_res[u][v]['weight']) for u, v in Graph_res.edges()])

    """ G4 """
    #
    # graph = nx.Graph()
    # graph.add_edge("a", "b", weight=8)
    # graph.add_edge("b", "c", weight=6)
    # graph.add_edge("c", "a", weight=7)
    # graph.add_edge("b", "d", weight=9)
    #
    # Graph_res = ASPS2(graph)
    #
    # print("Nodes:", Graph_res.nodes())
    # print("Edges:", Graph_res.edges())
    # print("Edge Weights:", [(u, v, Graph_res[u][v]['weight']) for u, v in Graph_res.edges()])

    """ G5 """

    graph = nx.Graph()

    graph.add_edge("f", "e", weight=12)
    graph.add_edge("d", "f", weight=5)
    graph.add_edge("d", "c", weight=8)
    graph.add_edge("c", "b", weight=3)
    graph.add_edge("b", "a", weight=6)
    graph.add_edge("a", "e", weight=4)
    graph.add_edge("a", "f", weight=10)
    graph.add_edge("b", "d", weight=7)

    Graph_res = ASPS2(graph)

    print("Nodes:", Graph_res.nodes())
    print("Edges:", Graph_res.edges())
    print(
        "Edge Weights:",
        [(u, v, Graph_res[u][v]["weight"]) for u, v in Graph_res.edges()],
    )

    import matplotlib.pyplot as plt

    # Plot
    # pos = nx.spring_layout(graph)
    # labels = nx.get_edge_attributes(graph, 'weight')
    # nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15, width=3)
    # nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=15)
    # plt.title("Eldoria Realm Magical Portals")
    # plt.show()
