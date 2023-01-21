from datetime import datetime

import core
from Body import Body
import random
from pygame import Vector2

from jauge import Jauge
from Vegetal import Vegetal


class DecomposorBody(Body):
    def __init__(self,args):
        Body.__init__(self)
        # Si il vient d'une reproduction
        if isinstance(args, DecomposorBody):
            self.speed = Vector2(random.uniform(args.speed[0] - 5, args.speed[0] + 5),
                                 random.uniform(args.speed[1] - 5, args.speed[1] + 5))
            self.speedMax = random.uniform(args.speedMax - 2, args.speedMax + 2)
            self.maxAcc = random.uniform(args.maxAcc - 2, args.maxAcc + 2)
            self.hunger = Jauge(random.uniform(args.hunger.max - 5, args.hunger.max + 5), 1)
            self.sleep = Jauge(random.uniform(args.sleep.max - 5, args.sleep.max + 5), 1)
            self.reprod = Jauge(random.uniform(args.reprod.max - 5, args.reprod.max + 5), 1)
            self.lifeTime = random.uniform(args.lifeTime - 5, args.lifeTime + 5)
            self.acceleration = Vector2(random.uniform(args.acceleration[0] - 5, args.acceleration[0] + 5),
                                        random.uniform(args.acceleration[1] - 5, args.acceleration[1] + 5))
            self.position = Vector2(random.uniform((args.position[0] - 5) % core.WINDOW_SIZE[0],
                                                   (args.position[0] + 5) % core.WINDOW_SIZE[0]),
                                    random.uniform((args.position[1] - 5) % core.WINDOW_SIZE[1],
                                                   (args.position[1] + 5)) % core.WINDOW_SIZE[1])

        # si il est créer par le main
        elif len(args) > 0:
            self.speed = Vector2(random.uniform(args["speed"][0], args["speed"][1]),
                                 random.uniform(args["speed"][0], args["speed"][1]))
            self.speedMax = random.uniform(args["speedMax"][0], args["speedMax"][1])
            self.maxAcc = random.uniform(args["maxAcc"][0], args["maxAcc"][1])
            self.hunger = Jauge(random.uniform(args["hunger"][0], args["hunger"][1]), 1)
            self.sleep = Jauge(random.uniform(args["sleep"][0], args["sleep"][1]), 1)
            self.reprod = Jauge(random.uniform(args["reprod"][0], args["reprod"][1]), 1)
            self.lifeTime = args["lifetime"]
            self.acceleration = Vector2(random.uniform(args["acceleration"][0], args["acceleration"][1]),
                                        random.uniform(args["acceleration"][0], args["acceleration"][1]))
        self.birth = datetime.now()

    def update(self):
        Body.update(self)
        # reprod
        if not self.isDead:
            self.reprod.value += self.reprod.step
            # if self.reprod.value > self.reprod.max:
            #     self.reprod.value = self.reprod.min
                # core.memory("agents").append(Decomposor(DecomposorBody()))
            # self.developVegetal.value+=self.reprod.step
            # if self.developVegetal.value>self.developVegetal.max:
            #     self.developVegetal.addValue(-self.developVegetal.max)
            #     core.memory("items").append(Vegetal())


    def show(self, name):
        core.Draw.circle(self.colors[name], self.position, 10)
