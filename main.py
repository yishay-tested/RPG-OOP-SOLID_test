import game
from core import player, orc, goblin

my_player = player.Player()

game.Game().start()

my_player.speak()
# print(dir(my_player))
# print(my_player.__dict__.items())
print(vars(my_player))


MY_orc = orc.Orc()

MY_orc.speak()
print(vars(MY_orc))
