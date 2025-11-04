import random as rand

class Alive_Entity:
    def __init__(self):
        self.name = ""
        self.hp = 50
        self.speed = rand.randint(5,10)
        self.power = rand.randint(5,10)
        self.armor_rating = rand.randint(5,15)
    
    def speak(self):
        print("I am " + self.name + ".")
        
    def attack(self):
        pass
        


class Player(Alive_Entity):
    def __init__(self):
        Alive_Entity().__init__()
        self.profession = ""

        
class Monsters(Alive_Entity):
    def __init__(self):
        Alive_Entity().__init__()
       