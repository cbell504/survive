class Inventory(object):

	def __init__(self):
		self.slots = {'wood':0}
		self.slotsMaxSize = 10


	def isSlotsFull(self):
		if(sum(self.slots.values()) >= self.slotsMaxSize):
			return True
		else:
			return False

