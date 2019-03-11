
import graph.graph as g

# file = 'email-Eu-core'
file = 'com-amazon.ungraph'
graph = g.Graph(file)

# print(str(graph.neighbor_of_node(0)))
# print(str(graph.get_degree_of_node(0)))

# Analyzing
# degree_distribution = graph.get_degree_distribution()
# print('Degree Distribution <degree>:<probability> = ' + str(degree_distribution))
# clustering_coefficient = graph.get_clustering_coefficient()
# print('Clustering coefficient' + str(clustering_coefficient))


# degree_analyzer.plot_store_degree_distribution_log_log(file, degree_distribution)
# degree_analyzer.plot_store_degree_distribution(file, degree_distribution)
# clustering_analyzer.plot_store_clustering_coefficient_log_log(file, clustering_coefficient, node_degree)
# clustering_analyzer.plot_store_clustering_coefficient(file, clustering_coefficient, node_degree, )


print(str(graph.get_degree_correlation()))
graph.plot_store_degree_correlation()
