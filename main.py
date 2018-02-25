from Entities.Game.GameController import GameController

def main():
	print("Welcome to Survithon.\n ")

	playerInput = input("Please enter your name.\n")

	game = GameController()
	game.start(playerInput)

if __name__ == "__main__": main()
