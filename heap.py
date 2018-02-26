# assume minHeap, easily fixable otherwise
class Heap(object):
	l = []

	# adds an element to the bottom of the heap
	def insert(self, x):
		self.l.append(x)
		loc = len(self.l) - 1
		# while not at the top of the heap and greater than the parent, swap
		while loc != 0 and self.l[loc] < self.l[(int)(loc // 2)]:
			self.l[loc], self.l[(int)(loc // 2)] = self.l[(int)(loc // 2)], self.l[loc]
			loc = (int)(loc // 2)

	# removes the top element and sifts upward as necessary
	def extract(self):
		if len(self.l) == 0:
			return -1
		# retrieves top element
		x = self.l[0]
		if len(self.l) == 1:
			x = self.l.pop()
			return x
		# take lowest element and place at top
		loc = 0
		self.l[0] = self.l.pop()
		# sift down while less than values below it
		while loc * 2 < len(self.l) and min(self.l[loc], self.l[loc * 2]) != self.l[loc] and (loc * 2 + 1 < len(self.l) or min(self.l[loc], self.l[loc * 2 + 1]) != self.l[loc]):
			if self.l[loc * 2] < self.l[loc * 2 + 1]:
				self.l[loc], self.l[loc * 2] = self.l[loc * 2], self.l[loc]
				loc *= 2
			else:
				self.l[loc], self.l[loc * 2 + 1] = self.l[loc * 2 + 1], self.l[loc]
				loc = loc * 2 + 1
		return x
