import networkx as nx
import matplotlib as plt
def print_hi(name):
    Daniel = nx.Graph()
    Daniel.add_edge("Tel aviv","Jerusalem", weight = 10,label="red")
    Daniel.add_edge("a","s",weight=4,label="blue")
    Daniel.add_edge("Tel aviv","Petah tikva", weight = 5,label="red")
    # Daniel.add_edge("Petah tikva","Jerusalem", weight = 5)
    # Daniel.add_edge("Eilat","Jerusalem", weight = 20)
    # Daniel.add_node("Haifa")
    # Daniel.add_node("Beer sheva")
    #
    # Daniel.add_edge("Haifa","Beer sheva", weight = 10)
    # Daniel.add_edge("Haifa","Jerusalem", weight = 10)
    # Daniel.add_edge("Beer sheva","Jerusalem", weight = 10)

    # print the shortest path between Eilat and Tel aviv with the weight number
    # print(nx.shortest_path(Daniel, "Eilat", "Tel aviv", weight = "weight"))
    # print(nx.shortest_path_length(Daniel, "Eilat", "Tel aviv", weight = "weight"))

    # how to iterete the graph
    for node in Daniel.nodes:
        print(node)
        for neighbor in Daniel[node]:
            print(neighbor)
            print(Daniel[node][neighbor]['weight'])
    # how to get the weight of the edge
    print(Daniel["Tel aviv"]["Jerusalem"]['weight'])


    print("edges loop")
    for v,u in Daniel.edges:
        print(v,u)
        if Daniel[v][u]["label"]=="red":
            print("this red")
    temp=None
    print("edges loop2")
    for edge in Daniel.edges:
        print(edge)
        temp=edge
    print(Daniel[edge[0]][edge[1]]["weight"])
    # show the graph with plt and networkx
    # nx.draw(Daniel, with_labels=True)
    # plt.pyplot.show()






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/