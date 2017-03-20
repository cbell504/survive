from Generic.View import View

class HuntingView(View):

	def displayStart(self):
		print("Possible Actions:\n")
		print("(1)  Hunt")
		print("(10) Clear Screen")
		print("(0)  Back To Game\n")

	def displayNoAnimalFound(self):
		print("You did not find an animial to fight.")

	def displayEnd(self):
		print("Moving back to game.\n")

	def displayRequestAction(self):
		print("Enter an action.\n")