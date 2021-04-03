from survive.models.model import Model
from survive.models.general.attribute import Attribute


class ActionableEntity(Model):
    def __init__(self):
        super().__init__()
        self.DEFAULT_HEALTH = 10
        self.DEFAULT_NAME = "Chris"
        self.DEFAULT_BASIC_ATTACK = 1
        self.DEFAULT_SPECIAL_ATTACK = 2
        self.DEFAULT_LEVEL = 1

        self._health = self.DEFAULT_HEALTH
        self._name = self.DEFAULT_NAME
        self._basic_attack = self.DEFAULT_BASIC_ATTACK
        self._basic_attacks = {"Bite", 1}
        self._special_attack = self.DEFAULT_SPECIAL_ATTACK
        self._special_attacks = {"Tackle", 2}
        self._level = Attribute(1, "Level")
        self._stamina = Attribute(1, "Stamina")
        self._strength = Attribute(1, "Strength")

    def is_entity_alive(self):
        if self._health > 1:
            return True
        else:
            return False

    def get_basic_attack(self):
        return self._basic_attack

    def set_basic_attack(self, basic_attack):
        if basic_attack >= 0:
            self._basic_attack = basic_attack

    def get_basic_attacks(self):
        return self._basic_attacks

    def set_basic_attacks(self, basic_attacks):
        self._basic_attacks = basic_attacks

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def get_level(self):
        return self._level

    def set_level(self, level):
        if level >= 1:
            self._level = level

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_special_attack(self):
        return self._special_attack

    def set_special_attack(self, special_attack):
        if special_attack >= 0:
            self._special_attack = special_attack

    def get_special_attacks(self):
        return self._special_attacks

    def set_special_attacks(self, special_attacks):
        self._special_attacks = special_attacks
