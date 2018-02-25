import platform
import os


class Controller(object):
    def __init__(self):
        self.system = ""

    def clear_screen(self):
        self.get_platform()
        if(self.system == "Windows"):
            os.system('cls')
        else:
            os.system('clear')

    def get_platform(self):
        self.system = platform.system()
