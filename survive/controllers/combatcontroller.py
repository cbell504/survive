from survive.controllers.controller import Controller
from survive.controllers.enemycontroller import EnemyController


class CombatController(Controller):
    def __init__(self):
        super().__init__()
        self._view_text = {
            0: "Enemy Appears!"
        }
        self._view.set_view_text(self._view_text)
        self._enemy_controller = EnemyController()

    def start(self, player):
        enemy = self._enemy_controller.generate_enemy()

        while enemy.get_health() >= 0:
            try:
                self.update_view(enemy, player, self._view)
                self._view.start()

                player_input = int(input("Enter an action.\n"))
                print("\n")
                self._view.clear_view()

                if player_input == 0:
                    self._view.end()
                    break
                elif player_input == 1:
                    enemy.set_health(enemy.get_health() - player.get_basic_attack())
                    player.set_health(player.get_health() - enemy.get_basic_attack())
                elif player_input == 10:
                    self._view._clear_view()
                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
        self._view.victory(enemy)
        return player

    def update_view(self, enemy, player, view):

        view.update(self._view)
