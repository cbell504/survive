from Generic.View import View

class GameView(View):
    
    def __init__(self):
        pass

    def startView(self, name):
		player = PlayerModel(name)
		craftingController = CraftingController()
		inventoryController = InventoryController()
		
		while True:
			playerInput = -1
			try:
				print("Possible Actions:\n")
				print("(1)  Check Stats")
				print("(2)  Check Inventory")
				print("(3)  Use Item")
				print("(4)  Gather Wood")
				print("(5)  Craft A New Item")
				print("(6)  Go Hunting")
				print("(10) Clear Screen")
				print("(0)  To Quit\n")

				playerInput = int(input("Enter an action.\n"))
				print("\n")
				self.clearScreen()

				if(playerInput == 0 ):
					print("You have quited.\n")
					break
				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					player.checkStats()

				elif(playerInput == 2):
					player.checkInventory();

				elif(playerInput == 3):
					inventoryController.start(player)

				elif(playerInput == 4):
					player.cutDownTree()

				elif(playerInput == 5):
					print("Entering Crafting Screen.\n")
					player = craftingController.start(player)

				elif(playerInput == 6):
					print("Entering Hunting Screen.\n")
					huntingController = HuntingController()
					player = huntingController.start(player)

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise