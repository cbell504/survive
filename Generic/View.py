import os

class View(object):
	
	def __init__(self, platform):
		self.system = platform

	def clearScreen(self):
		if(self.system == "Windows"):
			os.system('cls')
		else:
			os.system('clear')

	def displayInventoryEnd(self):
		print("Moving back to game.\n")

	def displayRequestAction(self):
		print("Enter an action.\n")

	def startView(self):
		pass

	