import random as rand

class Game:
    def __init__(self):
        pass
    
    def show_menu(self):
        while True:
            in_choice = input("Choose (B)attle or (Q)uit: ").upper()
            if in_choice == 'B':
                self.battle("player", "monster")
                return
            elif in_choice == 'Q':
                return
            else:
                continue

    def choose_random_monster(self):
        pass

    def battle(self, player, monster):
        pass

    def roll_dice(self, sides):
        return rand.randint(1,sides)
    
    def start(self):
        self.show_menu()
