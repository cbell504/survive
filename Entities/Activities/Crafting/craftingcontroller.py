from .crafting import Crafting
from .woodworking import Woodworking
import platform
import os

class CraftingController(object):
	
	def __init__(self):
		self.crafter = Crafting()

	def clearScreen(self):
		self.getPlatform()
		if(self.system == "Windows"):
			os.system('cls')
		else:
			os.system('clear')

	def getPlatform(self):
		self.system = platform.system()

	def start(self):
		while True:
			playerInput = -1
			try:
				print("Possible Actions:\n")
				print("(1)  Wood Working")
				print("(10) Clear Screen")
				print("(0)  To Quit\n")

				playerInput = int(input("Enter an action.\n"))
				print("\n")
				self.clearScreen()

				if(playerInput == 0 ):
					print("Moving back to game.\n")
					break
				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					pass

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise