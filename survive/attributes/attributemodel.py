class Attribute(object):

    def __init__(self, level, name):
        self.name = name
        self.level = level
        self.exp_points = 0
        self.exp_to_next_level = 1

    def gain_exp(self):
        self.exp_points += 1
        self.level_up()

    def is_level_up(self):
        if(self.exp_points >= self.exp_to_next_level):
            return True
        else:
            return False

    def level_up(self):
        if(self.is_level_up()):
            print("Your " + self.name + " is now " + str(self.level) + "!\n")
            self.level += 1
            self.exp_points = 0
            self.exp_to_next_level = \
                (self.exp_to_next_level * 2)

        else:
            pass

    def get_exp_points(self):
        return self.exp_points

    def get_exp_to_next_level(self):
        return self.exp_to_next_level

    def get_level(self):
        return self.level
