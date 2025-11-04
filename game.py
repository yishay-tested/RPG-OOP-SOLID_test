import random as rand
from core import player, orc, goblin


class Game:
    def __init__(self):
        self.start()
    
    def create_player(self):
        return player.Player()

    def choose_random_monster(self):
        match rand.choice(["Orc","Goblin"]):
            case "Orc":
                return orc.Orc()
            case "Goblin":
                return goblin.Goblin()
    
    def battle(self, player, monster):
        pass

    def roll_dice(self, sides):
        return rand.randint(1,sides)


    def show_menu(self):
        while True:
            in_choice = input("Choose (B)attle or (Q)uit: ").upper()
            if in_choice == 'B':
                return True
            elif in_choice == 'Q':
                return False
            else:
                continue


    def start(self):

        new_player = self.create_player()
        new_mon = self.choose_random_monster()

        new_player.speak()
        new_mon.speak()

        if self.show_menu(): # to start the battle or Quit
            self.battle(new_player, new_mon)
        else:
            return
        