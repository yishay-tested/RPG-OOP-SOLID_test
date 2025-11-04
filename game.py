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
    
    def battle(self, player:player.Player, monster:player.Monsters):
        # first turn chioce
        print("battle start.")
        player_first_turn = player.speed + self.roll_dice(6)
        mon_first_turn =  monster.speed + self.roll_dice(6)
        if mon_first_turn > player_first_turn:
            attacker = monster
            defender = player
        else:
            attacker = player
            defender = monster
        print(attacker.name,"turn to attack.")

        # fight !
        while True:
            att_speed = attacker.speed + self.roll_dice(20)
            if att_speed > defender.armor_rating:
                damage = attacker.attack()
                defender.hp -= damage
                if defender.hp <= 0:
                    print(defender.name, "Died...")
                    return
            else:
                print(attacker.name, "missed the attack!", defender.name,"turn.")
            attacker,defender = defender,attacker



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

        

        if self.show_menu(): # to start the battle or Quit
            new_player = self.create_player()
            new_mon = self.choose_random_monster()

            new_player.speak()
            new_mon.speak()
           
            self.battle(new_player, new_mon)
        else:
            return
        