from survive.controllers.controller import Controller

from survive.models.enemies.enemy import Enemy
from survive.models.enemies.hog import Hog


class EnemyController(Controller):
    def __init__(self):
        super().__init__()
        self._enemy = Enemy()

    def generate_enemy(self):
        self._enemy = Hog()
        return self._enemy
