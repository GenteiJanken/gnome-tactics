import settings, random, math, 

class EntityManager:

	def __init__(self, event, field):
		self.event = event
		self.field = field
		self.nextId = 0
		self.entities = dict()
		self.stack = list()	#Possibly will have "The Stack" and a system of interrupt spells

#Entities are either Units (mages, creatures) or Spells (instants, sorceries, artifacts)
	
	def new_unit():
		pass

	def new_spell():
		pass

class Entity:

	def __init__(self, event, id, field, x, y):
		pass




class Unit(Entity):
	pass

class Spell(Entity):
	pass
