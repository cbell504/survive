from ..Inventory.inventory import Inventory

class Player(object):
	def __init__(self, playerName):
		self.playerLevel = 1
		self.playerName = playerName
		self.playerStamina = 10
		self.playerStrength = 10
		self.inventory = Inventory()

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