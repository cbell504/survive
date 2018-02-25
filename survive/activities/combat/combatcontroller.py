from survive.generic.controller import Controller
from survive.activities.combat.combatview import CombatView
from survive.enemies.enemycontroller import EnemyController


class CombatController(Controller):

    def __init__(self):
        self.combat_view = CombatView()

    def start(self, player):

        #
        # Generate enemy here
        # Create spawner class and spawner will talk to combat to say what the enemy is doing
        #
        enemy_controller = EnemyController()
        enemy_controller.generate_enemy()
        self.combat_view.enemy_name = enemy_controller.enemy.name

        self.combat_view.enemy_appears()

        #enemy = Hog

        while(enemy_controller.enemy.health >= 0):

            self.combat_view.enemy_health = enemy_controller.enemy.health
            self.combat_view.player_health = player.player_health

            player_input = -1
            try:
                self.combat_view.display_start()

                player_input = int(input("Enter an action.\n"))
                print("\n")

                super().clear_screen()

                if(player_input == 0):
                    self.combat_view.display_end()
                    break

                elif(player_input == 1):
                    enemy_controller.enemy.health -= player.basic_attack()

                elif(player_input == 10):
                    self.clear_screen()

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise

        self.combat_view.win()

        return player
