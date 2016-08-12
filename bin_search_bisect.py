import time
from bisect import bisect_left

def bin_search(a, x, lo=0, hi=None):
	t1 = time.perf_counter()
	hi = hi if hi is not None else len(a)
	pos = bisect_left(a, x, lo, hi)
	t2 = time.perf_counter()
	print(pos if pos != hi and a[pos] == x else -1)
	return t2-t1

print(bin_search(range(1,100), 5))