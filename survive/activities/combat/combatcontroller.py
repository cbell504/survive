from survive.generic.controller import Controller
from survive.generic.view import View
from survive.enemies.enemycontroller import EnemyController


class CombatController(Controller):
    def __init__(self):
        self._view = {
            0: "Enemy Appears!"
        }

    def start(self, player):
        view = View(self._view)
        enemy_controller = EnemyController()
        enemy = enemy_controller.generate_enemy()
        player_input = -1

        while(enemy.get_health() >= 0):
            try:
                self.update_view(enemy, player, view)
                view.start()

                player_input = int(input("Enter an action.\n"))
                print("\n")

                super().clear_screen()

                if(player_input == 0):
                    view.end()
                    break

                elif(player_input == 1):
                    enemy.set_health(enemy.get_health() - player.get_basic_attack())
                    player.set_health(player.get_health() - enemy.get_basic_attack())

                elif(player_input == 10):
                    super().clear_screen()

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")

            except:
                print("Error occurred.\n")
                raise

        view.victory(enemy)

        return player

    def update_view(self, enemy, player, view):
        self._view = {
            0: enemy.get_name(),
            1: "Health: " + str(enemy.get_health()) + "\n",
            2: player.get_name(),
            3: "Health: " + str(player.get_health()) + "\n",
            4: "Possible Actions:\n",
            5: "(1)  Attack",
            6: "(2)  Defend",
            7: "(3)  Run",
            8: "(10) Clear Screen",
            9: "(0)  Back To Game\n"
        }
        view.update(self._view)
