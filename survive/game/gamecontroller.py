from survive.player.playermodel import Player
from survive.activities.crafting.craftingcontroller import CraftingController
from survive.inventory.inventorycontroller import InventoryController
from survive.activities.hunting.huntingcontroller import HuntingController
from survive.generic.controller import Controller
from survive.generic.view import View


class GameController(Controller):
    def __init__(self):
        self._view = {
            0: "Possible Actions:\n",
            1: "(1)  Check Stats",
            2: "(2)  Open Inventory",
            3: "(3)  Craft/Gather Items",
            4: "(4)  Hunt",
            10: "(10) Clear Screen",
            11: "(0)  To Quit\n"
        }

    def start(self, name):
        view = View(self._view)
        player = Player(name)
        crafting_controller = CraftingController()
        inventory_controller = InventoryController()
        huntingController = HuntingController()
        player_input = -1

        while True:
            try:
                view.start()
                player_input = int(input("Enter an action.\n"))
                super().clear_screen()

                if(player_input == 0):
                    print("Game Over\n")
                    break

                elif(player_input == 10):
                    super().clear_screen()

                elif(player_input == 1):
                    player.check_stats()

                elif(player_input == 2):
                    inventory_controller.start(player)

                elif(player_input == 3):
                    print("Entering Crafting Screen.\n")
                    player = crafting_controller.start(player)

                elif(player_input == 4):
                    print("Entering Hunting Screen.\n")
                    player = huntingController.start(player)

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")

            except:
                print("Error occurred.\n")
                raise
