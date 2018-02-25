from survive.generic.controller import Controller
from survive.activities.gathering.gatheringview import GatheringView
from survive.activities.crafting.craftingcontroller import CraftingController

class GatheringController(Controller):
    
    def __init__(self):
        self.inventoryView = InventoryView()

    def start(self, player):
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

                elif(playerInput == 1):
                    player.inventory.display()

                elif(playerInput == 2):
                    player.eatFood()

                elif(playerInput == 3):
                    craftingController = CraftingController()
                    player = craftingController.start(player)

                elif(playerInput == 9):
                    pass

                elif(playerInput == 10):
                    self.clearScreen()

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise

        return player



