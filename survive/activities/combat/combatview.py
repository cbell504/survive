from generic.view import View

class CombatView(View):
	def __init__(self):
		self.enemyName = "Something"
		self.enemyHealth = 1
		self.playerName = "Player"
		self.playerHealth = 1

	def enemyAppears(self):
		print("Wild " + self.enemyName + " appeared.\n")

	def displayStart(self):
		print(self.enemyName)
		print("Health: " + str(self.enemyHealth) + "\n")

		print("You")
		print("Health: " + str(self.playerHealth) + "\n")

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

	def win(self):
		print("You have defeated the " + self.enemyName + ".\n")