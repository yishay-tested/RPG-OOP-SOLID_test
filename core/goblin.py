import random as rand

import core.player as pl

class Goblin(pl.Monsters):
    def __init__(self):
        super().__init__()
        self.name = "Gob"
        self.type = "goblin"
        self.max_hp = 20
        self.hp = self.max_hp
        # self.speed = rand.randint(5,10)
        # self.power = rand.randint(5,10)
        self.armor_rating = 1

    def run_away(self):
        if self.hp < self.max_hp/2 and rand.random()<0.3:
            return "run away" # needs logic
            

    