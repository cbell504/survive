class View(object):
    def __init__(self, view):
        self.view = view

    def start(self):
        for key, value in self.view.items():
            print(value)
        print("\n")

    def end(self):
        print("Moving back to game.\n")

    def request_action(self):
        print("Enter an action.\n")
