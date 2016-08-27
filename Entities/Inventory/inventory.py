class Inventory(object):

	def __init__(self):
		self.slots = {'Wood':0}
		self.slotsMaxSize = 10

	def display(self):
		for k, v in self.slots.items():
			print(k,":", v)
		print("\n")


	def isSlotsFull(self):
		if(sum(self.slots.values()) >= self.slotsMaxSize):
			return True
		else:
			return False

