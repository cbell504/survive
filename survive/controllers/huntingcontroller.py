from random import randint

from survive.controllers.controller import Controller
from survive.models.activities.hunting.hunting import Hunting
from survive.controllers.combatcontroller import CombatController


class HuntingController(Controller):
    def __init__(self):
        super().__init__()
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Hunt",
            2: "(10) Clear Screen",
            3: "(0)  Back To Game\n"
        }
        self._view.update_view(self._view_text)
        self._combat_controller = CombatController()
        self._catch_chance = 40

    def start(self, player):
        hunting = Hunting()
        while True:
            try:
                self._view.update_view()
                player_input = int(input("Enter an action.\n"))
                self._view.clear_screen()

                if player_input == 0:
                    self._view.end()
                    break
                elif player_input == 10:
                    self._view.clear_screen()
                elif player_input == 1:
                    self.find_animal(player)
                else:
                    print("This is not a valid action\n")
            except ValueError:
                print("Please enter a number.\n")

        return player

    def find_animal(self, player):
        actual_animal_chance = randint(1, 100)
        if self._catch_chance <= actual_animal_chance:
            self._combat_controller.start(player)
        else:
            print("No Animal Found!")
