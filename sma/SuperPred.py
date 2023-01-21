from Agent import Agent
from CarnivorBody import CarnivorBody
from SuperPredBody import SuperPredBody


class SuperPred(Agent):
    def __init__(self,args):
        Agent.__init__(self)
        self.body = SuperPredBody(args)

    def show(self):
        self.body.show(self.__class__.__name__)

    def filtrePerception(self):
        danger = []
        manger = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, CarnivorBody) and not i.isDead:
                manger.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)

        return danger, manger, []
