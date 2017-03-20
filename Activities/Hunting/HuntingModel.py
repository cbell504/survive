from Generic.Model import Model

from random import randint

class HuntingModel(Model):
	
	def __init__(self):
		self.percentageToCatch = 2


	def chanceToFindAnimal(self):
		ranNum = randint(1,10)
		if(ranNum <= 7):
			return True
		else:
			return False



	#Determines what a player will fight