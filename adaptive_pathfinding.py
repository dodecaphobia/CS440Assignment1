class Heap(object):
	def __init__(self):
		self.heap = []
		self.objinds = {}

	def heap_lt(self, ind1, ind2):
		if self.heap[ind1].fVal == self.heap[ind2].fVal:
			return self.heap[ind1].gVal > self.heap[ind2].gVal

		return self.heap[ind1].fVal < self.heap[ind2].fVal

	def heap_sift_up(self, ind):
		while ind > 0:
			parentInd = (ind - 1) >> 1
			if self.heap_lt(parentInd, ind):
				break

			# swap elements
			h = self.heap
			h[parentInd], h[ind] = h[ind], h[parentInd]

			# update hash table
			self.objinds[h[parentInd].loc] = parentInd
			self.objinds[h[ind].loc] = ind

			ind = parentInd

	def heap_sift_down(self, ind):
		while True:
			leftInd = ((ind + 1) << 1) - 1
			rightInd = (ind + 1) << 1

			if leftInd > len(self.heap) - 1:
				break

			minInd = leftInd
			if rightInd <= len(self.heap) - 1 and self.heap_lt(rightInd, leftInd):
				minInd = rightInd

			if self.heap_lt(ind, minInd):
				break
		
			# swap elements
			h = self.heap
			h[minInd], h[ind] = h[ind], h[minInd]

			# update hash table
			self.objinds[h[minInd].loc] = minInd
			self.objinds[h[ind].loc] = ind

			ind = minInd

	def heap_peek(self):
		return self.heap[0].fVal

	def heap_empty(self):
		return len(self.heap) == 0

	def heap_delete_min(self):

		h = self.heap
		lastInd = len(h) - 1
		h[lastInd], h[0] = h[0], h[lastInd]

		self.objinds[h[0].loc] = 0
		del self.objinds[h[lastInd].loc]

		retVal = h.pop()
		self.heap_sift_down(0)

		return retVal

	def heap_update(self, newNode):
		ind = self.objinds[newNode.loc]
		self.heap[ind] = newNode

		# needs to go up
		if ind > 0:
			parentInd = (ind - 1) >> 1
			if not self.heap_lt(parentInd, ind):
				self.heap_sift_up(ind)
				return
		
		# needs to go down
		self.heap_sift_down(ind)

	def heap_insert(self, node):
		if node.loc in self.objinds:
			self.heap_update(node)
		else:
			self.objinds[node.loc] = len(self.heap)
			self.heap.append(node)

			self.heap_sift_up(len(self.heap) - 1)

class Node(object):
	def __init__(self, loc):
		self.loc = loc

	def __repr__(self):
		return '; '.join((str(self.loc), str(self.fVal)))

def printMap(mapVals):
	for row in mapVals:
		print("\t".join([str(elem) for elem in row]))

def getG(gVals, loc):
	return gVals[loc[1]][loc[0]]

def setG(gVals, node, gVal):
	loc = node.loc
	gVals[loc[1]][loc[0]] = gVal
	node.gVal = gVal

def calcF(gVals, loc, hVals):
	return getG(gVals, loc) + hVals[loc[1]][loc[0]]

def inBounds(loc, mapWidth, mapHeight):
	return loc[0] >= 0 and loc[1] >= 0 and loc[0] < mapWidth and loc[1] < mapHeight

def isClear(loc, gridMap):
	return gridMap[loc[1]][loc[0]] == 0

def addNeighbor(newLoc, parentNode, gVals, openHeap, goal, hVals):
	currG = getG(gVals, parentNode.loc) + 1
	if getG(gVals, newLoc) > currG:
		newNode = Node(newLoc)
		setG(gVals, newNode, currG)
		newNode.fVal = calcF(gVals, newLoc, hVals)
		newNode.parent = parentNode

		openHeap.heap_insert(newNode)

