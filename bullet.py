import pygame
from player import Player
from constants import *


class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # self.image = pygame.Surface([4, 10])
        # self.image.fill(BLACK)
        self.image = pygame.image.load('img/Bullet_12x3.png')

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the bullet. """
        if Player.direction == "R":
            self.rect.x -= -80
            # print(Player.direction)
        if Player.direction == "L":
            self.rect.x -= +80
