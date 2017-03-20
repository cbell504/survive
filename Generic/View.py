class View(object):
	def __init__(self):
		pass

	def clearScreen(self):
		self.getPlatform()
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

	