from survive.inventory.inventorymodel import Inventory
from survive.attributes.attributemodel import Attribute

import sys


class Player(object):
    def __init__(self, name):
        # Basic player attributes
        self._health = 10
        self._name = name

        # Advanced player attributes
        self._inventory = Inventory()
        self._level = Attribute(1, "Level")
        self._stamina = Attribute(10, "Stamina")
        self._strength = Attribute(2, "Strength")
        self._wood_working = Attribute(1, "Woodworking")

        # Attacks
        self._basic_attack = 1
        self._special_attack = 2

    def check_inventory(self):
        self._inventory.display()

    def check_stats(self):
        print("Player Stats:")
        print("Current level: ", self._level.get_level())
        print("Current Health: ", self._health)
        print("Strength: ", self._strength.get_level())
        print("\n")

    # TODO: Create a file to hold how much health should increase
    # based on what the player eats.
    def eat_food(self):
        if(self.get_inventory().get_item('Food') > 0):
            self._health += 5
        else:
            print("You don't have any food!\n")
        
    def get_basic_attack(self):
        return self._basic_attack + self._strength.get_level()

    def get_health(self):
        return self._health

    def get_inventory(self):
        return self._inventory

    def get_level(self):
        return self._level

    def get_name(self):
        return self._name

    def get_special_attack(self):
        return self._special_attack + self._strength.get_level()

    def get_stamina(self):
        return self._stamina

    def get_strength(self):
        return self._strength

    def is_player_dead(self):
        if(self._health <= 0):
            self.kill_player()
            return True
        else:
            return False

    def kill_player(self):
        self._health = 0
        print("Game Over, you have died.")
        sys.exit()

    def reduce_health(self, damage_taken):
        self._health = (self._health - damage_taken)

    def restore_health(self, amount_restored):
        self._health = (self._health + amount_restored)

    def set_health(self, health):
        self._health = health
        self.is_player_dead()
