from survive.generic.view import View


class CombatView(View):
    def __init__(self):
        self.enemyName = "Something"
        self.enemyHealth = 1
        self.playerName = "Player"
        self.playerHealth = 1

    def enemy_appears(self):
        print("Wild " + self.enemyName + " appeared.\n")

    def display_start(self):
        print(self.enemyName)
        print("Health: " + str(self.enemyHealth) + "\n")

        print("You")
        print("Health: " + str(self.playerHealth) + "\n")

        print("Possible Actions:\n")
        print("(1)  Attack")
        print("(2)  Defend")
        print("(3)  Run")
        print("(10) Clear Screen")
        print("(0)  Back To Game\n")

    def display_no_animal_found(self):
        print("You did not find an animial to fight.")

    def win(self):
        print("You have defeated the " + self.enemyName + ".\n")
