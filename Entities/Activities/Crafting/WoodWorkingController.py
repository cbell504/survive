from Entities.Controller import Controller
from Entities.Activities.Crafting.WoodWorking import WoodWorking

class WoodWorkingController(Controller):
	def __init__(self):
		woodworker = WoodWorking()
		itemBuilt = 0

	def start(self, inventory):
		totalWood = inventory['Wood']

		while True:
			playerInput = -1
			try:
				print("Possible Actions:\n")
				print("(1)  Build A Shelter")
				print("(2)  Build A Boat")
				print("(10) Clear Screen")
				print("(0)  Back To Crafting\n")

				playerInput = int(input("Enter an action.\n"))
				print("\n")
				self.clearScreen()

				if(playerInput == 0 ):
					print("Moving back to game.\n")
					break
				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					self.itemBuilt = buildShelter(totalWood)

				elif(playerInput == 2):
					self.itemBuilt = buildBoat(totalWood)

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

		return self.itemBuilt