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

    for i in range(1):
        core.memory("agents").append(Carnivor(params["SuperPred"]["params"]))
        core.memory("agents").append(SuperPred(params["SuperPred"]["params"]))
        core.memory("agents").append(Herbivor(params["SuperPred"]["params"]))
        core.memory("agents").append(Decomposor(params["SuperPred"]["params"]))

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

def findRightAgent(agent):
    if (agent.__class__.__name__ is "SuperPred"):
        return SuperPred(agent.body)
    elif agent.__class__.__name__ is "Carnivor":
        return Carnivor(agent.body)
    elif agent.__class__.__name__ is "Herbivor":
        return Herbivor(agent.body)
    elif agent.__class__.__name__ is "Decomposor":
        return  Decomposor(agent.body)



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
                        core.memory("items").append(Vegetal(b.body.position))
                        a.body.hunger.addValue(-25)

        if a.body.reprod.value> a.body.reprod.max:
            agent = findRightAgent(a)
            core.memory("agents").append(agent)
            a.body.reprod.value = 0


    for a in core.memory("agents"):
        for c in core.memory('items'):
            if isinstance(a,Herbivor) :
                if a.body.position.distance_to(c.position) <= c.mass:
                    core.memory("items").remove(c)
                    a.body.hunger.addValue(-25)



core.main(setup, run)
