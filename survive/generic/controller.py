import platform
import os

class Controller(object):
    def __init__(self):
        pass

    def clearScreen(self):
        self.getPlatform()
        if(self.system == "Windows"):
            os.system('cls')
        else:
            os.system('clear')

    def getPlatform(self):
        self.system = platform.system()