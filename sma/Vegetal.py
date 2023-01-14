import random
from pygame import Vector2

import core


class Vegetal(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.mass = 5
        self.color = (0, 86, 27)

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)
