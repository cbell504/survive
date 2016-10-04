from Entities.Controller import Controller
from Entities.Inventory.InventoryView import InventoryView

class HuntingController(Controller):
	
	def __init__(self):
		self.inventoryView = InventoryView()

	def startIiew(self, player):
		while True:
			playerInput = -1
			try:
				self.inventoryView.displayStart()

				playerInput = int(input("Enter an action.\n"))
				print("\n")

				self.clearScreen()

				if(playerInput == 0 ):
					self.inventoryView.displayEnd()
					break

				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					player.inventory.display()

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

		return player



