class View(object):
    def __init__(self, view):
        self._view = view

    def update(self, view):
        self._view = view

    def start(self):
        for key, value in self._view.items():
            print(value)
        print("\n")

    @staticmethod
    def end():
        print("Moving back to screen.\n")

    @staticmethod
    def request_action():
        print("Enter an action.\n")

    @staticmethod
    def victory(enemy):
        print("You have defeated " + enemy.get_name())
