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

	def start(self, player):

		# 
		# Generate enemy here
		# Create spawner class and spawner will talk to combat to say what the enemy is doing
		# 

		enemy = Hog
		while True:
			playerInput = -1
			try:
				self.huntingView.displayStart()

				playerInput = int(input("Enter an action.\n"))
				print("\n")

				self.clearScreen()

				if(playerInput == 0 ):
					self.huntingView.displayEnd()
					break

				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					if(self.hunting.chanceToFindAnimal()):
						combatController = CombatController()
						combatController.start(player)
					else:
						self.huntingView.displayNoAnimalFound()


					

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

		return player



