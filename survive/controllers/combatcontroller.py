import sys

from survive.controllers.controller import Controller
from survive.controllers.enemycontroller import EnemyController


class CombatController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self._enemy_controller = EnemyController(self._player)
        self._enemy = self._enemy_controller.generate_enemy()
        self._view_text = {
            0: self._enemy.get_name(),
            1: "Health: " + str(self._enemy.get_health()) + "\n",
            2: self._player.get_name(),
            3: "Health: " + str(self._player.get_health()) + "\n",
            4: "Possible Actions:\n",
            5: "(1)  Attack",
            6: "(2)  Defend",
            7: "(3)  Run",
            8: "(10) Clear Screen",
            9: "(0)  Back To Game\n"
        }
        self._view.set_view_text(self._view_text)

    def game_loop_by_class(self, player_input, loop_condition):
        if player_input == 0:
            loop_condition = 999
        elif player_input == 1:
            self._enemy.set_health(self._enemy.get_health() - self._player.get_basic_attack())
            self._player.set_health(self._player.get_health() - self._enemy.get_basic_attack())
        elif player_input == 10:
            self._view.clear_view()
        else:
            print("This is not a valid action\n")
        self.is_combat_over()
        return loop_condition

    def is_combat_over(self):
        if self._enemy.get_health() <= 0:
            self._view.victory(self._enemy)
        if self._player.get_health <= 0:
            print("You have died. Game Over")
            sys.exit()
