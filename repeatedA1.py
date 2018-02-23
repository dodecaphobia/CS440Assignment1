# calculates repeated forward A*
# can be used as forward and backward by switching start and end parameters
def A(l, start, end):

# given two tuples, calculates heuristic
# heuristic: Manhattan distance
def h(start, end):
	return abs(start[0] - end[0]) + abs(start[1] - end[1])

# assume minHeap, easily fixable otherwise
class Heap(object):
	l = []

	# for non-heaps, takes it and heapifies
	def __init__(nonHeap):
		l = nonHeap
		heapify()

	# adds an element to the bottom of the heap
	def insert(x):
		l.append(x)
		loc = len(x) - 1
		# while not at the top of the heap and greater than the parent, swap
		while loc != 0 and l[loc] > l[(int)(loc // 2)]:
			l[loc], l[(int)(loc // 2)] = l[(int)(loc // 2)], l[loc]
			loc = (int)(loc // 2)

	# removes the top element and sifts upward as necessary
	def extract():
		# retrieves top element
		x = l[0]
		# take lowest element and place at top
		loc = 0
		l[0] = l.pop()
		# sift down while causing problems
		while max(l[loc], l[loc * 2], l[loc * 2 + 1]) != l[loc]:
			if l[loc * 2] > l[loc * 2 + 1]:
				l[loc], l[loc * 2] = l[loc * 2], l[loc]
				loc *= 2
			else:
				l[loc], l[loc * 2 + 1] = l[loc * 2 + 1], l[loc]
				loc = loc * 2 + 1
		return x

	# turns a non-heapified list into a heap
	def heapify():
		temp = l
		l = []
		for i in temp:
			insert(i)