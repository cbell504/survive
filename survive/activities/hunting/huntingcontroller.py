from survive.generic.controller import Controller
from survive.activities.hunting.huntingmodel import Hunting
from survive.activities.combat.combatcontroller import CombatController
from survive.generic.view import View


class HuntingController(Controller):
    def __init__(self):
        self._view = {
            0: "Possible Actions:\n",
            1: "(1)  Hunt",
            2: "(10) Clear Screen",
            3: "(0)  Back To Game\n"
        }

    def start(self, player):
        view = View(self._view)
        hunting = Hunting()
        combat_controller = CombatController()
        playerInput = -1

        while True:
            try:
                view.start()
                playerInput = int(input("Enter an action.\n"))
                super().clear_screen()

                if(playerInput == 0):
                    view.end()
                    break

                elif(playerInput == 10):
                    super().clear_screen()

                elif(playerInput == 1):
                    if(hunting.chance_to_find_animal()):
                        combat_controller.start(player)
                    else:
                        print("No Animal Found!")

                else:
                    print("This is not a valid action\n")

            except ValueError:
                print("Please enter a number.\n")

            except:
                print("Error occurred.\n")
                raise

        return player
