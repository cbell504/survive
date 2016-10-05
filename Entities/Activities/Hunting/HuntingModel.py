from random import randint

class Hunting(object):
	

	def __init__(self):
		percentageToCatch = 2


	def chanceToFindAnimal(self):
		ranNum = randint(1,10)
		if(ranNum % self.percentageToCatch == 0):
			return True
		else:
			return False



	#Determines what a player will fight