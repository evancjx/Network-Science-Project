from itertools import groupby
import time


def count_degree_old(vertex):
    # not a good way to get degree
    # each_node_degree = [len(list(group)) for key, group in groupby(vertex)]
    # print(len(each_node_degree))

    start_time = int(round(time.time() * 1000))

    each_node_degree = [];
    index = 1;
    for key, group in groupby(vertex):
        # print('key: ' + str(key))
        # print('index: ' + str(index))

        if int(key) != int(index):
            # print('not equal')
            each_node_degree.insert(index-1, 0)
            index += 2
        else:
            index += 1

        each_node_degree.append(len(list(group)))
        # if key == '10':
        #     break

    end_time = int(round(time.time() * 1000))
    compute_time = int(end_time) - int(start_time)
    print('({}ms) Count degree'.format(compute_time))

    return each_node_degree


def count_degree(network):
    start_time = int(round(time.time() * 1000))
    node_degree = {}
    for key, value in network.items():
        node_degree[key] = len(value)
        # if key == 10:
        #     break
    end_time = int(round(time.time() * 1000))
    compute_time = int(end_time) - int(start_time)
    print('({}ms) Count degree'.format(compute_time))
    return node_degree


def count_node_with_degree_x(node_degree):
    degree_frequency = {}
    for key, value in node_degree.items():
        if value not in degree_frequency:
            degree_frequency[value] = 0
        degree_frequency[value] += 1
    s_degree_frequency = dict()
    for key in sorted(degree_frequency.keys()):
        s_degree_frequency[key] = degree_frequency[key]
    return s_degree_frequency


def calculate_degree_distribution(no_of_nodes, degree_frequency):
    prob_degree_distribution = {}
    for key, value in degree_frequency.items():
        prob_degree_distribution[key] = float(value / no_of_nodes)
    return prob_degree_distribution


def degree_distribution(network):
    node_degree = count_degree(network)
    degree_frequency = count_node_with_degree_x(node_degree)
    return calculate_degree_distribution(len(network), degree_frequency)

