from survive.generic.model import Model

# TODO: Raise error when values are set below zero


class Enemy(Model):
    def __init__(self):
        # Health
        self.health = 10
        self.DEFAULT_HEALTH = 10

        # Name
        self.name = "Enemy"
        self.DEFAULT_NAME = "Enemy"

        # Attack Power
        self.basic_attack = 1
        self.DEFAULT_BASIC_ATTACK = 1
        self.special_attack = 3
        self.DEFAULT_SPECIAL_ATTACK = 3

        self.level = 1
        self.DEFAULT_LEVEL = 1

    def is_enemy_alive(self):
        if(self.health > 1):
            return True
        else:
            return False

    # Getters and Setters

    def get_basic_attack(self):
        if(self.basic_attack):
            return self.basic_attack
        else:
            return self.DEFAULT_BASIC_ATTACK

    def get_health(self):
        return self.health

    def get_level(self):
        if(self.level):
            return self.level
        else:
            return self.DEFAULT_LEVEL

    def get_name(self):
        if(self.name):
            return self.name
        else:
            return self.DEFAULT_NAME

    def get_special_attack(self):
        if(self.special_attack):
            return self.special_attack
        else:
            return self.DEFAULT_SPECIAL_ATTACK

    def set_basic_attack(self, basic_attack):
        if(basic_attack >= 0):
            self.basic_attack = basic_attack
        else:
            try:
                raise Exception(
                    'Enemy Basic Attack was attempted to be set below zero')
            except Exception as error:
                print("Error Caught: " + repr(error))

    def set_health(self, health):
        self.health = health

    def set_level(self, level):
        if(level >= 1):
            self.level = level
        else:
            try:
                raise Exception(
                    'Enemy Level was attempted to be set below one.')
            except Exception as error:
                print("Error Caught: " + repr(error))

    def set_name(self, name):
        self.name = name

    def set_special_attack(self, special_attack):
        if(special_attack >= 0):
            self.special_attack = special_attack
        else:
            try:
                raise Exception(
                    'Enemy Special Attack was attempted to be set below zero.')
            except Exception as error:
                print("Error Caught: " + repr(error))
