
import graph.graph as g

file = 'email-Eu-core'
# file = 'com-amazon.ungraph'
graph = g.Graph(file)

# Analyzing

print('Degree Distribution <degree>:<probability> = ' + str(graph.get_degree_distribution()))

print('Clustering coefficient' + str(graph.get_clustering_coefficient()))


# degree_analyzer.plot_store_degree_distribution_log_log(file, degree_distribution, 'Degree Distribution Log Log')
# degree_analyzer.plot_store_degree_distribution(file, degree_distribution, 'Degree Distribution')
# clustering_analyzer.plot_store_clustering_coefficient_log_log(file, clustering_coefficient, node_degree, 'Clustering Coefficient Log Log')
# clustering_analyzer.plot_store_clustering_coefficient(file, clustering_coefficient, node_degree, 'Clustering Coefficient')


