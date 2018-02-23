import random
import os.path

# generate and return a square array with side length maxSize
# 0 is unblocked, 1 is blocked
# using method listed in assignment description (DFS)
def generate(maxSize):
	global size
	global unchecked
	size = maxSize
	# initialize two dimensional list, 2 is unchecked
	# need for unchecked: for quick access when traversing, otherwise must generate tuple and search in unchecked
	t = [[2 for x in range(size)] for y in range(size)]
	# create list of unchecked tuples
	# need for unchecked: for quick access when checking for completeness, otherwise must generate list each iteration from t
	unchecked = []
	for i in range(size):
		for j in range(size):
			tup = i, j
			unchecked.append(tup)
	# while loop: while there are unchecked nodes
	while len(unchecked) != 0:
		tup = unchecked.pop(random.randint(0, len(unchecked) - 1))
		t[tup[0]][tup[1]] = 0
		s = []
		s.append(tup)
		# while loop: while there are still parent nodes not fully checked
		while(len(s) != 0):
			traverse(s, t)
	return t

# traverse using given maze generation method, does NOT use recursion due to max recursion depth error in python
def traverse(s, t):
	# get current node
	tup = s[len(s) - 1]
	# get list of unvisited neighbors
	l = getUntouched(tup[0], tup[1], t)
	# if no unvisited neighbors, remove from stack
	if len(l) == 0:
		s.pop()
	# if unvisited neighbor, select random neighbor and determine if blocked
	else:
		x = l[random.randint(0, len(l) - 1)]
		var = random.randint(0, 9)
		if var < 7:
			t[x[0]][x[1]] = 0
			unchecked.remove(x)
			s.append(x)
		else:
			t[x[0]][x[1]] = 1
			unchecked.remove(x)

def getUntouched(r, c, t):
	output = []
	if r + 1 < size and t[r + 1][c] == 2:
		tup = r + 1, c
		output.append(tup)
	if r - 1 >= 0 and t[r - 1][c] == 2:
		tup = r - 1, c
		output.append(tup)
	if c + 1 < size and t[r][c + 1] == 2:
		tup = r, c + 1
		output.append(tup)
	if c - 1 >= 0 and t[r][c - 1] == 2:
		tup = r, c - 1
		output.append(tup)
	return output

def writeTo(baseFilePath, l, n):
	n = "maze" + str(n) + ".txt"
	path = os.path.join(baseFilePath, n)
	with open(path, "w") as f:
		for i in range(len(l)):
			f.write(str(l[i])[1:-1] + "\n")

def main(base, num, dim):
	for i in range(num):
		l = generate(dim)
		writeTo(base, l, i)

baseFilePath = "C:/Users/Cedric/Documents/Workplace/Python/mazeSamples"
main(baseFilePath, 5, 101)