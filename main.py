import logging
from survive.controllers.gamecontroller import GameController
from survive.models.entity.player import Player


def main():
    logging.basicConfig(filename='survive.log', level=logging.INFO)
    print("Welcome to Survive.\n ")
    player_input = input("Please enter your name.\n")
    player = Player(player_input)
    game = GameController(player)
    game.start()


if __name__ == "__main__":
    main()
