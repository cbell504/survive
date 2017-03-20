from Generic.Controller import Controller

from Game.GameView import GameView

from Entities.Player.PlayerModel import PlayerModel
from Entities.Inventory.InventoryController import InventoryController

from Activities.Crafting.CraftingController import CraftingController
from Activities.Hunting.HuntingController import HuntingController


import platform
import os
import time

class GameController(Controller):

	def __init__(self, player):
		self.system = ""
		self.player = player
		self.gameView = GameView(self.getPlatform())
		self.craftingController = CraftingController()
		self.inventoryController = InventoryController()
		self.huntingController = HuntingController()

	def startController(self):
		
		while True:
			playerInput = -1
			try:
				self.gameView.startView()

				playerInput = int(input("Enter an action.\n\n"))
				self.gameView.clearScreen()

				if(playerInput == 0 ):
					print("You have quited the game.\n")
					break
				elif(playerInput == 10):
					self.gameView.clearScreen()

				elif(playerInput == 1):
					self.player.checkStats()

				elif(playerInput == 2):
					self.player.checkInventory();

				elif(playerInput == 3):
					self.inventoryController.start(self.player)

				elif(playerInput == 4):
					self.player.cutWood()

				elif(playerInput == 5):
					print("Entering Crafting Screen.\n")
					self.player = self.craftingController.start(self.player)

				elif(playerInput == 6):
					print("Entering Hunting Screen.\n")
					self.player = self.huntingController.start(self.player)

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

	
	

	


			