from inventory.inventorymodel import Inventory
from activities.crafting.woodworking.woodworkingmodel import WoodWorking
from player.attributes.attributemodel import Attribute


class Player(object):
    def __init__(self, player_name):
        # Basic player attributes
        self.player_health = 10
        self.player_level = 1
        self.player_name = player_name
        self.player_stamina = 10

        # Advanced player attributes
        self.player_strength = Attribute()
        self.inventory = Inventory()
        self.wood_working = WoodWorking()

    def basic_attack(self):
        return 2

    def check_inventory(self):
        self.inventory.display()

    def check_stats(self):
        print("Player Stats")
        print("Current level: ", self.player_level)
        print("Current Health: ", self.player_health)
        print("Strength: ", self.player_strength.attributeLevel, "\n")

    def cut_down_tree(self):
        if(self.inventory.isSlotsFull()):
            print("Your inventory is full!\n")
            print("You didn't pick up the wood.\n")
        else:
            # TODO Make wood working class give out wood
            if(self.wood_working.isWoodGained()):
                print("You got 1 piece of wood!\n")
                self.inventory.addItem('Wood', 1)
                self.player_strength.gainExp()

            else:
                print("You failed to cut the tree.\n")

# TODO: Create a file to hold how much health should increase
# based on what the player eats.
    def eat_food(self):
        self.player_health += 5

    def gain_experience_points(self, experience_gained):
        self.player_exp_points = (self.player_exp_points + experience_gained)

    def is_player_dead(self):
        if(self.player_health <= 0):
            return True
        else:
            return False

    def kill_player(self):
        self.player_health = 0

    def level_up(self, level_gained):
        self.player_level = (self.player_level + level_gained)

    def reduce_health(self, damage_taken):
        self.player_health = (self.player_health - damage_taken)

    def restore_health(self, amount_restored):
        self.player_health = (self.player_health + amount_restored)
