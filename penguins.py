"""
Module for managing platforms.
"""
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
class Penguin(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    frames_r = []
    frames_l = []
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("img/pengu_spritesheet.png")
        # Grab the image for this platform
        frame_1 = sprite_sheet.get_image(0,0,72,64)
        self.frames_r.append(frame_1)
        frame_2 = sprite_sheet.get_image(72, 0, 72, 64)
        self.frames_r.append(frame_2)
        frame_3 = sprite_sheet.get_image(144, 0, 72, 64)
        self.frames_r.append(frame_3)
        frame_4 = sprite_sheet.get_image(216, 0, 72, 64)
        self.frames_r.append(frame_4)

        frame_5 = sprite_sheet.get_image(0, 0, 72, 64)
        frame_5 = pygame.transform.flip(frame_5, True, False)
        self.frames_l.append(frame_5)
        frame_6 = sprite_sheet.get_image(72, 0, 72, 64)
        frame_6 = pygame.transform.flip(frame_6, True, False)
        self.frames_l.append(frame_6)
        frame_7 = sprite_sheet.get_image(144, 0, 72, 64)
        frame_7 = pygame.transform.flip(frame_7, True, False)
        self.frames_l.append(frame_7)
        frame_8 = sprite_sheet.get_image(216, 0, 72, 64)
        frame_8 = pygame.transform.flip(frame_8, True, False)
        self.frames_l.append(frame_8)


        # self.image = pygame.transform.scale(self.image,(64,64))

        self.image = self.frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        self.index = 0

        self.counter = 0


class MovingPenguin(Penguin):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0
    direction = "Right"

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    player_hit = ""

    level = None
    player = None
    # max_pos_left = enemies[0][2]

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """
        # Move left/right
        self.rect.x += self.change_x

        pos = self.rect.x + self.level.world_shift

        self.counter += 1           # COUNTER FOR ENEMY SPRITE ANIMATION
        if self.counter == 10:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.frames_l) or self.index >= len(self.frames_r):
            self.index = 0
        cur_pos = self.rect.x - self.level.world_shift
        # if cur_pos < self.boundary_left:
        if self.direction == "Right":
            self.image = self.frames_l[self.index]
        if self.direction == "Left":
            self.image = self.frames_r[self.index]
        self.image = pygame.transform.scale(self.image,(64,64))

        # if self.change_x == -3:
        #     pygame.transform.flip(self.image, True, False)
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right
            # MovingPenguin.player_hit = True
            constants.pengu_sound.play()
            constants.score += 100
            # constants.health = constants.health - 10
            self.kill()

        # shot = pygame.sprite.collide_rect(self, self.bullet)
        # if shot:
        #     if self.change_x < 0:
        #         self.bullet.rect.right = self.rect.left
        #     else:
        #         self.bullet.rect.left = self.rect.right
        #     self.kill()






        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom


        # Check the boundaries and see if we need to reverse
        # direction.
        # if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
        #     self.change_y *= -1
        #     pygame.transform.flip(self.image, True, False)

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left:
            self.direction = "Right"
        if cur_pos > self.boundary_right:
            self.direction = "Left"
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
            self.image = pygame.transform.flip(self.image, True, False)
