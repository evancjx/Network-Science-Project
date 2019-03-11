import matplotlib.pyplot as plt
import networkx as nx
import convert as convert
import load_graph as load
import graph.analyzer.degree_analyzer as degree_analyzer
import graph.analyzer.clustering as clustering_analyzer

import load_graph as load

# network = load.load_graph_v4('com-amazon.ungraph')
network = load.load_graph_v4('email-Eu-core')
print('size of the network: ' + str(len(network)))
node_degree = degree_analyzer.count_degree(network)
degree_frequency = degree_analyzer.count_node_with_degree_x(node_degree)
print('Each degree frequency = ' + str(degree_frequency))
degree_distribution = degree_analyzer.calculate_degree_distribution(len(network), degree_frequency)
print('Degree Distribution <degree>:<probability> = ' + str(degree_distribution))
first_moment = degree_analyzer.calculate_degree_n_moment(node_degree, n=1)
print('1st Moment (Average degree): ' + str(first_moment))
second_moment = degree_analyzer.calculate_degree_n_moment(node_degree, n=2)
print('2nd Moment (Variance): ' + str(second_moment))
k_max = degree_analyzer.find_k_max(degree_frequency)
print('Maximum k: ' + str(k_max))
k_min = degree_analyzer.find_k_min(degree_frequency)
print('Minimum k: ' + str(k_min))
node_cc_links = clustering_analyzer.connected_neighbours_links(network)
clustering_coefficient = clustering_analyzer.clustering_coefficient(node_degree, node_cc_links)
print('Clustering coefficient' + str(clustering_coefficient))

# # convert.convert_txt_to_csv('email-Eu-core')
#
# # g = nx.Graph()
# # g = load.load_graph_v5('email-Eu-core')
# # plt.subplot(121)
# # nx.draw(g, with_labels=True, font_weight='bold')
# # plt.show()
# # print(nx.clustering(g))
#
# g = nx.Graph();
# file_name = 'email-Eu-core';
# convert.convert_txt_to_csv(file_name);
#