import random

from Body import Body


class Agent(object):
    def __init__(self):
        self.body = Body()
        self.uuid = random.randint(100000,999999999)
        self.hungerMax = 100
        self.currentHunger = 50

    def show(self):
        self.body.show(self.__class__.__name__)


    def update(self):
        self.filtrePerception()
        self.body.move()

    def filtrePerception(self):
        pass



