from Generic.Controller import Controller

from Activities.Combat.CombatView import CombatView

from Entities.Enemies.EnemyModel import EnemyModel
from Entities.Enemies.Animals.HogModel import HogModel

class EnemyController(Controller):
	
	def __init__(self):
		self.enemy = EnemyModel()

	def generateGenericEnemy(self):
		return EnemyModel()

	def getEnemyAttack(self):
		return self.enemy.basicAttack()



