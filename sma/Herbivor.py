from Agent import Agent
from Vegetal import Vegetal
from CarnivorBody import CarnivorBody
from SuperPredBody import SuperPredBody
from HerbivorBody import HerbivorBody


class Herbivor(Agent):
    def __init__(self,args):
        Agent.__init__(self)
        self.body = HerbivorBody(args)

    def show(self):
        self.body.show(self.__class__.__name__)


    def filtrePerception(self):
        danger = []
        manger = []
        protect = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, SuperPredBody) and not i.isDead:
                protect.append(i)
            if isinstance(i, Vegetal):
                manger.append(i)
            if isinstance(i, CarnivorBody) and not i.isDead:
                danger.append(i)


        danger.sort(key=lambda x: x.dist, reverse=False)
        manger.sort(key=lambda x: x.dist, reverse=False)
        protect.sort(key=lambda x: x.dist, reverse=False)

        return danger, manger, protect

