from Agent import Agent


class Herbivor(Agent):
    def __init__(self,body):
        Agent.__init__(self)
        self.body = body

    def show(self):
        self.body.show(self.__class__.__name__)
