import pygame

from spritesheet_functions import SpriteSheet
import constants

WORM            = (0,0,128,128)


class Heart(pygame.sprite.Sprite):
    frames_h = []

    def __init__(self, sprite_sheet_data):
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
        self.counter += 1  # COUNTER FOR ENEMY SPRITE ANIMATION
        if self.counter == 9:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.frames_h):
            self.index = 0
        self.image = self.frames_h[self.index]

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if constants.health < 900:
                constants.health = constants.health + 300
                constants.heart_sound.play()
            self.kill()
