def ssort(V):
	j = 0
	while j != len(V):
		for i in range(j, len(V)):
			if V[i] < V[j]:
				V[j],V[i] = V[i],V[j]
			j = j+1
	return V