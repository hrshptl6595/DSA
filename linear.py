import time
def linear_search(v, L):
	'''Does Linear search with the value v in the List L

	Inputs:
		List L
		Value v

	Examples:
	>>>linear_search(1, [2,5,1,3,4,9,8,6,7])
	The number was found
	>>>linear_search(2, [1,5,6,4,8,7,9,5])
	The number was not found
	'''
	t1 = time.perf_counter()
	c = 0
	for i in L:
		if i==v:
			print('The number was found')
			c = 0
			break
		else:
			c=1
	if c==1:
		print('The number was not found')

	t2 = time.perf_counter()
	return t2-t1

def binary_search(v, SL, lo=0, hi=None):
	'''Does binary search with the value v in the Sorted List SL

	Inputs:
		List SL
		Value v

	Exapmles:
	>>>binary_search(1, [1,2,3,4,5,6,7,8,9,10])
	The number was found
	>>>binary_search(1, [2,3,4,5,6,7,8,9,10,11])
	The number was not found
	'''
	t1 = time.perf_counter()
	c=1
	if hi is None:
		hi = len(SL)

	while lo < hi:
		mid = (lo+hi)//2
		midval = SL[mid]
		if midval < v:
			lo = mid+1
		elif midval > v: 
			hi = mid
		else:
			print('The number was found at ',mid)
			c = 0
			break
	if(c==1):
		print('The number was not found')

	t2 = time.perf_counter()
	return t2-t1
print(linear_search(3, [1,6,5,9,7,8,6,2,12,35,45,87,68,5,6,4,6,9,5,6,8,4,6,8,4,4,8,4,5,4,15,3,89,45,78,66]))
print(binary_search(4, range(1,100)))