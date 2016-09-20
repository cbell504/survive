from ..Player.player import Player
from ..Activities.Crafting.craftingcontroller import CraftingController

import platform
import os
import time

class Game(object):

	def __init__(self):
		self.system = ""

	def clearScreen(self):
		self.getPlatform()
		if(self.system == "Windows"):
			os.system('cls')
		else:
			os.system('clear')

	def getPlatform(self):
		self.system = platform.system()

	def start(self, name):
		player = Player(name)
		craftingController = CraftingController()
		
		while True:
			playerInput = -1
			try:
				print("Possible Actions:\n")
				print("(1)  Check Stats")
				print("(2)  Check Inventory")
				print("(3)  Gather Wood")
				print("(4)  Craft A New Item")
				print("(10) Clear Screen")
				print("(0)  To Quit\n")

				playerInput = int(input("Enter an action.\n"))
				print("\n")
				self.clearScreen()

				if(playerInput == 0 ):
					print("You have quited.\n")
					break
				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					player.checkStats()

				elif(playerInput == 2):
					player.checkInventory();

				elif(playerInput == 3):
					player.cutDownTree()

				elif(playerInput == 4):
					print("Entering Crafting Screen.\n")
					player.inventory = craftingController.start(player.inventory)

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise


			