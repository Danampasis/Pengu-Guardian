import pygame

import constants
import levels
from bullet import Bullet
import screens
import time
import numpy
from platforms import MovingPlatform

from player import Player
import enemylast


# font_name = pygame.font.match_font('arial')
font_name = 'Wonder_Boy_In_Monster_World.ttf'


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, constants.BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def game():
    """ Main Program """
    pygame.init()
    pygame.joystick.init()
    pygame.mixer.init()
    pygame.mouse.set_visible(False)

    try:
        j = pygame.joystick.Joystick(0)  # create a joystick instance
        j.init()  # init instance
        print("Enabled joystick: {0}".format(j.get_name()))
    except pygame.error:
        print("no joystick found.")

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Pengu Guardian")
    a = pygame.image.load('character_blue.png')
    pygame.display.set_icon(a)

    # Create the player
    player = Player()

    debug_fps = False

    # Create all the levels
    level_list = []
    # level_list.append(levels.Level_TEST(player))
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))
    level_list.append(levels.Level_04(player))
    level_list.append(levels.Level_04(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    bullet_list = pygame.sprite.Group()

    ammo_list = pygame.sprite.Group()

    magazine_limit = 5

    animation_list = pygame.sprite.Group()

    score = 0

    # font = pygame.font.Font('Wonder_Boy_In_Monster_World.ttf',30)

    if current_level.music_on == True:
        pygame.mixer.music.load(current_level.music)
        pygame.mixer.music.play(-1)

    current_position = 0


    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                print("Average fps for this session:",avg_fps)
                done = True # Flag that we are done so we exit this loop
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(5):
                    if current_level.weapons:
                        if len(ammo_list) < 6:
                            constants.click_sound.play()
                            bullet = Bullet()
                            # Set the bullet so it is where the player is
                            bullet.rect.x = player.rect.x
                            bullet.rect.y = player.rect.y + 30
                            # Add the bullet to the lists
                            active_sprite_list.add(bullet)
                            bullet_list.add(bullet)
                            ammo_list.add(bullet)
                        else:
                            constants.out_of_bullets.play()
                    else:
                        constants.out_of_bullets.play()
                if j.get_button(2):
                    player.jump()
                if j.get_button(4):
                    if magazine_limit >= 1:
                        if len(ammo_list) == 6:
                            ammo_list.empty()
                            constants.reload_sound.play()
                            magazine_limit = magazine_limit - 1
                    else:
                        constants.out_of_bullets.play()
                if j.get_button(9):
                    screens.ending()
                if j.get_button(8):
                    screens.help()
            if event.type == pygame.JOYAXISMOTION:
                value = j.get_axis(0)
                if round(value) >= 1:
                    player.go_right()
                if round(value) == 0:
                    player.stop()
                if round(value) == -1:
                    player.go_left()
            if event.type == pygame.KEYDOWN:
                keymod = pygame.key.get_mods()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_r:
                    if magazine_limit >= 1:
                        if len(ammo_list) == 6:
                            ammo_list.empty()
                            constants.reload_sound.play()
                            magazine_limit = magazine_limit - 1
                    # else:
                    #     constants.jump_sound.play() # TODO out of magazines sound(maybe)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_EQUALS and keymod == 1:
                    player.god()
                if event.key == pygame.K_1 and keymod == 1:  # Toggles fps print on console
                    if debug_fps == False:
                        debug_fps = True
                    else:
                        debug_fps = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.jump()
                    # jump_sound.play()
                if event.key == pygame.K_2:
                    player.go_in()
                if event.key == pygame.K_5:
                    constants.speed = 12
                if event.key == pygame.K_SPACE:
                    if current_level.weapons:
                        if len(ammo_list) < 6:
                            constants.click_sound.play()
                            bullet = Bullet()
                            # Set the bullet so it is where the player is
                            bullet.rect.x = player.rect.x
                            bullet.rect.y = player.rect.y + 30
                            # Add the bullet to the lists
                            active_sprite_list.add(bullet)
                            bullet_list.add(bullet)
                            ammo_list.add(bullet)
                        else:
                            constants.out_of_bullets.play()
                    else:
                        constants.out_of_bullets.play()
                #Debugging Button - Shows info on console
                if event.key == pygame.K_BACKQUOTE and keymod == 1:
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
                        print('Is player hit?: ', MovingPlatform.player_hit)
                        print('------------------------------------------------------')
                        numTimesToRepeat -= 1  # repeat one less time because we just did it
                        if numTimesToRepeat == 0:  # do we repeat again?
                            break
                        # time.sleep(60.0 - ((time.time() - starttime) % 60.0))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

        for bullet in bullet_list:
            if bullet.rect.x > player.rect.x+500 or bullet.rect.x < player.rect.x-500:
                bullet_list.remove(bullet)
                active_sprite_list.remove(bullet)
        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        current_position = player.rect.x + abs(current_level.world_shift)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            if current_position > 120:
                current_level.shift_world(diff)
            else:
                current_level.shift_world(-diff)
                constants.bad_sound.play()

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + abs(current_level.world_shift)
        if current_position > current_level.level_limit_right:
            screens.level_intro()
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                screens.current_level += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                # if current_level.music_on:
                #     pygame.mixer.music.load(current_level.music)
                #     pygame.mixer.music.play(-1)
            if current_level_no == len(level_list)-1:
                screens.ending()

        # Check level 0 position to enter customisation building

        # if current_level_no == 0:
        #     if current_position > 2900 and current_position < 3100:
        #         if event.key == pygame.K_f:
        #             screens.customise() # TODO Show Screen

        fps_list =  []
        fps = int(clock.get_fps())
        fps_list.append(fps)
        avg_fps = numpy.average(fps_list)
        if debug_fps == True:
            print(fps)

        if constants.health == 0:
            screens.death()
        if constants.health >= 900:
            img = pygame.image.load('full health.png')
        if constants.health < 600:
            img = pygame.image.load('middle health.png')
        if constants.health < 300:
            # pygame.mixer.music.stop()
            # constants.heart_beat.play(-1)  # TODO heartbeat sound when health is low
            img = pygame.image.load('low health.png')

        # SHOTGUN SHELL IMAGE
        if len(ammo_list) == 0:
            bullets = pygame.image.load('full ammo.png')
        if len(ammo_list) == 1:
            bullets = pygame.image.load('5 ammo.png')
        if len(ammo_list) == 2:
            bullets = pygame.image.load('4 ammo.png')
        if len(ammo_list) == 3:
            bullets = pygame.image.load('3 ammo.png')
        if len(ammo_list) == 4:
            bullets = pygame.image.load('2 ammo.png')
        if len(ammo_list) == 5:
            bullets = pygame.image.load('1 ammo.png')
        if len(ammo_list) == 6:
            bullets = pygame.image.load('reload.png')

        if magazine_limit > 0:
            if len(ammo_list) == 6:
                reload = 'Reload!' # TODO show reload when out bullets
            else:
                text = str(magazine_limit)+'x'
        if magazine_limit == 0:
            text = ''
            if len(ammo_list) == 6:
                bullets = pygame.image.load('out of ammo.png')
        for bullet in bullet_list:
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, levels.Level.enemy_list, True)
            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                active_sprite_list.remove(bullet)
                # constants.score_up.play()
                score += 1


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        # draw_text(screen, 'Magazines: ', 18, constants.SCREEN_WIDTH - 760, 5)
        # draw_text(screen, reload, 18, 50, 10)
        draw_text(screen,text, 18, 20, 10)
        draw_text(screen,'Score: '+str(score),18, 400, 10)
        draw_text(screen, constants.version, 10, 60, 585) # TODO remove before release
        screen.blit(bullets, (40, 5))
        screen.blit(img, (670, 5))

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


# if __name__ == "__main__":
screens.main_menu() # Displays Main Menu
# screens.level()
if screens.customise == True:
    screens.customisation()
else:
#screens.settings() # TODO Settings Screen
# screens.level1() # TODO implement level change screen
    game()
# re,mk Chelsea cat walked over the keyboard
