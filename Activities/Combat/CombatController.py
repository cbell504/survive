from Generic.Controller import Controller

from Activities.Combat.CombatView import CombatView
from Entities.Enemies.EnemyController import EnemyController


class CombatController(Controller):
    
    def __init__(self):
        self.combatView = CombatView(self.getPlatform())
        self.enemyController = EnemyController()
        
    def startController(self, player):
        #
        # Generate enemy here
        # Create spawner class and spawner will talk to combat to say what the enemy is doing
        #

        enemy = self.enemyController.generateGenericEnemy()

        self.combatView.enemyAppears(enemy)

        #enemy = Hog

        while enemy.isEnemyAlive():
            playerInput = -1
            try:
                self.combatView.startView(enemy, player)

                playerInput = int(input("Enter an action.\n"))
                print("\n")

                self.clearScreen()

                if(playerInput == 0):
                    self.combatView.displayEnd()
                    break

                elif(playerInput == 1):
                    enemy.setHealth(enemy.getHealth() - player.getBasicAttack())

                elif(playerInput == 2):
                    pass
                
                elif(playerInput == 3):
                    enemy.setLevel(0)

                elif(playerInput == 10):
                    self.clearScreen()

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise
    
        if(enemy.isEnemyAlive() == False):
            self.combatView.win(enemy)

        return player
