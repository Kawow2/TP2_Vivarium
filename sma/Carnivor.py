from Agent import Agent


class Carnivor(Agent):
    def __init__(self,body):
        Agent.__init__(self)
        self.body = body

    def show(self):
        self.body.show(self.__class__.__name__)

    # def filtrePerception(self):
    #     danger = []
    #     manger = []
    #     for i in self.body.fustrum.perceptionList:
    #         i.dist = self.body.position.distance_to(i.position)
    #         if isinstance(i, Herbivor):
    #             manger.append(i)
    #         if isinstance(i, SuperPred):
    #             danger.append(i)
    #
    #     danger.sort(key=lambda x: x.dist, reverse=False)
    #     manger.sort(key=lambda x: x.dist, reverse=False)
    #
    #     return danger, manger
    #
    #
    # def update(self):
    #     danger, manger = self.filtrePerception()
    #     print(manger)
    #
    #     if len(manger) > 0:
    #         target = manger[0].position - self.body.position
    #         target.scale_to_length(target.length() * self.coefCreep)
    #         self.body.acc = self.body.acc + target
    #
    #     if len(danger) > 0:
    #         target = self.body.position - danger[0].position
    #         target.scale_to_length(1 / target.length() ** 2)
    #         target.scale_to_length(target.length() * (self.coefObs + self.body.mass))
    #         self.body.acc = self.body.acc + target
