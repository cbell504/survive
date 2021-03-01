from random import randint

from survive.controllers.controller import Controller
from survive.controllers.combatcontroller import CombatController


class HuntingController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Hunt",
            2: "(10) Clear Screen",
            3: "(0)  Back To Game\n"
        }
        self._view.set_view_text(self._view_text)
        self._combat_controller = CombatController(self._player)
        self._catch_chance = 40

    def game_loop_by_class(self, player_input, loop_condition):
        if player_input == 0:
            loop_condition = 999
        elif player_input == 10:
            self._view.clear_screen()
        elif player_input == 1:
            self.find_animal(self._player)
        else:
            print("This is not a valid action\n")
        return loop_condition

    def find_animal(self, player):
        actual_animal_chance = randint(1, 100)
        if self._catch_chance <= actual_animal_chance:
            self._combat_controller.start()
        else:
            print("No Animal Found!")

    def get_catch_chance(self):
        return self._catch_chance

    def set_catch_chance(self, catch_chance):
        self._catch_chance = catch_chance
