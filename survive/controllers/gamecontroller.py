from survive.controllers.craftingcontroller import CraftingController
from survive.controllers.inventorycontroller import InventoryController
from survive.controllers.huntingcontroller import HuntingController
from survive.controllers.controller import Controller


class GameController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Check Stats",
            2: "(2)  Open Inventory",
            3: "(3)  Craft/Gather Items",
            4: "(4)  Hunt",
            10: "(10) Clear Screen",
            11: "(0)  To Quit\n"
        }
        self._view.set_view_text(self._view_text)
        self._crafting_controller = CraftingController(self._player)
        self._inventory_controller = InventoryController(self._player)
        self._huntingController = HuntingController(self._player)

    def game_loop_by_class(self, player_input, loop_condition):
        if player_input == 0:
            print("Game Over")
            loop_condition = 999
        elif player_input == 10:
            self._view.clear_view()
        elif player_input == 1:
            self._player.check_stats()
        elif player_input == 2:
            self._inventory_controller.start()
        elif player_input == 3:
            self._player = self._crafting_controller.start()
        elif player_input == 4:
            self._player = self._huntingController.start()
        else:
            print("This is not a valid action\n")

        return loop_condition
