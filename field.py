import settings, random, math

class Field:

	def __init__(self, event, size):
		self.size = size
		self.spaces = []
		for i in xrange(size):
			self.spaces.append([])
			for j in xrange(size):
				self.spaces[i].append( Space(event, i, j) )

	def populate(self):
		pass	


class Space:

	def(self, event, x, y):
		self.entities = []
		self.x = x
		self.y = y

	#places entity on space
	def spawn(self, entity):
		pass
	
