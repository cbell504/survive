from survive.generic.controller import Controller
from survive.activities.hunting.huntingview import HuntingView
from survive.activities.hunting.huntingmodel import Hunting
from survive.activities.combat.combatcontroller import CombatController


class HuntingController(Controller):

    def __init__(self):
        self.hunting_view = HuntingView()
        self.hunting = Hunting()

    def start(self, player):
        while True:
            playerInput = -1
            try:
                self.hunting_view.display_start()

                playerInput = int(input("Enter an action.\n"))
                print("\n")

                super().clear_screen()

                if(playerInput == 0):
                    self.hunting_view.display_end()
                    break

                elif(playerInput == 10):
                    super().clear_screen()

                elif(playerInput == 1):
                    if(self.hunting.chance_to_find_animal()):
                        combat_controller = CombatController()
                        combat_controller.start(player)
                    else:
                        self.hunting_view.display_no_animal_found()

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")
            except:
                print("Error occurred.\n")
                raise

        return player
