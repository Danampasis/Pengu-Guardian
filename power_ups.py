import pygame

from spritesheet_functions import SpriteSheet
import constants
# from levels import mobs
# import bullet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

WORM            = (0,0,128,128)


class Coin(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    frames_r = []
    frames_l = []

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("img/coin_spritesheet.png")
        # Grab the image for this platform
        frame_1 = sprite_sheet.get_image(0,0,50,50)
        self.frames_r.append(frame_1)
        frame_2 = sprite_sheet.get_image(50, 0, 50, 50)
        self.frames_r.append(frame_2)
        frame_3 = sprite_sheet.get_image(100, 0, 50, 50)
        self.frames_r.append(frame_3)
        frame_4 = sprite_sheet.get_image(150, 0, 50, 50)
        self.frames_r.append(frame_4)
        frame_5 = sprite_sheet.get_image(200, 0, 50, 50)
        self.frames_r.append(frame_5)
        frame_6 = sprite_sheet.get_image(250, 0, 50, 50)
        self.frames_r.append(frame_6)

        self.image = self.frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        self.index = 0

        self.counter = 0

    def update(self):
        self.counter += 1           # COUNTER FOR ENEMY SPRITE ANIMATION
        if self.counter == 9:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.frames_r):
            self.index = 0
        self.image = self.frames_r[self.index]

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            constants.coin_sound.play()
            constants.score += 10
            constants.coins += 1
            self.kill()