from survive.controllers.woodworkingcontroller import WoodWorkingController
from survive.controllers.controller import Controller


class CraftingController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Wood Working",
            2: "(10) Clear Screen",
            3: "(0)  Back To Game\n"
        }
        self._view.set_view_text(self._view_text)
        self._woodworking_controller = WoodWorkingController(self._player)

    def game_loop_by_class(self, player_input, loop_condition):
        if player_input == 0:
            loop_condition = 999
        elif player_input == 10:
            self._view.clear_view()
        elif player_input == 1:
            self._player = self._woodworking_controller.start()
        else:
            print("This is not a valid action\n")

        return loop_condition
