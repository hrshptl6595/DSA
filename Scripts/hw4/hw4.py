#BT3051 Assignment 4
#Roll number : ED13B045
#Collaborators : none
#Time: 1:45
import networkx as nx
import matplotlib.pyplot as plt
import random

def barabasi_albert_graph(G, nNodes , mLinks ):
	# G is an initial graph , which should be an nx.Graph type of object
	# nNodes is the number of nodes to add to G
	# mLinks is the number of links that get added from a new node to existing nodes in each iteration
	G_new = G.copy()
	### CODE FOR graph creation
	targets = list(range(mLinks))
	rep_nodes = []
	source = mLinks
	while source<nNodes:
		G_new.add_edges_from(zip([source]*mLinks, targets))
		rep_nodes.extend(targets)
		rep_nodes.extend([source]*mLinks)
		targets = random_subset(rep_nodes, mLinks)
		source+=1
	return G_new

def random_subset(seq,m):
	targets=[]
	while len(targets)<m:
		x=random.choice(seq)
		targets.append(x)
	return targets

if __name__ == '__main__':
	G = nx.Graph()
	G.add_edge(1,2)
	G_new = barabasi_albert_graph(G,98,1)
	#plot G_new
	nx.draw(G_new)
	plt.savefig("plot.png")
	plt.show()