import networkx as nx

def main():
    g = nx.Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)

    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print g.nodes(), g.edges()

    print nx.shortest_path(g, source = 1, target = 3)

if __name__ == "__main__":
    main()
