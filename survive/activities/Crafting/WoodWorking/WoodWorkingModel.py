from random import randint

# Items Numbers:
# 1 - Boat
# 2 - Shelter
# 0 - Nothing


#TODO Make this send up a dic to upper controllers
class WoodWorking(object):
	
	def __init__(self):
		self.skillLevel = 1
		self.percentageToCut = 2
		self.itemBuilt = 0


	def isWoodGained(self):
		ranNum = randint(1,10)
		if(ranNum % self.percentageToCut == 0):
			return True
		else:
			return False

	def buildBoat(self, totalWood, player):
		if(totalWood >= 10):
			print("You have built a boat.\n")
			player.inventory.slots['Boat'] += 1
			player.inventory.slots['Wood'] -= 10
		else:
			print("You don't have enough wood.\n")
	
		return player

	def buildShelter(self, totalWood, player):
		if(totalWood >= 5):
			print("You have built a Shelter.\n")
			player.inventory.slots['Shelter'] += 1
			player.inventory.slots['Wood'] -= 5
		else:
			print("You don't have enough wood.\n")

		return player