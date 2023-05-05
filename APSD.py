import networkx as nx
import matplotlib as plt
import random

def private_compute_on_the_public_graph (G_0):
    # implement compute the shortest path between two nodes on the public graph
    pass

def partyNum1_func (G_1):
    # implement compute the shortest path between two nodes on the G_1 graph
    pass
def partyNum2_func (G_2):
    # implement compute the shortest path between two nodes on the G_2 graph
    pass



def main():
    # create a complete graph with 6 nodes and infty weight and a flag on each edge
    G_0 = nx.complete_graph(6)
    G_1 = nx.complete_graph(6)
    G_2 = nx.complete_graph(6)
    # give random weight to each edge on G_1
    for (u, v, w) in G_1.edges(data=True):
        w['weight'] = random.randint(1, 15)
        w['color'] = 'blue'
    # give random weight to each edge on G_2 but need to be lower than G_1
    for (u, v, w) in G_2.edges(data=True):
        w['weight'] = random.randint(1, 15)
        while w['weight'] > G_1[u][v]['weight']:
            w['weight'] = random.randint(1, 15)
        w['color'] = 'blue'

    for (u, v, w) in G_0.edges(data=True):
        w['weight'] = float('inf')
        w['color'] = 'blue'

    print(G_1.edges.data())
    print(G_2.edges.data())

    min_public = private_compute_on_the_public_graph(G_0)
    min_G_1 = partyNum1_func(G_1)
    min_G_2 = partyNum2_func(G_2)



    k = 1 # the number of the iteration
    edges_num = G_0.number_of_edges()
    print(edges_num)



if __name__ == '__main__':
    main()
