"""
Module for managing platforms.
"""
import pygame

from spritesheet_functions import SpriteSheet
import constants
# import bullet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

WORM            = (128,0,128,128)

class Item(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("worm_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.image = pygame.transform.scale(self.image,(64,64))

        self.rect = self.image.get_rect()

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            constants.health = constants.health + 300