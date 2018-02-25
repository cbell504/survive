from random import randint


class WoodWorking(object):
    def __init__(self):
        self._percentage_to_cut = 2

    def build_boat(self, player):
        if(player.get_inventory().get_slots()['Wood'] >= 10):
            print("You have built a boat.\n")
            player.get_inventory().get_slots()['Boat'] += 1
            player.get_inventory().get_slots()['Wood'] -= 10
        else:
            print("You don't have enough wood.\n")

        return player

    def build_shelter(self, player):
        if(player.get_inventory().get_slots()['Wood'] >= 5):
            print("You have built a Shelter.\n")
            player.get_inventory().get_slots()['Shelter'] += 1
            player.get_inventory().get_slots()['Wood'] -= 5
        else:
            print("You don't have enough wood.\n")

        return player

    def cut_wood(self, player):
        if(player.get_inventory().is_slots_full()):
            print("Your inventory is full!\n")
            print("You didn't pick up the wood.\n")
        else:
            # TODO Make wood working class give out wood
            if(self.is_wood_gained()):
                print("You got 1 piece of wood!\n")
                player.get_inventory().add_item('Wood', 1)
                player.get_strength().gain_exp()
                player.get_stamina().gain_exp()

            else:
                print("You failed to cut the tree.\n")
        return player

    def is_wood_gained(self):
        ranNum = randint(1, 10)
        if(ranNum % self._percentage_to_cut == 0):
            return True
        else:
            return False
