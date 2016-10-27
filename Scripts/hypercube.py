import networkx as nx
def hyper_g(n):
	G = nx.Graph()
	for i in range(2**n):
		for j in range(n):
			