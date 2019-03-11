import os

import config
import graph.analyzer.degree_analyzer as da
import graph.analyzer.clustering as ca


class Graph:

    network = dict()

    # Initializer / Instance Attributes
    def __init__(self, input_file):
        self.graph_name = input_file
        self.loaded = False
        self.read()

    def read(self):
        if self.loaded:
            return

        with open(os.path.join(config.NETWORKS_DIR, self.graph_name + '.txt'), 'r') as input_graph:
            for line in input_graph:
                if line.startswith('#'):
                    continue

                split = line.split()

                if int(split[1]) not in self.network:
                    self.network[int(split[1])] = []

                if int(split[0]) not in self.network:
                    edge_to_list = [int(split[1])]
                    self.network[int(split[0])] = edge_to_list
                elif int(split[0]) in self.network:
                    retrieve = self.network[int(split[0])]
                    edge_to_list = list()
                    for value in retrieve:
                        edge_to_list.append(value)
                    edge_to_list.append(int(split[1]))
                    self.network[int(split[0])] = edge_to_list

        s_network = dict()
        for key in sorted(self.network.keys()):
            edge_to_list = self.network[key]
            edge_to_list = sorted(edge_to_list)
            s_network[key] = edge_to_list

        self.network = s_network
        self.loaded = True

    def neighbor_of_node(self, node):
        return self.network[node]

    def get_node_count(self):
        return len(self.network)

    def get_nodes(self):
        node_list = list()
        for key in self.network.keys():
            node_list.append(key)
        return node_list

    def get_edge_count(self):
        count = 0
        for node, edge_list in self.network.items():
            count += len(edge_list)
        return count

    def get_each_node_degree(self):
        return da.count_degree(self.network)

    def get_each_degree_frequency(self):
        return da.count_node_with_degree_x(self.get_each_node_degree())

    def get_degree_distribution(self):
        return da.calculate_degree_distribution(self.get_node_count(), self.get_each_degree_frequency())

    def get_moment_n(self, n):
        return da.calculate_degree_n_moment(self.get_each_node_degree(), n)

    def get_max_k(self):
        return da.find_k_max(self.get_each_degree_frequency())

    def get_min_k(self):
        return da.find_k_min(self.get_each_degree_frequency())

    def get_clustering_coefficient(self):
        return ca.clustering_coefficient(self.get_each_node_degree(), ca.connected_neighbours_links(self.network))
