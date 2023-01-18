import core
from Body import Body
import random
from pygame import Vector2
from jauge import Jauge
import datetime

from sma.Fustrum import Fustrum


class CarnivorBody(Body):
    def __init__(self, *args):
        Body.__init__(self)
        if len(args) == 0:
            self.speed = Vector2(15, 15)
            self.lifeTime = 10000
        else:
            # seul le lifetime et la speed change aléatoirement pour les enfats pour l'instant
            self.lifeTime = args[0]
            self.speed = args[1]
            self.position = args[2]
        self.speedMax = 4
        self.maxAcc = 1
        self.hunger = Jauge(500, 0)
        self.sleep = Jauge(100000, 0)
        self.reprod = Jauge(500, 1)
        self.birth = datetime.datetime.now()
        self.fustrum = Fustrum(500,self)

    def update(self):
        Body.update(self)
        # reprod
        if not self.isDead:
            self.reprod.value += self.reprod.step
            if self.reprod.value > self.reprod.max:
                self.reprod.value = self.reprod.min
                from sma.Carnivor import Carnivor
                core.memory("agents").append(
                    Carnivor(CarnivorBody(
                        random.randint(self.lifeTime - 2, self.lifeTime + 2),
                        Vector2(random.randint(round(self.speed[0] + 10), round(self.speed[0] + 15)),
                                random.randint(round(self.speed[1] + 10), round(self.speed[1] + 15))),

                        Vector2(random.randint(round(self.position[0] - 5), round(self.position[0] + 5)),
                                random.randint(round(self.position[1] - 5), round(self.position[1] + 5))))))




    def show(self, name):
        core.Draw.circle(self.colors[name], self.position, 10)
