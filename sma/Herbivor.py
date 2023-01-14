from Agent import Agent
from Vegetal import Vegetal
from CarnivorBody import CarnivorBody
from sma.SuperPredBody import SuperPredBody


class Herbivor(Agent):
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
            if isinstance(i, Vegetal):
                manger.append(i)
            if isinstance(i, CarnivorBody) and not i.isDead:
                danger.append(i)
            if isinstance(i, SuperPredBody) and not i.isDead:
                danger.append(i)

        danger.sort(key=lambda x: x.dist, reverse=False)
        manger.sort(key=lambda x: x.dist, reverse=False)

        return danger, manger


    # def update(self):
    #
    #     danger, manger = self.filtrePerception()
    #     if len(manger) > 0:
    #         target = manger[0].position - self.body.position
    #         target.scale_to_length(target.length())
    #         self.body.acceleration = self.body.acceleration + target
    #
    #     if len(danger) > 0:
    #         target = self.body.position - danger[0].position
    #         target.scale_to_length(1 / target.length() ** 2)
    #         target.scale_to_length(target.length() * (self.coefObs + self.body.mass))
    #         self.body.acceleration = self.body.acceleration + target
