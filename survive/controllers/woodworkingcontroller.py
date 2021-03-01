from random import randint

from survive.controllers.controller import Controller


class WoodWorkingController(Controller):
    def __init__(self, player):
        super().__init__(player)
        self._view_text = {
            0: "Possible Actions:\n",
            1: "(1)  Cut Wood",
            2: "(2)  Build A Shelter",
            3: "(3)  Build A Boat",
            4: "(10) Clear Screen",
            5: "(0)  Back To Crafting\n"
        }
        self._view.set_view_text(self._view_text)
        self._percentage_to_cut = 2

    def game_loop_by_class(self, player_input, loop_condition):
        if player_input == 0:
            loop_condition = 999
        elif player_input == 10:
            self._view.clear_view()
        elif player_input == 1:
            self._player = self.cut_wood()
        elif player_input == 2:
            self._player = self.build_shelter()
        elif player_input == 3:
            self._player = self.build_boat()
        else:
            print("This is not a valid action\n")

        return loop_condition

    def build_boat(self ):
        if self._player.get_inventory().get_slots()['Wood'] >= 10:
            print("You have built a boat.\n")
            self._player.get_inventory().get_slots()['Boat'] += 1
            self._player.get_inventory().get_slots()['Wood'] -= 10
        else:
            print("You don't have enough wood.\n")

        return self._player

    def build_shelter(self):
        if self._player.get_inventory().get_slots()['Wood'] >= 5:
            print("You have built a Shelter.\n")
            self._player.get_inventory().get_slots()['Shelter'] += 1
            self._player.get_inventory().get_slots()['Wood'] -= 5
        else:
            print("You don't have enough wood.\n")

        return self._player

    def cut_wood(self):
        if self._player.get_inventory().is_slots_full():
            print("Your inventory is full!\n")
            print("You didn't pick up the wood.\n")
        else:
            # TODO Make wood working class give out wood
            if self.is_wood_gained():
                print("You got 1 piece of wood!\n")
                self._player.get_inventory().add_item('Wood', 1)
                self._player.get_strength().gain_exp()
                self._player.get_stamina().gain_exp()

            else:
                print("You failed to cut the tree.\n")
        return self._player

    def is_wood_gained(self):
        ran_num = randint(1, 10)
        if ran_num % self._percentage_to_cut == 0:
            return True
        else:
            return False
