import heapq
a = input()
s = a.split()
x = int(s[0])
y = int(s[1])
g = []
for i in range(x):
	g.append(input())
gpu = []
for i in g:
	temp = i.split()
	t2 = []
	for j in temp:
		t2.append(int(j))
	gpu.append(t2)

def find_minimum_range(sequences):
	# Maintain information which sequence each item belongs to
	sequences = [[(item, n) for item in seq] for n, seq in enumerate(sequences)]
	# Merge sequences into a single minheap, taking advantage of already sorted lists
	gp = []
	for i in range(len(sequences)):
		gp += sequences[i]
	# Current items to test
	found_range = None
	last_range = None
	current_items = [None] * len(sequences)
	for item, n in gp:
		current_items[n] = item
		if not all(current_items): # List not yet filled
			continue
		# Find range of current selection
		minimum = min(current_items)
		maximum = max(current_items)
		current_range = abs(maximum-minimum)
		# Update minimum range
		if not last_range or current_range < last_range:
			found_range = [minimum, maximum]
			last_range = current_range
	return found_range

range = find_minimum_range(gpu)
print(range[0],range[1])