class View(object):
    def __init__(self, view):
        self._view = view

    def update(self, view):
        self._view = view

    def start(self):
        for key, value in self._view.items():
            print(value)
        print("\n")

    def end(self):
        print("Moving back to screen.\n")

    def request_action(self):
        print("Enter an action.\n")

    def victory(self, enemy):
        print("You have defeated " + enemy.get_name())
