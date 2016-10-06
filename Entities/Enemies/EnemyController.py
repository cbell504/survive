from Entities.Generic.Controller import Controller
from Entities.Activities.Combat.CombatView import CombatView

from Entities.Enemies.EnemyModel import Enemy
from Entities.Enemies.HogModel import Hog

class EnemyController(Controller):
	
	def __init__(self):
		self.enemy = Enemy()

	def generateEnemy(self):
		self.enemy = Hog()

	def getEnemyAttack(self):
		return self.enemy.basicAttack()



