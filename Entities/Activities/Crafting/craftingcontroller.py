from .crafting import Crafting
from Entities.Activities.Crafting.WoodWorkingController import WoodWorkingController
from Entities.Controller import Controller

class CraftingController(Controller):
	
	def __init__(self):
		self.crafter = Crafting()
		self.WoodControl = WoodWorkingController()

	def start(self, player):
		while True:
			playerInput = -1
			try:
				print("Possible Actions:\n")
				print("(1)  Wood Working")
				print("(10) Clear Screen")
				print("(0)  Back To Game\n")

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
					player = self.WoodControl.start(player)

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise
				
		return player