from random import randint

# Items Numbers:
# 1 - Boat
# 2 - Shelter
# 0 - Nothing


#TODO Make this send up a dic to upper controllers
class WoodWorking(object):
	
	def __init__(self, player):
		self.skillLevel = 1
		self.percentageToCut = 2
		self.itemBuilt = 0
		self.player = player


	def isWoodGained(self):
		ranNum = randint(1,10)
		if(ranNum % self.percentageToCut == 0):
			return True
		else:
			return False

	def buildBoat(self, totalWood):
		if(totalWood >= 10):
			print("You have built a boat.")
			self.player.inventory.slots['Boat'] += 1
			self.player.inventory.slots['Wood'] -= 10
		else:
			print("You don't have enough wood")
	
		return self.player

	def buildShelter(self, totalWood):
		if(totalWood >= 5):
			print("You have built a Shelter.")
			self.itemBuilt = 2
			return self.itemBuilt
		else:
			print("You don't have enough wood")
			self.itemBuilt = 0
			return self.itemBuilt