from Generic.Controller import Controller

from Activities.Crafting.WoodWorking.WoodWorkingModel import WoodWorkingModel

class WoodWorkingController(Controller):
	def __init__(self):
		self.itemBuilt = 0
		self.woodWorkingView = WoodWorkingView()

	def start(self, player):
		totalWood = player.inventory.slots['Wood']

		while True:
			playerInput = -1
			self.woodWorkingView.startView()
			
			try:
				playerInput = int(input("Enter an action.\n"))
				print("\n")
				self.clearScreen()

				if(playerInput == 0 ):
					print("Moving back to game.\n")
					break
				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					#TODO: Fix this junk
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