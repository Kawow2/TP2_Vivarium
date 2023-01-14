from Agent import Agent
from HerbivorBody import HerbivorBody
from SuperPredBody import SuperPredBody


class Carnivor(Agent):
    def __init__(self,body):
        Agent.__init__(self)
        self.body = body

    def show(self):
        self.body.show(self.__class__.__name__)

    def filtrePerception(self):
        danger = []
        manger = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, HerbivorBody):
                manger.append(i)
            if isinstance(i, SuperPredBody):
                danger.append(i)

        danger.sort(key=lambda x: x.dist, reverse=False)
        manger.sort(key=lambda x: x.dist, reverse=False)

        return danger, manger


