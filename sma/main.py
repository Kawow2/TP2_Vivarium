import core as core
from Carnivor import Carnivor
from CarnivorBody import CarnivorBody
from Decomposor import Decomposor
from DecomposorBody import DecomposorBody
from Herbivor import Herbivor
from HerbivorBody import HerbivorBody
from SuperPred import SuperPred
from SuperPredBody import SuperPredBody
from Vegetal import Vegetal


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("agents", [])
    core.memory("nbAgents", 10)
    core.memory("items", [])

    for i in range(core.memory("nbAgents")):
        core.memory("agents").append(SuperPred(SuperPredBody()))
        core.memory("agents").append(Carnivor(CarnivorBody()))
        core.memory("agents").append(Herbivor(HerbivorBody()))
        core.memory("items").append(Vegetal())
        # core.memory("agents").append(Decomposor(DecomposorBody()))

    print("Setup END-----------")


def computePerception(a):
    a.body.fustrum.perceptionList = []
    for b in core.memory('agents'):
        if a.uuid != b.uuid:
            if a.body.fustrum.inside(b.body):
                a.body.fustrum.perceptionList.append(b.body)
    for c in core.memory("items"):
        if a.body.fustrum.inside(c):
            a.body.fustrum.perceptionList.append(c)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()


def run():
    core.cleanScreen()
    # Display
    for agent in core.memory("agents"):
        agent.show()

    for item in core.memory("items"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    updateEnv()


def updateEnv():
    for a in core.memory("agents"):
        for b in core.memory('agents'):
            if b.uuid != a.uuid:
                if a.body.position.distance_to(b.body.position) <= 10:
                    if isinstance(a, Carnivor) and isinstance(b, Herbivor) :
                        core.memory("agents").remove(b)
                        a.body.hunger.addValue(-25)
                    elif isinstance(a, SuperPred) and isinstance(b, Carnivor):
                        core.memory("agents").remove(b)
                        b.body.hunger.addValue(-25)
                    # elif isinstance(b, Carnivor) and isinstance(a, Herbivor):
                    #     core.memory("agents").remove(a)
                    #     b.body.hunger.addValue(-25)
                    #     print(b.body.hunger.value)
    for a in core.memory("agents"):
        for c in core.memory('items'):
            if isinstance(a,Herbivor):
                if a.body.position.distance_to(c.position) <= c.mass:
                    core.memory("items").remove(c)
                    core.memory("items").append(Vegetal())
                    a.body.hunger.addValue(-25)


core.main(setup, run)
