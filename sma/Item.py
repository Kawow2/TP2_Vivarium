from random import random

from pygame import Vector2

import core


class Item(object):
    def __int__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.mass = 1
        self.color = (100, 100, 100)