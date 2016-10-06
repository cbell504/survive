from Entities.Inventory.InventoryModel import Inventory
from Entities.Activities.Crafting.WoodWorking.WoodWorkingModel import WoodWorking
from Entities.Player.Attributes.AttributeModel import Attribute

class Player(object):
	def __init__(self, playerName):
		self.playerHealth = 10
		self.playerLevel = 1
		self.playerName = playerName
		self.playerStamina = 10
		self.playerStrength = Attribute()
		self.inventory = Inventory()
		self.woodWorkingSkill = WoodWorking()


	def basicAttack(self):
		return 2

	def checkInventory(self):
		self.inventory.display()

	def checkStats(self):
		print("Player Stats")
		print("Current level: ", self.playerLevel)
		print("Current Health: ", self.playerHealth)
		print("Strength: ", self.playerStrength.attributeLevel, "\n")

	def cutDownTree(self):
		if(self.inventory.isSlotsFull()):
			print("Your inventory is full!\n")
			print("You didn't pick up the wood.\n")
		else:
			#TODO Make wood working class give out wood
			if(self.woodWorkingSkill.isWoodGained()):
				print("You got 1 piece of wood!\n")
				self.inventory.addItem('Wood', 1)
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

	def killPlayer(self):
		self.playerHealth = 0

	def levelUp(self, levelGained):
		self.playerLevel = (self.playerLevel + levelGained)

	def reduceHealth(self, damageTaken):
		self.playerHealth = (self.playerHealth - damageTaken)

	def restoreHealth(self, amountRestored):
		self.playerHealth = (self.playerHealth + amountRestored)