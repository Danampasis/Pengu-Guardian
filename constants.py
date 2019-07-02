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
pains = ["sfx/pain1.wav","sfx/pain2.wav","sfx/pain3.wav","sfx/pain4.wav","sfx/pain5.wav","sfx/pain6.wav","sfx/painh.wav","sfx/paino.wav"]
jump_sound = pygame.mixer.Sound('sfx/jump.wav')
bad_sound = pygame.mixer.Sound('sfx/lose sound 2 - 1_0.ogg')
out_of_bullets = pygame.mixer.Sound('sfx/no ammo.wav')
click_sound = pygame.mixer.Sound('sfx/Shotgun.wav')
reload_sound = pygame.mixer.Sound('sfx/reload shotgun.wav')
death_sound = pygame.mixer.Sound('sfx/die1.wav')
heart_beat = pygame.mixer.Sound('sfx/heart beat.ogg')
# score_up = pygame.mixer.Sound('Picked Coin Echo 2.wav')
# select_sound = pygame.mixer.Sound('Menu Selection Click.wav')
pain_sound = pygame.mixer.Sound(random.choice(pains))
coin_sound = pygame.mixer.Sound('sfx/Coin.wav')
heart_sound = pygame.mixer.Sound('sfx/Replenish.wav')
start_sound = pygame.mixer.Sound('sfx/Start.wav')



# Music on or off
music = True

#Character selection
character_color = 'Blue' # TODO character color customisation
character = ""
if character_color == 'White':
    character = 'img/white_character.png'
elif character_color == 'Green':
    character = 'img/green_character.png'
elif character_color == 'Red':
    character = 'img/red_character.png'
elif character_color == 'Blue':
    character = 'img/blue_character.png'

health = 900

version = 'ALPHA_v0.1'

#Player Score

score = 0
coins = 0



