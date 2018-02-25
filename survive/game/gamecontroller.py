from survive.player.playermodel import Player
from survive.activities.crafting.craftingcontroller import CraftingController
from survive.inventory.inventorycontroller import InventoryController
from survive.activities.hunting.huntingcontroller import HuntingController
from survive.generic.controller import Controller
from survive.generic.view import View


import platform
import os
import time


class GameController(Controller):
    def __init__(self):
        self.view = {
            0: "Possible Actions:\n",
            1: "(1)  Check Stats",
            2: "(2)  Check Inventory",
            3: "(3)  Use Item",
            4: "(4)  Gather Wood",
            5: "(5)  Craft A New Item",
            6: "(6)  Go Hunting",
            10: "(10) Clear Screen",
            11: "(0)  To Quit\n"
        }

    def start(self, name):
        view = View(self.view)
        player = Player(name)
        crafting_controller = CraftingController()
        inventory_controller = InventoryController()
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
                    player.check_inventory()

                elif(player_input == 3):
                    inventory_controller.start(player)

                elif(player_input == 4):
                    player.cut_down_tree()

                elif(player_input == 5):
                    print("Entering Crafting Screen.\n")
                    player = crafting_controller.start(player)

                elif(player_input == 6):
                    print("Entering Hunting Screen.\n")
                    huntingController = HuntingController()
                    player = huntingController.start(player)

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise
