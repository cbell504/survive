from survive.generic.model import Model
from survive.attributes.attributemodel import Attribute

# TODO: Raise error when values are set below zero


class Enemy(Model):
    def __init__(self):
        self.DEFAULT_HEALTH = 10
        self.DEFAULT_NAME = "Enemy"
        self.DEFAULT_BASIC_ATTACK = 1
        self.DEFAULT_SPECIAL_ATTACK = 3
        self.DEFAULT_LEVEL = 1

        self._health = 10
        self._name = ""
        self._basic_attack = 1
        self._special_attack = 3
        self._level = Attribute(1, "Level")
        

    def is_enemy_alive(self):
        if(self._health > 1):
            return True
        else:
            return False

    def get_basic_attack(self):
        if(self._basic_attack):
            return self._basic_attack
        else:
            return self.DEFAULT_BASIC_ATTACK

    def get_health(self):
        return self._health

    def get_level(self):
        if(self._level):
            return self._level
        else:
            return self.DEFAULT_LEVEL

    def get_name(self):
        if(self._name):
            return self._name
        else:
            return self.DEFAULT_NAME

    def get_special_attack(self):
        if(self._special_attack):
            return self._special_attack
        else:
            return self.DEFAULT_SPECIAL_ATTACK

    def set_basic_attack(self, basic_attack):
        if(basic_attack >= 0):
            self._basic_attack = basic_attack
        else:
            try:
                raise Exception(
                    'Enemy Basic Attack was attempted to be set below zero')
            except Exception as error:
                print("Error Caught: " + repr(error))

    def set_health(self, health):
        self._health = health

    def set_level(self, level):
        if(level >= 1):
            self._level = level
        else:
            try:
                raise Exception(
                    'Enemy Level was attempted to be set below one.')
            except Exception as error:
                print("Error Caught: " + repr(error))

    def set_name(self, name):
        self._name = name

    def set_special_attack(self, special_attack):
        if(special_attack >= 0):
            self._special_attack = special_attack
        else:
            try:
                raise Exception(
                    'Enemy Special Attack was attempted to be set below zero.')
            except Exception as error:
                print("Error Caught: " + repr(error))
