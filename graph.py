import os
import time

import config as CONFIG
import graphCreators.graphCreator as GRAPH_CREATOR
import graph.analyzer.degree_analyzer as degree_analyzer


def graph():
    pass


# should pass in network object
def analyze_real_network_properties():
    pass


# should pass in network object
def compute_real_network_properties():
    pass
    # number of node
    # number of edge


def load_graph(name):
    # f = open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r')
    start_time = int(round(time.time() * 1000))

    # context manager
    with open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r') as f:
        # f_contents = f.readline()
        # print(f_contents)

        # empty list
        vertex = list()
        edgeto = list()
        for line in f:
            if line.startswith('#'):
                continue
            split = line.split()
            vertex.append(split[0])
            edgeto.append(split[1])

    end_time = int(round(time.time() * 1000))
    compute_time = int(end_time) - int(start_time)
    print('({}ms) Read graph from {} txt file'.format(compute_time, name))
    degree_analyzer.count_degree(vertex, vertex)

load_graph('com-amazon.ungraph')
