from survive.controllers.woodworkingcontroller import WoodWorkingController
from survive.controllers.controller import Controller


class CraftingController(Controller):
    def __init__(self):
        super().__init__()
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Wood Working",
            2: "(10) Clear Screen",
            3: "(0)  Back To Game\n"
        }
        self._view.set_view_text(self._view_text)
        self._woodworking_controller = WoodWorkingController()

    def start(self, player):
        while True:
            try:
                self._view.update_view()
                player_input = int(input("Enter an action.\n"))
                self._view.clear_screen()

                if player_input == 0:
                    self._view.end()
                    break
                elif player_input == 10:
                    self._view.clear_screen()
                elif player_input == 1:
                    player = self._woodworking_controller.start(player)
                else:
                    print("This is not a valid action\n")
            except ValueError:
                print("Please enter a number.\n")
        return player
