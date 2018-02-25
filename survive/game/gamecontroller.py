from survive.player.playermodel import Player
from survive.activities.crafting.craftingcontroller import CraftingController
from survive.inventory.inventorycontroller import InventoryController
from survive.activities.hunting.huntingcontroller import HuntingController
from survive.generic.controller import Controller


import platform
import os
import time

class GameController(Controller):

    def __init__(self):
        self.system = ""

    def clear_screen(self):
        self.get_platform()
        if(self.system == "Windows"):
            os.system('cls')
        else:
            os.system('clear')

    def get_platform(self):
        self.system = platform.system()

    def start(self, name):
        player = Player(name)
        crafting_controller = CraftingController()
        inventory_controller = InventoryController()
        
        while True:
            playerInput = -1
            try:
                print("Possible Actions:\n")
                print("(1)  Check Stats")
                print("(2)  Check Inventory")
                print("(3)  Use Item")
                print("(4)  Gather Wood")
                print("(5)  Craft A New Item")
                print("(6)  Go Hunting")
                print("(10) Clear Screen")
                print("(0)  To Quit\n")

                playerInput = int(input("Enter an action.\n"))
                print("\n")
                self.clear_screen()

                if(playerInput == 0 ):
                    print("You have quit.\n")
                    break
                elif(playerInput == 10):
                    self.clear_screen()

                elif(playerInput == 1):
                    player.check_stats()

                elif(playerInput == 2):
                    player.check_inventory()

                elif(playerInput == 3):
                    inventory_controller.start(player)

                elif(playerInput == 4):
                    player.cut_down_tree()

                elif(playerInput == 5):
                    print("Entering Crafting Screen.\n")
                    player = crafting_controller.start(player)

                elif(playerInput == 6):
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


            