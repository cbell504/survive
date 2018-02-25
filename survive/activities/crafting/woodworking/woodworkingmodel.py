from random import randint

# Items Numbers:
# 1 - Boat
# 2 - Shelter
# 0 - Nothing


#TODO Make this send up a dic to upper controllers
class WoodWorking(object):
    
    def __init__(self):
        self.skill_level = 1
        self.percentage_to_cut = 2
        self.item_built = 0


    def is_wood_gained(self):
        ranNum = randint(1,10)
        if(ranNum % self.percentage_to_cut == 0):
            return True
        else:
            return False

    def build_boat(self, total_wood, player):
        if(total_wood >= 10):
            print("You have built a boat.\n")
            player.inventory.slots['Boat'] += 1
            player.inventory.slots['Wood'] -= 10
        else:
            print("You don't have enough wood.\n")
    
        return player

    def build_shelter(self, total_wood, player):
        if(total_wood >= 5):
            print("You have built a Shelter.\n")
            player.inventory.slots['Shelter'] += 1
            player.inventory.slots['Wood'] -= 5
        else:
            print("You don't have enough wood.\n")

        return player