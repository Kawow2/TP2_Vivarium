
import core
from Body import Body
import random
from pygame import Vector2
from jauge import Jauge
import datetime

from SuperPred import SuperPred


class SuperPredBody(Body):
    def __init__(self,args):
        Body.__init__(self)
        if len(args)>0:
            self.speed = Vector2(random.uniform(args["speed"][0], args["speed"][1]), random.uniform(args["speed"][0], args["speed"][1]))
            self.speedMax = random.uniform(args["speedMax"][0], args["speedMax"][1])
            self.maxAcc = random.uniform(args["maxAcc"][0], args["maxAcc"][1])
            self.hunger = Jauge(random.uniform(args["hunger"][0], args["hunger"][1]),1)
            self.sleep = Jauge(random.uniform(args["sleep"][0], args["sleep"][1]),1)
            self.reprod = Jauge(random.uniform(args["reprod"][0], args["reprod"][1]),1)
            self.lifeTime = args["lifetime"]
            self.acceleration = Vector2(random.uniform(args["acceleration"][0], args["acceleration"][1]), random.uniform(args["acceleration"][0], args["acceleration"][1]))




        self.birth = datetime.datetime.now()

    def update(self):
        Body.update(self)
        # reprod
        if not self.isDead:
            self.reprod.value += self.reprod.step
            if self.reprod.value > self.reprod.max:
                self.reprod.value = self.reprod.min
                core.memory("agents").append(self.createAgentFromSelf())

    def createAgentFromSelf(self):
        body = SuperPredBody([])
        body.lifeTime = random.randint(self.lifeTime - 2, self.lifeTime + 2)
        body.speedMax = random.randint(self.lifeTime - 2, self.lifeTime + 2)
        body.speed = Vector2(random.randint(round(self.speed[0] - 10), round(self.speed[0] + 10)),
                    random.randint(round(self.speed[1] - 10), round(self.speed[1] + 10)))
        body.acceleration = Vector2(random.randint(round(self.acceleration[0] - 10), round(self.acceleration[0] + 10)),
                    random.randint(round(self.acceleration[1] - 10), round(self.acceleration[1] + 10)))
        body.sleep = Jauge(random.randint(round(self.sleep.max - 10), round(self.sleep.max + 10)),self.sleep.step)
        body.hunger = Jauge(random.randint(round(self.hunger.max - 10), round(self.hunger.max + 10)),self.hunger.step)
        body.reprod = Jauge(random.randint(round(self.reprod.max - 10), round(self.reprod.max + 10)),self.reprod.step)

        return SuperPred(body)


    def show(self,name):
        core.Draw.circle(self.colors[name], self.position, 10)
