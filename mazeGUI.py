import tkinter as tk
import os.path

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
		for j in range(len(l)):
			val = l[i][j]
			if val == 1:
				tiles[i][j] = c.create_rectangle(j * dim, i * dim, (j + 1) * dim, (i + 1) * dim, fill = "black")
			elif tiles[i][j] != None:
				c.delete(tiles[i][j])
				tiles[i][j] = None

# main vars
baseFilePath = "C:/Users/Cedric/Documents/Workplace/Python/mazeSamples"
sizeMap = 505
# generates the window
root = tk.Tk()
# generates the canvas and adjusts size of window to fit
c = tk.Canvas(root, width = sizeMap + 300, height = sizeMap, background = 'white')
c.pack()
# positions widgets on right side
# update map
l, tiles = getMaze(baseFilePath, 0)
dim = (int)(sizeMap // len(l))
update(l, tiles, dim)

root.mainloop()