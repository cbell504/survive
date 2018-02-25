from generic.controller import Controller
from activities.crafting.woodworking.woodworkingmodel import WoodWorking

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
                    woodworker = WoodWorking()

                    player = woodworker.buildShelter(totalWood, player)

                elif(playerInput == 2):
                    woodworker = WoodWorking()

                    player = woodworker.buildBoat(totalWood, player)


                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise

        return player