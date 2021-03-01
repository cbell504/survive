from random import randint

from survive.models.model import Model


class Hunting(Model):
    def __init__(self):
        super().__init__()
        # Determines player's chance to fight an animal. Default is 20% chance
        self._catch_chance = 20

    def get_catch_chance(self):
        return self._catch_chance

    def set_catch_chance(self, catch_chance):
        self._catch_chance = catch_chance
