def ssort(V):
	j = 0
	while j != len(V):
		for i in range(j, len(V)):
			if V[i] < V[j]:
				V[i],V[j] = V[j],V[i]
		j = j+1
	return V

if __name__ == "__main__":
	print(ssort([1,4,6,2,7,3,9,4,90,34,67,23,45]))