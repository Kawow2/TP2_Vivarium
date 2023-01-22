import random
from pygame import Vector2

import core
from Item import Item


class Vegetal(Item):
    def __init__(self,args):
        if len(args)>0:
            self.position = Vector2(args[0],args[1])
        else:
            self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.mass = 8
        self.color = (0, 86, 27)

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)
