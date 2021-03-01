from survive.controllers.controller import Controller


class InventoryController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Display Inventory",
            2: "(2)  Eat Food",
            3: "(3)  Craft",  # Point to CraftController # End Game choice
            5: "(10) Clear Screen",
            6: "(0)  Back To Game\n"
        }
        self._view.set_view_text(self._view_text)

    def game_loop_by_class(self, player_input, loop_condition):

        if player_input == 0:
            loop_condition = 999
        elif player_input == 1:
            self._player.get_inventory().display()
        elif player_input == 2:
            self._player.eat_food()
        elif player_input == 10:
            self._view.clear_screen()
        else:
            print("This is not a valid action\n")

        return loop_condition
