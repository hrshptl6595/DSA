def mergeSort(a):
	n = len(a)
	if len(a) == 1:
		return a
	else:
		return merge(mergeSort(a[:n//2]), mergeSort(a[n//2:]))

def merge(al, bl):
	na = len(al)
	nb = len(bl)
	cl = []
	for i in range(na):
		for j in range(nb):
			if al[i]<bl[j]:
				cl = cl + [al[i]]
			else:
				cl = cl + [bl[j]]
	return cl
mergeSort([8,7,6,5,4,3,2,1])