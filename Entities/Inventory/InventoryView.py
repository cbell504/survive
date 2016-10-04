from Entities.View import View

class InventoryView(View):
	
	def __init__(self):
		pass

	def displayInventoryStart(self):
		print("Possible Actions:\n")
		print("(1)  Display")
		print("(10) Clear Screen")
		print("(0)  Back To Game\n")


	def displayInventoryEnd(self):
		print("Moving back to game.\n")

	def displayRequestAction(self):
		print("Enter an action.\n")