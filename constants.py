"""
Global constants
"""

import pygame
import random

pygame.mixer.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 128)

speed = 7

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Sounds
effects = True
pains = ["pain1.wav","pain2.wav","pain3.wav","pain4.wav","pain5.wav","pain6.wav","painh.wav","paino.wav"]
jump_sound = pygame.mixer.Sound('jump.wav')
bad_sound = pygame.mixer.Sound('lose sound 2 - 1_0.ogg')
out_of_bullets = pygame.mixer.Sound('no ammo.wav')
click_sound = pygame.mixer.Sound('Shotgun.wav')
reload_sound = pygame.mixer.Sound('reload shotgun.wav')
death_sound = pygame.mixer.Sound('die1.wav')
heart_beat = pygame.mixer.Sound('heart beat.ogg')
# score_up = pygame.mixer.Sound('Picked Coin Echo 2.wav')
# select_sound = pygame.mixer.Sound('Menu Selection Click.wav')
pain_sound = pygame.mixer.Sound(random.choice(pains))



# Music on or off
music = True

#Character selection
character_color = 'Blue' # TODO character color customisation
character = ""
if character_color == 'White':
    character = 'white_character.png'
elif character_color == 'Green':
    character = 'green_character.png'
elif character_color == 'Red':
    character = 'red_character.png'
elif character_color == 'Blue':
    character = 'blue_character.png'

health = 900

version = 'ALPHA_v0.1'



