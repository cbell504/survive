from survive.controllers.controller import Controller
from survive.models.activities.crafting.woodworking.woodworkingmodel import WoodWorking


class WoodWorkingController(Controller):
    def __init__(self):
        super().__init__()
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Cut Wood",
            2: "(2)  Build A Shelter",
            3: "(3)  Build A Boat",
            4: "(10) Clear Screen",
            5: "(0)  Back To Crafting\n"
        }
        self._view.set_view_text(self._view_text)

    def start(self, player):
        woodworker = WoodWorking()
        while True:
            try:
                self._view.update_view()
                player_input = int(input("Enter an action.\n"))
                self._view.clear_view()

                if player_input == 0:
                    self._view.end()
                    break
                elif player_input == 10:
                    self._view.clear_view()
                elif player_input == 1:
                    player = woodworker.cut_wood(player)
                elif player_input == 2:
                    player = woodworker.build_shelter(player)
                elif player_input == 3:
                    player = woodworker.build_boat(player)
                else:
                    print("This is not a valid action\n")
            except ValueError:
                print("Please enter a number.\n")

        return player
