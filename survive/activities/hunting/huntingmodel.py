from random import randint


class Hunting(object):
    def __init__(self):
        self._percentage_to_catch = 2

    def chance_to_find_animal(self):
        ranNum = randint(1, 10)
        if(ranNum <= 7):
            return True
        else:
            return False

    # Determines what a player will fight
