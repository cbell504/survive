from survive.controllers.controller import Controller


class InventoryController(Controller):
    def __init__(self):
        super().__init__()
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Display Inventory",
            2: "(2)  Eat Food",
            3: "(3)  Craft",  # Point to CraftController # End Game choice
            5: "(10) Clear Screen",
            6: "(0)  Back To Game\n"
        }
        self._view.update_view(self._view_text)

    def start(self, player):
        while True:
            try:
                self._view.display_view()
                player_input = int(input("Enter an action.\n"))
                self._view.clear_view()

                if player_input == 0:
                    self._view.end()
                    break
                elif player_input == 1:
                    player.get_inventory().display()
                elif player_input == 2:
                    player.eat_food()
                elif player_input == 10:
                    self._view.clear_screen()
                else:
                    print("This is not a valid action\n")
            except ValueError:
                print("Please enter a number.\n")

        return player
