class Inventory(object):

	def __init__(self):
		self.slots = {'Wood':0, 'Shelter':0, 'Boat':0}
		self.slotsMaxSize = 10

	def display(self):
		for key, value in self.slots.items():
			print(key,":", value)
		print("\n")


	def isSlotsFull(self):
		if(sum(self.slots.values()) >= self.slotsMaxSize):
			return True
		else:
			return False