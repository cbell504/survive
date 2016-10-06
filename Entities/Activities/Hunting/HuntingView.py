from Entities.Generic.View import View

class HuntingView(View):
	def __init__(self):
		pass

	def displayStart(self):
		print("Possible Actions:\n")
		print("(1)  Hunt")
		print("(10) Clear Screen")
		print("(0)  Back To Game\n")

	def displayNoAnimalFound(self):
		print("You did not find an animial to fight.")