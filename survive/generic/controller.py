import platform
import os


class Controller(object):
    def __init__(self):
        self._system = ""

    def clear_screen(self):
        self.get_platform()
        if(self._system == "Windows"):
            os.system('cls')
        else:
            os.system('clear')

    def get_platform(self):
        self._system = platform.system()
