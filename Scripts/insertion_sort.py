import time
def insertion_sort(alist):
	n = len(alist)
	for i in range(1, n):
		pos = i
		currval = alist[i]
		while pos>0 and alist[pos - 1]>currval:
			alist[pos] = alist[pos - 1]
			pos = pos - 1
		alist[pos] = currval
	return alist
t1 = time.perf_counter()
print(insertion_sort(list(range(5000))+[10**8]+list(range(5001,10000))))
t2 = time.perf_counter()
print("Time Taken: ", t2-t1)