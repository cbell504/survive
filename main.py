from Game.GameController import GameController
from Entities.Player.PlayerModel import PlayerModel

def main():
	print("Welcome to Surivthon.\n ")

	playerInput = input("Please enter your name.\n")
	player = PlayerModel(playerInput)

	game = GameController(player)
	game.startController()

if __name__ == "__main__": main()
