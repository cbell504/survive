from Generic.View import View

class CombatView(View):

	def enemyAppears(self, enemy):
		print("Wild " + enemy.getName() + " appeared.\n")

	def startView(self, enemy, player):
		print(enemy.getName())
		print("Health: " + str(enemy.getHealth()) + "\n")

		print("You")
		print("Health: " + str(player.getHealth()) + "\n")

		print("Possible Actions:\n")
		print("(1)  Attack")
		print("(2)  Defend")
		print("(3)  Run")
		print("(10) Clear Screen")
		print("(0)  Back To Game\n")

	def displayNoAnimalFound(self):
		print("You did not find an animial to fight.")


	def displayEnd(self):
		print("Moving back to game.\n")

	def displayRequestAction(self):
		print("Enter an action.\n")

	def win(self, enemy):
		print("You have defeated the " + enemy.getName() + ".\n")