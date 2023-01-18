from datetime import datetime

import core
from Body import Body
import random
from pygame import Vector2

from Decomposor import Decomposor
from jauge import Jauge
from Vegetal import Vegetal


class DecomposorBody(Body):
    def __init__(self):
        Body.__init__(self)

        self.speed = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.speedMax = 4
        self.maxAcc = 1
        self.hunger = Jauge(100, 0)
        self.sleep = Jauge(100, 0)
        self.reprod = Jauge(500, 1)
        self.birth = datetime.now()
        self.lifeTime = 200
        self.developVegetal = Jauge(100,5)

    def update(self):
        Body.update(self)
        # reprod
        if not self.isDead:
            self.reprod.value += self.reprod.step
            if self.reprod.value > self.reprod.max:
                self.reprod.value = self.reprod.min
                core.memory("agents").append(Decomposor(DecomposorBody()))
            # self.developVegetal.value+=self.reprod.step
            # if self.developVegetal.value>self.developVegetal.max:
            #     self.developVegetal.addValue(-self.developVegetal.max)
            #     core.memory("items").append(Vegetal())


    def show(self, name):
        core.Draw.circle(self.colors[name], self.position, 10)
