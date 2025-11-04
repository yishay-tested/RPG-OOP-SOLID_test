import random as rand

class Alive_Entity:
    def __init__(self):
        self.name = "someone"
        self.max_hp = 50
        self.__hp = self.max_hp
        self.speed = rand.randint(5,10)
        self.__power = rand.randint(5,10)
        self.armor_rating = rand.randint(5,15)
    
    def speak(self):
        print("I am " + self.name + ".")
        
    def attack(self):
        pass
        


class Player(Alive_Entity):
    def __init__(self,name = "some"):
        super().__init__()
        self.name = name
        self.profession = rand.choice(['Warrior','Healer'])
        if self.profession == 'Healer':
            self._Alive_Entity__hp += 10
        if self.profession == 'Warrior':
            self._Alive_Entity__power += 2

        
class Monsters(Alive_Entity):
    def __init__(self):
        super().__init__()
        self.type = "Monster"
        self.weapon = rand.choice(['Sword','Knife','Axe'])
    
    def speak(self):
        print("I am " + self.type +" "+ self.name + ". And i'm ANGRY!")