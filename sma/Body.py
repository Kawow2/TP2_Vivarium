import datetime
import random
from pygame import Vector2
import core
from Fustrum import Fustrum
from jauge import Jauge


class Body:
    def __init__(self):
        self.fustrum = Fustrum(1000,self)
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.acceleration = Vector2(random.uniform(-2,2), random.uniform(-2,2))
        self.speed = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.speedMax = 15
        self.maxAcc = 15
        self.hunger = Jauge(100,0)
        self.sleep = Jauge(100,10)
        self.reprod = Jauge(100,5)
        self.birth = datetime.datetime.now()
        self.lifeTime = 1000
        self.isDead = False
        self.isSleeping = False
        self.colors = {
            'SuperPred': (71, 41, 230),
            'Carnivor': (255, 0, 0),
            'Decomposor': (128, 128, 128),
            'Herbivor': (255, 255, 0)
        }

    def move(self):
        if not self.isDead and not self.isSleeping:
            if self.acceleration.length() > self.maxAcc:
                self.acceleration.scale_to_length(self.maxAcc)
            self.speed += self.acceleration
            if self.speed.length() > self.speedMax:
                self.speed.scale_to_length(self.speedMax)
            self.position += self.speed
            self.acceleration = Vector2(0, 0)
            self.edge()

    def edge(self):
        if self.position.x <= self.maxAcc:
            self.speed.x *= -1
        if self.position.x + self.maxAcc >= core.WINDOW_SIZE[0]:
            self.speed.x *= -1
        if self.position.y <= self.maxAcc:
            self.speed.y *= -1
        if self.position.y + self.maxAcc >= core.WINDOW_SIZE[1]:
            self.speed.y *= -1

    def show(self,name):
        core.Draw.circle(self.colors[name], self.position, 10)

    def update(self):

        self.move()
        if (datetime.datetime.now() - self.birth).seconds > self.lifeTime:
            self.acceleration = Vector2(0,0)
            self.speed = Vector2(0,0)
            self.isDead = True


        #Faim
        if self.hunger.value > self.hunger.max:
            self.isDead = True

        self.hunger.value+=self.hunger.step

        #fatigue
        if not self.isSleeping:
            self.sleep.value += self.sleep.step

        if self.sleep.value>self.sleep.max:
            self.isSleeping = True

        if self.isSleeping:
            self.sleep.value -=self.sleep.step

        if self.sleep.value<self.sleep.min:
            self.isSleeping = False









