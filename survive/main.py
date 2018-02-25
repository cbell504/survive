from game.gamecontroller import GameController

def main():
	print("Welcome to Survive.\n ")

	player_input = input("Please enter your name.\n")

	game = GameController()
	game.start(player_input)

if __name__ == "__main__": main()
