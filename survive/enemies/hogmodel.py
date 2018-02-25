from survive.enemies.enemymodel import Enemy


class Hog(Enemy):
    def __init__(self):
        self.name = "Hog"
        self.health = 5
        self.level = 1
        self.attacks = {"Bite": 1}
        self.special_attacks = {"Ram": 2}

    def attack(self):
        pass
        # print("Uses")
        # return self.hog.attacks

    def get_basic_attack(self):
        return self.attacks["Bite"]

    def get_special_attack(self):
        return self.special_attacks["Ram"]
