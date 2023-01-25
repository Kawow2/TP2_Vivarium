import random

from Body import Body


class Agent(object):
    def __init__(self):
        self.body = Body()
        self.uuid = random.randint(100000, 999999999)
        self.coefObs = 500

    def show(self):
        self.body.show(self.__class__.__name__)

    def update(self):
        self.filtrePerception()
        self.body.move()

    def update(self):
        danger, manger, protect = self.filtrePerception()
        if len(manger) > 0:
            target = manger[0].position - self.body.position
            target.scale_to_length(target.length())
            self.body.acceleration = self.body.acceleration + target

        if len(danger) > 0:
            if len(protect)==0:
                target = self.body.position - danger[0].position
                target.scale_to_length(1 / target.length() ** 2)
                target.scale_to_length(target.length() * self.coefObs)
                self.body.acceleration = self.body.acceleration + target
            if len(protect) > 0:
                # il faudrait check si le danger est pas entre l'agent et le protect
                target = protect[0].position - self.body.position
                target.scale_to_length(target.length())
                self.body.acceleration = self.body.acceleration + target
