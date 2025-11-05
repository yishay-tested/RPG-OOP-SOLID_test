import random as rand

import core.player as pl

class Orc(pl.Monsters):
    def __init__(self):
        super().__init__()
        self.name = "Bob"
        self.type = "orc"
        # self.max_hp = 50
        # self.hp = self.max_hp
        self.speed = rand.randint(0,5)
        self.power = rand.randint(10,15)
        self.armor_rating = rand.randint(2,8)
    
    def speak(self):
        print("I am " + self.type +" "+ self.name + ". And i'm ANGRY!")
        