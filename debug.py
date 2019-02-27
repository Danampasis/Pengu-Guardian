import time
import player
from platform_scroller import Player,game

player = Player()
game = game()
def debug():

    starttime = time.time()
    numTimesToRepeat = 5
    while True:
        print('Player is facing:', Player.direction)
        print('Player x value is:', player.rect.x)
        print('Player y valus is:', player.rect.y)
        print('Weapons status:', current_level.weapons)
        print('Current level limit:', current_level.level_limit_right)
        print('Current level world shift:', current_level.world_shift)
        print('Number of Levels:',len(level_list))
        print('Current Level:',current_level_no)
        print('Current position is:',current_position)
        print('Current music is:',current_level.music)
        print('------------------------------------------------------')
        numTimesToRepeat -= 1  # repeat one less time because we just did it
        if numTimesToRepeat == 0:  # do we repeat again?
            break