from datetime import datetime

import core
from Body import Body
import random
from pygame import Vector2

from jauge import Jauge
from Herbivor import Herbivor


class HerbivorBody(Body):
    def __init__(self):
        Body.__init__(self)
        self.speed = Vector2(-1, 1)
        self.speedMax = 4
        self.maxAcc = 1
        self.hunger = Jauge(250, 1)
        self.sleep = Jauge(100, 0)
        self.reprod = Jauge(1000, 0)
        self.birth = datetime.now()
        self.lifeTime = 1000000

    def update(self):
        Body.update(self)
        # reprod
        if not self.isDead:
            self.reprod.value += self.reprod.step
            if self.reprod.value > self.reprod.max:
                self.reprod.value = self.reprod.min
                core.memory("agents").append(Herbivor(HerbivorBody()))

    def show(self, name):
        core.Draw.circle(self.colors[name], self.position, 10)
