# Repeated Forward A* Algorithm


def A(heapList, start, end):
    return 0


# Heuristic function calculates theoretical remaining distance
# Calculates Manhattan distances where current[0] and end[0] are x coordinates
# and current[1] and end[1] are y coordinates
def h(current, end):
    return abs((current[0] - end[0]) + abs(current[1] - end[1]))


# Function that calculates actual (minimum) distance travelled from the start to current grid
# Calculates Manhattan distances where current[0] and start[0] are x coordinates
# and current[1] and start[1] are y coordinates
def g(start, current):
    return abs((current[0] - start[0]) + abs(current[1] - end[1]))


# Computes the f value by calling the heuristic function and distance travelled function
# f value is used to decide what coordinate to expand next
def f(start, current, end):
    return g(start, current) + h(current, end)


# Returns a list of traverse-able neighboring nodes of current node
def getNeighbors(current, grid):
    neighborList = []
    if()


# Computes the shortest path between start and end
def computePath_repeated(start, end, grid):
    openList = []
    current = (start[0], start[1])
    if()

# assume minHeap, easily fixable otherwise
/* class Heap(object):
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
			insert(i) */