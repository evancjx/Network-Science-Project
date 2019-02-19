import os
import time
import collections

import config as CONFIG
import graphCreators.graphCreator as GRAPH_CREATOR
import graph.analyzer.degree_analyzer as degree_analyzer


# Where node_id not in txt means not connected at all, standalone node
# WRONG!
def load_graph_v1(name):
    # f = open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r')
    start_time = int(round(time.time() * 1000))

    # context manager
    with open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r') as f:
        # f_contents = f.readline()
        # print(f_contents)

        # empty list
        network = dict()
        edge_to_list = list()
        node_id = 1
        # count_edge = 0
        for line in f:
            if line.startswith('#'):
                continue
            split = line.split()
            while int(split[0]) != node_id:
                network[node_id] = edge_to_list
                edge_to_list = list()
                node_id += 1

            if int(split[0]) == node_id:
                edge_to_list.append(split[1])
            # count_edge += 1
        # last line
        network[node_id] = edge_to_list
        # network[0] = count_edge

    end_time = int(round(time.time() * 1000))
    compute_time = int(end_time) - int(start_time)
    print('({}ms) Read graph from {} txt file'.format(compute_time, name))
    return network


# Did not account to end nodes
# in txt file, it is about edges, start node to end node
def load_graph_v2(name):
    # f = open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r')
    start_time = int(round(time.time() * 1000))

    # context manager
    with open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r') as f:
        # f_contents = f.readline()
        # print(f_contents)

        # empty list
        network = dict()
        edge_to_list = list()
        current_node = 1
        last_node = 1
        # count_edge = 0
        for line in f:
            if line.startswith('#'):
                continue

            split = line.split()
            # if int(split[0]) < 540000:
            #     continue
            # if int(split[0]) > 541000:
            #     break

            if int(split[0]) == last_node:
                edge_to_list.append(split[1])
            elif current_node != int(split[0]):
                network[last_node] = edge_to_list
                edge_to_list = list()
                current_node = int(split[0])
                edge_to_list.append(split[1])
                last_node = current_node

        network[current_node] = edge_to_list  # last line

    end_time = int(round(time.time() * 1000))
    compute_time = int(end_time) - int(start_time)
    print('({}ms) Read graph from {} txt file'.format(compute_time, name))
    return network


def load_graph_v3(name):
    # f = open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r')
    start_time = int(round(time.time() * 1000))
    count = 0
    # context manager
    with open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r') as f:
        network = dict()
        for line in f:
            if line.startswith('#'):
                continue

            count += 1
            split = line.split()

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
    print('({}ms) Read graph from {} txt file'.format(compute_time, name))
    return s_network


def load_graph_v4(name):
    start_time = int(round(time.time() * 1000))
    count = 0
    with open(os.path.join(CONFIG.NETWORKS_DIR, name + '.txt'), 'r') as f:
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
    print('({}ms) Read graph from {} txt file'.format(compute_time, name))
    return s_network


network = load_graph_v4('com-amazon.ungraph')
print('size of the network: ' + str(len(network)))
degree_distribution = degree_analyzer.degree_distribution(network)
print('Degree Distribution <degree>:<probability> = ' + str(degree_distribution))
