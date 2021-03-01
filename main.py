from survive.controllers.gamecontroller import GameController

import logging


def main():
    logging.basicConfig(filename='survive.log', level=logging.INFO)
    print("Welcome to Survive.\n ")

    player_input = input("Please enter your name.\n")

    game = GameController()
    game.start(player_input)


if __name__ == "__main__":
    main()
