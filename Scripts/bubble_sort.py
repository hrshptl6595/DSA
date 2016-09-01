import time
def bubbleSort(alist):
	for num in range(len(alist)-1,0,-1):
		for i in range(num):
			if alist[i]>alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

def bubble_sort_adaptive(alist):
	blist = []
	for num in range(len(alist)-1,0,-1):
		for i in range(num):
			if alist[i]<alist[i+1]:
				blist.append(alist[i])
			else:
				blist.append(alist[i+1])
	return blist

if __name__ == "__main__":
	#print(bubbleSort(list(range(5000))+[10**8]+list(range(5001,10000))))
	t1 = time.perf_counter()
	print(bubble_sort_adaptive(list(range(5000))+[10**8]+list(range(5001,10000))))
	t2 = time.perf_counter()
	print("Time taken: ", t2-t1)