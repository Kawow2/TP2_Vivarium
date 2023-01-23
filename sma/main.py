import datetime
import threading

import core as core
from Carnivor import Carnivor
from Decomposor import Decomposor
from Herbivor import Herbivor
from SuperPred import SuperPred
from Vegetal import Vegetal
import json
import matplotlib.pyplot as plt

def setup():
    data = load('scenario.json')
    params = data["params"]
    core.fps = 30
    core.start = datetime.datetime.now()
    core.graph = data["graph"]
    core.WINDOW_SIZE = [600, 600]
    core.duration = data["simDuration"]

    core.memory("agents", [])
    core.memory("nbAgents", 2)
    core.memory("items", [])

    for i in range(params["Carnivor"]["nb"]):
        core.memory("agents").append(Carnivor(params["Carnivor"]["params"]))

    for i in range(params["SuperPred"]["nb"]):
        core.memory("agents").append(SuperPred(params["SuperPred"]["params"]))

    for i in range(params["Herbivor"]["nb"]):
        core.memory("agents").append(Herbivor(params["Herbivor"]["params"]))

    for i in range(params["Decomposor"]["nb"]):
        core.memory("agents").append(Decomposor(params["Decomposor"]["params"]))

    for i in range(params["Vegetaux"]["nb"]):
        core.memory("items").append(Vegetal([]))

    if core.graph:
        thr = threading.Thread(target=displayGraph,args=())
        thr.start()

    print("Setup END-----------")


def load(path):
    file = open(path)
    data = json.load(file)
    return data


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


def printPercentage(list):
    for i in range(0,len(list)-1):
        pop = list[i]
        print( pop["name"] , ": ", pop["nb"] ,"individus -->", round(pop["nb"]/list[4]["nb"]*100) , "% de la pop totale")



def displayPercentage():
    agents = core.memory("agents")
    list = [{"name":"SuperPred","nb": 0}, {"name":"Carnivor","nb": 0}, {"name":"Herbivor","nb": 0}, {"name":"Decomposor","nb": 0}, {"name":"Total","nb": 0}]
    for agent in agents:
        if not agent.body.isDead:
            if agent.__class__.__name__ == "SuperPred":
                list[0]["nb"] += 1
            elif agent.__class__.__name__ == "Carnivor":
                list[1]["nb"] += 1
            elif agent.__class__.__name__ == "Herbivor":
                list[2]["nb"] += 1
            elif agent.__class__.__name__ == "Decomposor":
                list[3]["nb"] += 1
            list[4]["nb"] += 1

    printPercentage(list)


def printBestAgent(agent):
    print("Le meilleur agent est un ",agent.__class__.__name__, ".")
    print("Temps de vie : ",round(agent.body.lifetime))
    print("Faim : ",round(agent.body.hunger.max))
    print("Sommeil : ",round(agent.body.sleep.max))
    print("Reproduction : ",round(agent.body.reprod.max))
    print("Vitesse Max : ",round(pow(agent.body.speedMax,2)))
    print("Vitesse : ",round(abs(agent.body.speed[0]) * abs(agent.body.speed[1])))




def displayBestAgent():
    value = 0
    choosenOne = None
    for agent in core.memory("agents"):
        body = agent.body        
        agentValue = body.reprod.max + body.sleep.max + body.hunger.max + body.lifetime * 10 + body.maxAcc * 5 + body.speedMax * 5 + (abs(body.speed[0]) + abs(body.speed[1]) * 5) + (abs(body.acceleration[0]) + abs(body.acceleration[1]) * 5)
        if body.isDead:
            agentValue*=-1
        if value<agentValue:
            value = agentValue
            choosenOne = agent
    
    printBestAgent(choosenOne)



def run():
    core.cleanScreen()

    leftClick = core.getMouseLeftClick()
    if leftClick is not None:
        displayPercentage()

    rightClick = core.getMouseRightClick()
    if rightClick is not None:
        displayBestAgent()
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
def displayGraph():
    while True:
        plt.cla()
        data = {'Herbivor': 0, 'Carnivor': 0, 'SuperPred': 0, 'Decomposor': 0}
        for agent in core.memory("agents"):
            data[agent.__class__.__name__] += 1
        plt.cla()  # Clear axis
        labels = list(data.keys())
        values = list(data.values())
        plt.ylabel("Nombre d'individus")

        plt.title("Nombre d'individus en fonction de l'espèce")
        plt.bar(labels,values,color=['yellow', 'red', 'blue', 'grey'])
        plt.draw()
        plt.show()
        plt.pause(0.001)

def findRightAgent(agent):
    if agent.__class__.__name__ == "SuperPred":
        return SuperPred(agent.body)
    elif agent.__class__.__name__ == "Carnivor":
        return Carnivor(agent.body)
    elif agent.__class__.__name__ == "Herbivor":
        return Herbivor(agent.body)
    elif agent.__class__.__name__ == "Decomposor":
        return Decomposor(agent.body)


def updateEnv():
    for a in core.memory("agents"):
        for b in core.memory('agents'):
            if b.uuid != a.uuid:
                if a.body.position.distance_to(b.body.position) <= b.body.mass:
                    # carnivor eats herbivor
                    if isinstance(a, Carnivor) and isinstance(b, Herbivor) and not a.body.isDead:
                        core.memory("agents").remove(b)
                        a.body.hunger.addValue(-25)
                        # superpred eats carnivor
                    elif isinstance(a, SuperPred) and isinstance(b, Carnivor) and not a.body.isDead:
                        core.memory("agents").remove(b)
                        b.body.hunger.addValue(-25)
                        # decomposor eats dead carnivor or superpred or herbivor
                    elif isinstance(a, Decomposor) and b.body.isDead and (
                            isinstance(b, Carnivor) or isinstance(b, SuperPred) or isinstance(b, Herbivor) or isinstance(b, Decomposor)):
                        core.memory("agents").remove(b)
                        core.memory("items").append(Vegetal(b.body.position))
                        a.body.hunger.addValue(-25)

        if a.body.reprod.value > a.body.reprod.max:
            agent = findRightAgent(a)
            core.memory("agents").append(agent)
            a.body.reprod.value = 0

    for a in core.memory("agents"):
        for c in core.memory('items'):
            if isinstance(a, Herbivor):
                if a.body.position.distance_to(c.position) <= c.mass:
                    core.memory("items").remove(c)
                    a.body.hunger.addValue(-25)


core.main(setup, run)