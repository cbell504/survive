class Attribute(object):
    def __init__(self, level, name):
        self._name = name
        self._level = level
        self._exp_points = 0
        self._exp_to_next_level = 1

    def gain_exp(self):
        self._exp_points += 1
        self.level_up()

    def is_level_up(self):
        if(self._exp_points >= self._exp_to_next_level):
            return True
        else:
            return False

    def level_up(self):
        if(self.is_level_up()):
            print("Your " + self._name + " is now " + str(self._level) + "!\n")
            self._level += 1
            self._exp_points = 0
            self._exp_to_next_level = \
                (self._exp_to_next_level * 2)

        else:
            pass

    def get_exp_points(self):
        return self._exp_points

    def get_exp_to_next_level(self):
        return self._exp_to_next_level

    def get_level(self):
        return self._level
