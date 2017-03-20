class AttributeModel(object):
	
	def __init__(self):
		self.attributeLevel = 1
		self.attributeExpPoints = 0
		self.attributeExpToNextLevel = 5

	def gainExp(self):
		self.attributeExpPoints += 1
		self.levelUp()

	def isItTimeToLevelUp(self):
		if(self.attributeExpPoints >= self.attributeExpToNextLevel):
			return True
		else:
			return False

	def levelUp(self):
		if(self.isItTimeToLevelUp()):
			print("You have leveled up!\n")
			self.attributeLevel += 1
			self.attributeExpPoints = 0
			self.attributeExpToNextLevel = \
			(self.attributeExpToNextLevel * 2)

		else:
			pass

