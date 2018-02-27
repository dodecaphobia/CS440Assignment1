try:
	import tkinter as tk # Python 3
except:
	import Tkinter as tk # Python 2
import os

# from pathfinding import findPath
from adaptive_pathfinding import findPath

# generate list from txt, also generate tiles list from dimensions
def getMaze(baseFilePath, num):
	n = "maze" + str(num) + ".txt"
	path = os.path.join(baseFilePath, n)
	l = []
	with open(path, "r") as f:
		for line in f:
			temp = line.split(", ")
			for i in range(len(temp)):
				temp[i] = int(temp[i])
			l.append(temp)
	tiles = [[None for x in range(len(l))] for y in range(len(l))]
	return l, tiles

# draws maze from given list
def update(l, tiles, dim):
	for i in range(len(l)):
		c.create_line(0, i * dim, len(l) * dim, i * dim)
		c.create_line(i * dim, 0, i * dim, len(l) * dim)
		for j in range(len(l)):
			val = l[i][j]
			if val == 1:
				tiles[i][j] = c.create_rectangle(j * dim, i * dim, (j + 1) * dim, (i + 1) * dim, fill = "black")
			elif val == 2:
				tiles[i][j] = c.create_rectangle(j * dim, i * dim, (j + 1) * dim, (i + 1) * dim, fill = "green")
			elif val == 3:
				tiles[i][j] = c.create_rectangle(j * dim, i * dim, (j + 1) * dim, (i + 1) * dim, fill = "red")
			elif val == 4:
				tiles[i][j] = c.create_rectangle(j * dim, i * dim, (j + 1) * dim, (i + 1) * dim, fill = "gray")
			# elif tiles[i][j] != None:
			# 	c.delete(tiles[i][j])
			# 	tiles[i][j] = None

# main vars
baseFilePath = os.path.join(os.getcwd(), "mazeSamples")
for i in range(50):
	l, tiles = getMaze(baseFilePath, i)

	# fully create maze
	start = (4, 4)
	goal = (90, 90)
	l[start[1]][start[0]] = 0
	l[goal[1]][goal[0]] = 0

	l, numExpanded = findPath(start, goal, l)
	print(numExpanded)

# # generates the window
# root = tk.Tk()
# # generates the canvas and adjusts size of window to fit
# sizeMap = 808
# c = tk.Canvas(root, width = sizeMap + 300, height = sizeMap, background = 'white')
# c.pack()
# # positions widgets on right side
# # update map
# dim = (int)(sizeMap // len(l))
# update(l, tiles, dim)

# root.mainloop()