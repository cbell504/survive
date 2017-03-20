from Generic.Controller import Controller

from Activities.Crafting.WoodWorking.WoodWorkingModel import WoodWorkingModel

class WoodWorkingController(Controller):
	def __init__(self):
		self.itemBuilt = 0

	def start(self, player):
		totalWood = player.inventory.slots['Wood']

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
					woodworker = WoodWorkingModel(player)

					player = woodworker.buildShelter(totalWood)

				elif(playerInput == 2):
					woodworker = WoodWorking(player)

					player = woodworker.buildBoat(totalWood)


				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

		return player