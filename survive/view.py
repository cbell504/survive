import platform
import os


class View(object):
    def __init__(self, view_text):
        self._view_text = view_text

    def update_view(self):
        for key, value in self._view_text.items():
            print(value)
        print("\n")

    def get_view_text(self):
        return self._view_text

    def set_view_text(self, view_text):
        self._view_text = view_text

    @staticmethod
    def clear_view():
        system = platform.system()
        if system == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def end():
        print("Moving back a screen.\n")

    @staticmethod
    def request_action():
        print("Enter an action.\n")

    @staticmethod
    def victory(enemy):
        print("You have defeated " + enemy.get_name())
