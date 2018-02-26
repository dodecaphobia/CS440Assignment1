# Repeated Forward A* Algorithm

import math
import heapq
'''def A(heapList, start, end):
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

h = Heap(list)
minElem = h.extract()
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
			insert(i) '''


class Node(object):

	def __init__(self, x_coordinate, y_coordinate, tile_type, parent_node, g_score, f_score):
		self.x = x_coordinate
		self.y = y_coordinate
		self.tile_type = tile_type
		self.parent = parent_node
		self.g_score = g_score
		self.f_score = f_score

	def __lt__(self, other):
		return self.g_score <= other.g_score

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y


def h(start, end):
	return abs(start[0] - end[0]) + abs(start[1] - end[1])


def g(current):
	current.g_score = current.parent.g_score + 1


def f(start, current, end):
	current.f_score = current.g_score + h(start, end)


def get_neighbors(current, grid):
	neighbors = []
	n1 = Node(current.x - 1, current.y, grid[current.x - 1][current.y], current, math.inf, math.inf)
	n2 = Node(current.x + 1, current.y, grid[current.x + 1][current.y], current, math.inf, math.inf)
	n3 = Node(current.x, current.y - 1, grid[current.x][current.y - 1], current, math.inf, math.inf)
	n4 = Node(current.x, current.y + 1, grid[current.x][current.y + 1], current, math.inf, math.inf)
	neighbors.extend([n1, n2, n3, n4])

	for x in range(0, 3):
		neighbor = neighbors[x]
		if any((neighbor.x < 0, neighbor.y < 0, neighbor.x > len(grid) - 1, neighbor.y > len(grid) - 1, neighbor.tile_type == 1)):
			neighbors.remove(neighbor)
	return neighbors


def compute_path(start, end, grid):

	# Initialize the open and closed lists
	open_list = []
	closed_list = []

	# Initialize current to start. Coordinates should be same as start as well as tile type
	# Since this is the starting node, it does not have a parent. g_score is set to 0, f_score is set to heuristic
	current = Node(start[0], start[1], grid[start[0]][start[1]], None, 0, h(start, end))

	# Add current to the closed list
	closed_list.append(current)

	# Get list of all neighbors of current and add them to the open list
	# Update the g-values and f-values of children in the open list
	# Heapify the open_list
	neighbors = get_neighbors(current, grid)
	open_list.extend(neighbors)
	for x in open_list:
		g(open_list[x])
		f(start, open_list[x], end)
	heapq.heapify(open_list)

	# While open list is not empty
	# Check each tile in the open list to see if it exists in the closed list
	# Existing being defined as having the same x and y coordinates
	# If tile does not exist in closed list update the g-value such that g-value is one greater than parent's g-value
	# If tile exist in closed list, update g and f values of the tile and neighbors/descendants and re-heapify
	while open_list:
		current_tile = heapq.heappop(open_list)
		current_neighbors = get_neighbors(current_tile, grid)
		for i in current_neighbors:
			for j in closed_list:
				if current_neighbors[i].x == closed_list[j].x and current_neighbors[i].y == closed_list[j].y:
					# Goes in this branch if same coordinates are detected in the closed list

				else: