from survive.enemies.enemymodel import Enemy
from survive.attributes.attributemodel import Attribute


class Hog(Enemy):
    def __init__(self):
        self._name = "Hog"
        self._health = 5
        self._level = Attribute(1, "Level")
        self._attacks = {"Bite": 1}
        self._special_attacks = {"Ram": 2}

    def get_basic_attack(self):
        return self._attacks["Bite"]

    def get_special_attack(self):
        return self._special_attacks["Ram"]
