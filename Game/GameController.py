from Generic.Controller import Controller

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

	def control(self):
		pass

	def getPlatform(self):
		self.system = platform.system()
	
	

	


			