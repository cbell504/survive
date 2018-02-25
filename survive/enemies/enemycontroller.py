from generic.controller import Controller
from activities.combat.combatview import CombatView

from enemies.enemymodel import Enemy
from enemies.hogmodel import Hog

class EnemyController(Controller):
	
	def __init__(self):
		self.enemy = Enemy()

	def generateEnemy(self):
		self.enemy = Hog()

	def getEnemyAttack(self):
		return self.enemy.basicAttack()



