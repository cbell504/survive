from survive.generic.controller import Controller
from survive.activities.combat.combatview import CombatView

from survive.enemies.enemymodel import Enemy
from survive.enemies.hogmodel import Hog

class EnemyController(Controller):
    
    def __init__(self):
        self.enemy = Enemy()

    def generateEnemy(self):
        self.enemy = Hog()

    def getEnemyAttack(self):
        return self.enemy.basicAttack()



