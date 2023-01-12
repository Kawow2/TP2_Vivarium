import core as core
from Carnivor import Carnivor
from CarnivorBody import CarnivorBody
from Decomposor import Decomposor
from DecomposorBody import DecomposorBody
from Herbivor import Herbivor
from HerbivorBody import HerbivorBody
from SuperPred import SuperPred
from SuperPredBody import SuperPredBody


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("agents", [])
    core.memory("nbAgents", 10)
    core.memory("item", [])

    for i in range(core.memory("nbAgents")):
        core.memory("agents").append(Carnivor(CarnivorBody()))
        core.memory("agents").append(SuperPred(SuperPredBody()))
        core.memory("agents").append(Herbivor(HerbivorBody()))
        core.memory("agents").append(Decomposor(DecomposorBody()))


    print("Setup END-----------")


def computePerception(a):

    a.body.fustrum.perceptionList = []
    for b in core.memory('agents'):
        if a.uuid != b.uuid:
            if a.body.fustrum.inside(b.body):
                a.body.fustrum.perceptionList.append(b.body)



def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()

def run():
    core.cleanScreen()
    #Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("item"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

core.main(setup, run)


