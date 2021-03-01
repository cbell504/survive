from survive.models.player import Player
from survive.controllers.craftingcontroller import CraftingController
from survive.controllers.inventorycontroller import InventoryController
from survive.controllers.huntingcontroller import HuntingController
from survive.controllers.controller import Controller


class GameController(Controller):
    def __init__(self):
        super().__init__()
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
        self._crafting_controller = CraftingController()
        self._inventory_controller = InventoryController()
        self._huntingController = HuntingController()

    def start(self, name):
        player = Player(name)
        while True:
            try:
                self._view.update_view()
                player_input = int(input("Enter an action.\n"))
                self._view.clear_view()

                if player_input == 0:
                    print("Game Over\n")
                    break
                elif player_input == 10:
                    self._view.clear_view()
                elif player_input == 1:
                    player.check_stats()
                elif player_input == 2:
                    self._inventory_controller.start(player)
                elif player_input == 3:
                    player = self._crafting_controller.start(player)
                elif player_input == 4:
                    player = self._huntingController.start(player)
                else:
                    print("This is not a valid action\n")
            except ValueError:
                print("Please enter a number.\n")
