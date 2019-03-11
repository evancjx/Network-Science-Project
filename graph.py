import os
import time

import config as CONFIG


class Graph:

    network = dict()

    # Initializer / Instance Attributes
    def __init__(self, name):
        self.name = name

    def load_graph_v4(self):
        start_time = int(round(time.time() * 1000))
        count = 0
        with open(os.path.join(CONFIG.NETWORKS_DIR, self.name + '.txt'), 'r') as f:
            network = dict()
            for line in f:
                if line.startswith('#'):
                    continue

                count += 1
                split = line.split()

                # if int(split[0]) not in nodes_id:
                #     nodes_id.append(int(split[0]))
                # if int(split[1]) not in nodes_id:
                #     nodes_id.append(int(split[1]))

                if int(split[1]) not in network:
                    network[int(split[1])] = ''

                if int(split[0]) not in network:
                    edge_to_list = [split[1]]
                    network[int(split[0])] = edge_to_list
                elif int(split[0]) in network:
                    # print(list(network[int(split[0])]))
                    edge_to_list = list(network[int(split[0])])
                    edge_to_list.append(split[1])
                    network[int(split[0])] = edge_to_list
        # Sorting network dictionary in order of keys
        s_network = dict()
        for key in sorted(network.keys()):
            s_network[key] = network[key]
        end_time = int(round(time.time() * 1000))
        compute_time = int(end_time) - int(start_time)
        print('({}ms) Read graph from {} txt file'.format(compute_time, self.name))
        self.network = s_network
        return s_network

    def num_vertices(self):
        return len(self.network)
