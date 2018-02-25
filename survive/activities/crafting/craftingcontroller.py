from survive.activities.crafting.woodworking.woodworkingcontroller import WoodWorkingController
from survive.generic.controller import Controller
from survive.generic.view import View


class CraftingController(Controller):
    def __init__(self):
        self._view = {
            0: "Possible Actions:\n",
            1: "(1)  Wood Working",
            2: "(10) Clear Screen",
            3: "(0)  Back To Game\n"
        }

    def start(self, player):
        view = View(self._view)
        woodworking_controller = WoodWorkingController()

        while True:
            playerInput = -1
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
                    player = woodworking_controller.start(player)

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")

            except:
                print("Error occurred.\n")
                raise

        return player
