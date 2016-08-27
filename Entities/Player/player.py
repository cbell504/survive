from ..Inventory.inventory import Inventory
from ..Activities.woodworking import Woodworking
from .Attributes.attribute import Attribute

class Player(object):
	def __init__(self, playerName):
		self.playerLevel = 1
		self.playerName = playerName
		self.playerStamina = 10
		self.playerStrength = Attribute()
		self.inventory = Inventory()
		self.woodWorkingSkill = Woodworking()

	def checkStats(self):
		print("Player Stats")
		print("Current level: ", self.playerLevel)
		print("Strength: ", self.playerStrength.attributeLevel, "\n")

	def cutDownTree(self):
		if(self.inventory.isSlotsFull()):
			print("Your inventory is full!\n")
			print("You didn't pick up the wood.\n")
		else:
			if(self.woodWorkingSkill.isWoodGained()):
				print("You got 1 piece of wood!\n")
				self.inventory.slots['wood'] += 1
				self.playerStrength.gainExp()
			else:
				print("You failed to cut the tree.\n")

#TODO: Create a file to hold how much health should increase
# based on what the player eats.
	def eatFood(self):
		self.playerHealth += 5

	def gainExperiencePoints(self, experienceGained):
		self.playerExpPoints = (self.playerExpPoints + experienceGained)

	def isPlayerDead(self):
		if(self.playerHealth <= 0):
			return true
		else:
			return false

#TODO: Fix this function
	def increaseStat(self):
		self.playerStrength = 1

	def killPlayer(self):
		self.playerHealth = 0

	def levelUp(self, levelGained):
		self.playerLevel = (self.playerLevel + levelGained)

	def reduceHealth(self, damageTaken):
		self.playerHealth = (self.playerHealth - damageTaken)

	def restoreHealth(self, amountRestored):
		self.playerHealth = (self.playerHealth + amountRestored)