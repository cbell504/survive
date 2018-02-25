from survive.generic.controller import Controller
from survive.generic.view import View
from survive.activities.crafting.woodworking.woodworkingmodel import WoodWorking


class WoodWorkingController(Controller):
    def __init__(self):
        self._view = {
            0: "Possible Actions:\n",
            1: "(1)  Cut Wood",
            2: "(2)  Build A Shelter",
            3: "(3)  Build A Boat",
            4: "(10) Clear Screen",
            5: "(0)  Back To Crafting\n"
        }

    def start(self, player):
        view = View(self._view)
        woodworker = WoodWorking()
        playerInput = -1

        while True:
            try:
                view.start()
                playerInput = int(input("Enter an action.\n"))
                super().clear_screen()

                if(playerInput == 0):
                    view.end()
                    break

                elif(playerInput == 10):
                    super().clear_screen()

                elif(playerInput == 1):
                    player = woodworker.cut_wood(player)

                elif(playerInput == 2):
                    player = woodworker.build_shelter(player)

                elif(playerInput == 3):
                    player = woodworker.build_boat(player)

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")

            except:
                print("Error occurred.\n")
                raise

        return player
