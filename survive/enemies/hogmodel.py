from survive.enemies.enemymodel import Enemy


class Hog(Enemy):
    def __init__(self):
        self._name = "Hog"
        self._health = 5
        self._level = 1
        self._attacks = {"Bite": 1}
        self._special_attacks = {"Ram": 2}

    def attack(self):
        pass
        # print("Uses")
        # return self.hog.attacks

    def get_basic_attack(self):
        return self._attacks["Bite"]

    def get_special_attack(self):
        return self._special_attacks["Ram"]
