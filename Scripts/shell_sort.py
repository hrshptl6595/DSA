import time
def Shell_Sort(alist):
	"""Shell sort using Shell's original gap sequence: n/1, n/4, ..... 1"""
	gap = len(alist)//2
	#loop over gaps
	while gap > 0:
		#do the insertion sort
		for i in range(gap, len(alist)):
			val = alist[i]
			j = i
			while j >= gap and alist[j - gap] > val:
				alist[j] = alist[j - gap]
				j -= gap
			alist[j] = val
		gap //= 2
	return alist
t1 = time.perf_counter()
print("Sorted Array: ", Shell_Sort(list(range(5000))+[10**8]+list(range(5001,10000))))
t2 = time.perf_counter()
print("Time taken : ", t2 - t1)