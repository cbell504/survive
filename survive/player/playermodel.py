from survive.inventory.inventorymodel import Inventory
from survive.player.attributes.attributemodel import Attribute


class Player(object):
    def __init__(self, name):
        # Basic player attributes
        self.health = 10
        self.name = name

        # Advanced player attributes
        self.inventory = Inventory()
        self.level = Attribute(1, "Level")
        self.stamina = Attribute(10, "Stamina")
        self.strength = Attribute(2, "Strength")
        self.wood_working = Attribute(1, "Woodworking")

        # Attacks
        self.basic_attack = 1
        self.special_attack = 2

    def check_inventory(self):
        self.inventory.display()

    def check_stats(self):
        print("Player Stats:")
        print("Current level: ", self.level.get_level())
        print("Current Health: ", self.health)
        print("Strength: ", self.strength.get_level())
        print("\n")

# TODO: Create a file to hold how much health should increase
# based on what the player eats.
    def eat_food(self):
        self.health += 5

    def is_player_dead(self):
        if(self.health <= 0):
            return True
        else:
            return False

    def kill_player(self):
        self.health = 0

    def reduce_health(self, damage_taken):
        self.health = (self.health - damage_taken)

    def restore_health(self, amount_restored):
        self.health = (self.health + amount_restored)

    def get_basic_attack(self):
        return self.basic_attack + self.strength.get_level()

    def get_special_attack(self):
        return self.special_attack + self.strength.get_level()
