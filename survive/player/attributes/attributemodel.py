class Attribute(object):

    def __init__(self):
        self.attribute_level = 1
        self.attribute_exp_points = 0
        self.attribute_exp_to_next_level = 5

    def gain_exp(self):
        self.attribute_exp_points += 1
        self.level_up()

    def is_level_up(self):
        if(self.attribute_exp_points >= self.attribute_exp_to_next_level):
            return True
        else:
            return False

    def level_up(self):
        if(self.is_level_up()):
            print("You have leveled up!\n")
            self.attribute_level += 1
            self.attribute_exp_points = 0
            self.attribute_exp_to_next_level = \
                (self.attribute_exp_to_next_level * 2)

        else:
            pass
