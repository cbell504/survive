from Entities.Generic.Controller import Controller
from Entities.Activities.Combat.CombatView import CombatView
from Entities.Enemies.EnemyController import EnemyController


class CombatController(Controller):
	
	def __init__(self):
		self.combatView = CombatView()

	def start(self, player):

		# 
		# Generate enemy here
		# Create spawner class and spawner will talk to combat to say what the enemy is doing
		# 
		enemyController = EnemyController()
		enemyController.generateEnemy()
		self.combatView.enemyName = enemyController.enemy.name

		self.combatView.enemyAppears()

		#enemy = Hog

		while(enemyController.enemy.health >=0):

			self.combatView.enemyHealth = enemyController.enemy.health
			self.combatView.playerHealth = player.playerHealth

			playerInput = -1
			try:
				self.combatView.displayStart()

				playerInput = int(input("Enter an action.\n"))
				print("\n")

				self.clearScreen()

				if(playerInput == 0 ):
					self.combatView.displayEnd()
					break

				elif(playerInput == 1):
					enemyController.enemy.health -= player.basicAttack()

				elif(playerInput == 10):
					self.clearScreen()

			

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

		self.combatView.win()

		return player



