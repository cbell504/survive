from survive.generic.controller import Controller
from survive.activities.crafting.woodworking.woodworkingmodel import WoodWorking


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
                super().clear_screen()

                if(playerInput == 0):
                    print("Moving back to game.\n")
                    break
                elif(playerInput == 10):
                    super().clear_screen()

                elif(playerInput == 1):
                    woodworker = WoodWorking()

                    player = woodworker.build_shelter(totalWood, player)

                elif(playerInput == 2):
                    woodworker = WoodWorking()

                    player = woodworker.build_boat(totalWood, player)

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise

        return player
