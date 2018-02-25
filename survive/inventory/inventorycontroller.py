from survive.generic.controller import Controller
from survive.generic.view import View
from survive.activities.crafting.craftingcontroller import CraftingController


class InventoryController(Controller):
    def __init__(self):
        self._view = {
            0: "Possible Actions:\n",
            1: "(1)  Display Inventory",
            2: "(2)  Eat Food",
            3: "(3)  Craft",  # Point to CraftController # End Game choice
            5: "(10) Clear Screen",
            6: "(0)  Back To Game\n"
        }

    def start(self, player):
        view = View(self._view)
        crafting_controller = CraftingController()
        player_input = -1

        while True:
            try:
                view.start()
                player_input = int(input("Enter an action.\n"))
                super().clear_screen()

                if(player_input == 0):
                    view.end()
                    break

                elif(player_input == 1):
                    player.get_inventory().display()

                elif(player_input == 2):
                    player.eat_food()

                elif(player_input == 3):
                    player = crafting_controller.start(player)

                elif(player_input == 10):
                    super().clear_screen()

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")

            except:
                print("Error occurred.\n")
                raise

        return player
