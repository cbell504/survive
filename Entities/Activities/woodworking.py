from random import randint

class Woodworking(object):
	
	def __init__(self):
		self.skillLevel = 1
		self.percentageToCut = 2


	def isWoodGained(self):
		ranNum = randint(1,10)
		if(ranNum % self.percentageToCut == 0):
			return True
		else:
			return False

	