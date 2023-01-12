from datetime import datetime
from random import random

import core
from Body import Body
from pygame import Vector2
from jauge import Jauge



class SuperPredBody(Body):
    def __init__(self):
        super().__init__()
        self.speed = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.speedMax = 4
        self.maxAcc = 1
        self.hunger = Jauge(100, 1)
        self.sleep = Jauge(100, 2)
        self.reprod = Jauge(200, 1)
        self.birth = datetime.now()
        self.lifeTime = 2


    # def update(self):
    #     Body.update(self)
    #     # reprod
    #     if not self.isDead:
    #         self.reprod.value += self.reprod.step
    #         if self.reprod.value > self.reprod.max:
    #             self.reprod.value = self.reprod.min
    #             core.memory("agents").append(SuperPred(SuperPredBody()))
    #             print("new agent")

    def show(self, name):
        core.Draw.circle(self.colors[name], self.position, 10)
