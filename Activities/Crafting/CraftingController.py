from Generic.Controller import Controller

from Activities.Crafting.CraftingView import CraftingView
from Activities.Crafting.WoodWorking.WoodWorkingController import WoodWorkingController

class CraftingController(Controller):
	
	def __init__(self):
		#self.crafter = Crafting()
		self.craftingView = CraftingView()

	def startController(self, player):
		while True:
			self.craftingView.startView()

			playerInput = -1
			try:
				playerInput = int(input("Enter an action.\n"))
				print("\n")
				self.clearScreen()

				if(playerInput == 0 ):
					print("Moving back to game.\n")
					break
				elif(playerInput == 10):
					self.clearScreen()

					player.inventory.display()

				elif(playerInput == 1):
					woodworkingController = WoodWorkingController()
					player = woodworkingController.start(player)

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise
				
		return player