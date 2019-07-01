import pygame

from spritesheet_functions import SpriteSheet
import constants

WORM            = (0,0,128,128)

class Heart(pygame.sprite.Sprite):
    """ Platform the user can jump on """
    frames_h = []
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("img/heart_spritesheet.png")
        # Grab the image for this platform
        frame_1 = sprite_sheet.get_image(0, 0, 50, 50)
        self.frames_h.append(frame_1)
        frame_2 = sprite_sheet.get_image(50, 0, 50, 50)
        self.frames_h.append(frame_2)
        frame_3 = sprite_sheet.get_image(100, 0, 50, 50)
        self.frames_h.append(frame_3)
        frame_4 = sprite_sheet.get_image(150, 0, 50, 50)
        self.frames_h.append(frame_4)
        frame_5 = sprite_sheet.get_image(200, 0, 50, 50)
        self.frames_h.append(frame_5)
        frame_6 = sprite_sheet.get_image(250, 0, 50, 50)
        self.frames_h.append(frame_6)
        # self.image = pygame.transform.scale(self.image,(64,64)
        self.image = self.frames_h[0]
        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.index = 0
        self.counter = 0

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """
        # Move left/right
        # self.rect.x += self.change_
        # pos = self.rect.x + self.level.world_shif
        self.counter += 1  # COUNTER FOR ENEMY SPRITE ANIMATION
        if self.counter == 9:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.frames_h):
            self.index = 0
        # cur_pos = self.rect.x - self.level.world_shift
        # # if cur_pos < self.boundary_left:
        # if self.direction == "Right":
        self.image = self.frames_h[self.index]
        # if self.direction == "Left":
        #     self.image = self.frames_r[self.index]
        # self.image = pygame.transform.scale(self.image,(64,64)
        # if self.change_x == -3:
        #     pygame.transform.flip(self.image, True, False)
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            print("hit")
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else
            # If we are moving right, set our right side
            # to the left side of the item we hit
            # if self.change_x < 0:
            #     self.player.rect.right = self.rect.left
            # else:
            #     # Otherwise if we are moving left, do the opposite.
            #     self.player.rect.left = self.rect.right
            # constants.pain_sound.play()
            if constants.health < 900:
                constants.health = constants.health + 100
            constants.heart_sound.play()
            self.kill()
