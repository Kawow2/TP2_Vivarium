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
from Params import Params


def setup():
    print("Setup START---------")

    params = (Params().load())["params"]
    core.fps = 30
    core.WINDOW_SIZE = [600, 600]

    core.memory("agents", [])
    core.memory("nbAgents", 2)
    core.memory("items", [])

    for i in range(params["SuperPred"]["nb"]):
        core.memory("agents").append(SuperPred(SuperPredBody(params["SuperPred"]["params"])))

    # for i in range(params["Carnivor"]["nb"]):
    #     core.memory("agents").append(Carnivor(params["Carnivor"]["params"]))
    #
    # for i in range(params["SuperPred"]["nb"]):
    #     # core.memory("agents").append(Herbivor(HerbivorBody()))
    #
    # for i in range(params["SuperPred"]["nb"]):
    #     # core.memory("items").append(Vegetal())
    #
    # for i in range(params["SuperPred"]["nb"]):
    #     # core.memory("agents").append(Decomposor(DecomposorBody()))

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
    newAgent = agent.body.update()
    if newAgent is not None:
        core.memory("agents").append(Carnivor(agent))

def CreateAgent(classAgent):
    core.memory("agents").append(Carnivor())



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
                    #carnivor eats herbivor
                    if isinstance(a, Carnivor) and isinstance(b, Herbivor) and not a.body.isDead:
                        core.memory("agents").remove(b)
                        a.body.hunger.addValue(-25)
                        #superpred eats carnivor
                    elif isinstance(a, SuperPred) and isinstance(b, Carnivor) and not a.body.isDead:
                        core.memory("agents").remove(b)
                        b.body.hunger.addValue(-25)
                        #decomposor eats dead carnivor or superpred or herbivor
                    elif isinstance(a, Decomposor) and b.body.isDead and (isinstance(b, Carnivor) or  isinstance(b, SuperPred) or isinstance(b, Herbivor)):
                        core.memory("agents").remove(b)
                        a.body.hunger.addValue(-25)


    for a in core.memory("agents"):
        for c in core.memory('items'):
            if isinstance(a,Herbivor) or isinstance(a, Decomposor):
                if a.body.position.distance_to(c.position) <= c.mass:
                    core.memory("items").remove(c)
                    core.memory("items").append(Vegetal())
                    a.body.hunger.addValue(-25)



core.main(setup, run)
