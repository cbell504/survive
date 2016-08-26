from ..Player.player import Player

class Game(object):

	def __init__(self):
		pass

	def start(self, name):
		player1 = Player(name)
		
		while True:
			playerInput = -1
			try:
				playerInput = int(input("Enter an action.\n"))
			except ValueError:
				print("Please enter a number.\n")

			if(playerInput == 0 ):
				print("You have quited.\n")
				break
			elif(playerInput == 1):
				pass
			else:
				print("This is not a valid action\n")