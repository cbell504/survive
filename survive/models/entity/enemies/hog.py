from survive.models.entity.enemies import Enemy
from survive.models.general.attribute import Attribute


class Hog(Enemy):
    def __init__(self):
        super().__init__()
        self._name = "Hog"
        self._health = 5
        self._level = Attribute(1, "Level")
        self._attacks = {"Bite": 1}
        self._special_attacks = {"Ram": 2}

    def get_attacks(self):
        return self._attacks

    def get_special_attacks(self):
        return self._special_attacks
