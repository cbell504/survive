from Entities.Player.player import Player
from Entities.Game.game import Game

def main():
	print("Welcome to Surivthon.")

	playerInput = input("Please enter your name.\n")

	game = Game()
	game.start(playerInput)

if __name__ == "__main__": main()
