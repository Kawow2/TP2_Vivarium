from Agent import Agent
from CarnivorBody import CarnivorBody
from Herbivor import Herbivor
from SuperPredBody import SuperPredBody
from Vegetal import Vegetal
from HerbivorBody import HerbivorBody
from DecomposorBody import DecomposorBody


class Decomposor(Agent):
    def __init__(self,args):
        Agent.__init__(self)
        self.body = DecomposorBody(args)

    def show(self):
        self.body.show(self.__class__.__name__)

    def filtrePerception(self):
        danger = []
        manger = []
        protect = []

        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if  not isinstance(i, Vegetal) and i.isDead :
                manger.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)
        protect.sort(key=lambda x: x.dist, reverse=False)

        return danger, manger, protect
