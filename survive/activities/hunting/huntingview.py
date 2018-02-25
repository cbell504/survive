from survive.generic.view import View


class HuntingView(View):
    def __init__(self):
        pass

    def display_start(self):
        print("Possible Actions:\n")
        print("(1)  Hunt")
        print("(10) Clear Screen")
        print("(0)  Back To Game\n")

    def display_no_animal_found(self):
        print("You did not find an animial to fight.")

    def display_end(self):
        print("Moving back to game.\n")

    def display_request_action(self):
        print("Enter an action.\n")
