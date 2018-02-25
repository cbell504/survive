from survive.generic.controller import Controller
from survive.inventory.inventoryview import InventoryView
from survive.activities.crafting.craftingcontroller import CraftingController

class InventoryController(Controller):
    
    def __init__(self):
        self.inventory_view = InventoryView()

    def start(self, player):
        while True:
            player_input = -1
            try:
                self.inventory_view.display_start()

                player_input = int(input("Enter an action.\n"))
                print("\n")

                super().clear_screen()

                if(player_input == 0 ):
                    self.inventory_view.display_end()
                    break

                elif(player_input == 1):
                    player.inventory.display()

                elif(player_input == 2):
                    player.eat_food()

                elif(player_input == 3):
                    crafting_controller = CraftingController()
                    player = crafting_controller.start(player)

                elif(player_input == 9):
                    pass

                elif(player_input == 10):
                    super.clear_screen()

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise

        return player



