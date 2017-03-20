from Entities.Enemies.EnemyModel import EnemyModel

class HogModel(EnemyModel):
	
	def __init__(self):
		self.name    		= "Hog"
		self.health 		= 5
		self.attacks 		= {"Bite": 1}
		self.specialAttacks = {"Ram" : 2}

	def attack(self):
		pass
		#print("Uses")
		#return self.hog.attacks

	def basicAttack(self):
		return self.attacks["Bite"]

	def specialAttack(self):
		return self.specialAttack["Ram"]