def compute_path(start, goal, currMap, mapHeight, mapWidth, hVals, numExpanded):
	gVals = [[float('inf') for i in range(mapWidth)] for j in range(mapHeight)]

	startNode = Node(start)
	setG(gVals, startNode, 0)
	startNode.fVal = calcF(gVals, start, hVals)

	openHeap = Heap()
	openHeap.heap_insert(startNode)

	closedList = []

	while not openHeap.heap_empty() and getG(gVals, goal) > openHeap.heap_peek():
		expandNode = openHeap.heap_delete_min()
		expandLoc = expandNode.loc
		closedList.append(expandLoc)

		numExpanded = numExpanded + 1

		newLoc = (expandLoc[0] - 1, expandLoc[1])
		if inBounds(newLoc, mapHeight, mapWidth) and isClear(newLoc, currMap):
			addNeighbor(newLoc, expandNode, gVals, openHeap, goal, hVals)

		newLoc = (expandLoc[0] + 1, expandLoc[1])
		if inBounds(newLoc, mapHeight, mapWidth) and isClear(newLoc, currMap):
			addNeighbor(newLoc, expandNode, gVals, openHeap, goal, hVals)

		newLoc = (expandLoc[0], expandLoc[1] - 1)
		if inBounds(newLoc, mapHeight, mapWidth) and isClear(newLoc, currMap):
			addNeighbor(newLoc, expandNode, gVals, openHeap, goal, hVals)

		newLoc = (expandLoc[0], expandLoc[1] + 1)
		if inBounds(newLoc, mapHeight, mapWidth) and isClear(newLoc, currMap):
			addNeighbor(newLoc, expandNode, gVals, openHeap, goal, hVals)

	if openHeap.heap_empty():
		# print('No path found.')
		return None, numExpanded

	goalNode = openHeap.heap_delete_min()
	while goalNode.loc != goal:
		goalNode = openHeap.heap_delete_min()

	currNode = goalNode
	currLen = 0
	while currNode.loc != start:
		currNode.parent.child = currNode
		currNode = currNode.parent
		currLen = currLen + 1

	for loc in closedList:
		hVals[loc[1]][loc[0]] = currLen - gVals[loc[1]][loc[0]]

	return currNode, numExpanded

def discoverNeighbors(currLoc, mapHeight, mapWidth, knownMap, actualMap):
	newLoc = (currLoc[0] - 1, currLoc[1])
	if inBounds(newLoc, mapHeight, mapWidth):
		knownMap[newLoc[1]][newLoc[0]] = actualMap[newLoc[1]][newLoc[0]]

	newLoc = (currLoc[0] + 1, currLoc[1])
	if inBounds(newLoc, mapHeight, mapWidth):
		knownMap[newLoc[1]][newLoc[0]] = actualMap[newLoc[1]][newLoc[0]]

	newLoc = (currLoc[0], currLoc[1] - 1)
	if inBounds(newLoc, mapHeight, mapWidth):
		knownMap[newLoc[1]][newLoc[0]] = actualMap[newLoc[1]][newLoc[0]]

	newLoc = (currLoc[0], currLoc[1] + 1)
	if inBounds(newLoc, mapHeight, mapWidth):
		knownMap[newLoc[1]][newLoc[0]] = actualMap[newLoc[1]][newLoc[0]]

def init_Hvals(goal, mapWidth, mapHeight):
	hVals = [[0 for i in range(mapWidth)] for j in range(mapHeight)]
	for i in range(mapHeight):
		yDist = abs(goal[1] - i)
		for j in range(mapWidth):
			xDist = abs(goal[0] - j)
			hVals[i][j] = xDist + yDist

	return hVals

def findPath(start, goal, gridMap):
	mapHeight = len(gridMap)
	mapWidth = len(gridMap[0])

	numExpanded = 0

	hVals = init_Hvals(goal, mapWidth, mapHeight)
	# printMap(hVals)

	# deep copy from https://stackoverflow.com/questions/6532881/how-to-make-a-copy-of-a-2d-array-in-python
	pathMap = [row[:] for row in gridMap]

	knownMap = [[0 for i in range(mapWidth)] for j in range(mapHeight)]
	currLoc = start
	discoverNeighbors(currLoc, mapHeight, mapWidth, knownMap, gridMap)

	currNode, numExpanded = compute_path(start, goal, knownMap, mapHeight, mapWidth, hVals, numExpanded)
	while currNode is not None and currNode.child.loc != goal:
		if isClear(currNode.child.loc, knownMap):
			currNode = currNode.child
			pathMap[currNode.loc[1]][currNode.loc[0]] = 4
			discoverNeighbors(currNode.loc, mapHeight, mapWidth, knownMap, gridMap)
		else:
			currNode, numExpanded = compute_path(currNode.loc, goal, knownMap, mapHeight, mapWidth, hVals, numExpanded)

	pathMap[start[1]][start[0]] = 2
	pathMap[goal[1]][goal[0]] = 3

	return pathMap, numExpanded

start = (1, 4)
goal = (4, 4)
testMap = [
	[0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 1, 0]
]
finalMap, numExpanded = findPath(start, goal, testMap)
printMap(finalMap)
print(numExpanded)