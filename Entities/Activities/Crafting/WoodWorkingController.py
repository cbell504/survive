from Entities.Controller import Controller
from Entities.Activities.Crafting.WoodWorking import WoodWorking

class WoodWorkingController(Controller):
	def __init__(self):
		self.woodworker = WoodWorking()
		self.itemBuilt = 0

	def start(self, inventory):
		#error here
		totalWood = inventory.slots['Wood']

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
					self.itemBuilt = self.woodworker.buildShelter(totalWood)
					if(self.itemBuilt >= 1):
						inventory.slots['Shelter'] += 1
						self.itemBuilt = 0
						inventory.slots['Wood'] -= 5

				elif(playerInput == 2):
					self.itemBuilt = self.woodworker.buildBoat(totalWood)
					if(self.itemBuilt >= 1):
						inventory.slots['Boat'] += 1
						self.itemBuilt = 0
						inventory.slots['Wood'] -= 5

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

		return inventory