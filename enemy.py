"""
This module is used to hold the Enemy class. The Enemy represents the user-
controlled sprite on the screen.
"""
import pygame
#
# import constants
#
# from platforms import MovingPlatform
# from spritesheet_functions import SpriteSheet
# from enemies import MovingEnemy
#
# class Enemy(pygame.sprite.Sprite):
#     """ This class represents the bar at the bottom that the enemy
#     controls. """
#
#     # -- Attributes
#     # Set speed vector of enemy
#     change_x = 0
#     change_y = 0
#
#     # This holds all the images for the animated walk left/right
#     # of our enemy
#     walking_frames_l = []
#     walking_frames_r = []
#     walking_frames_t = []
#     hit_frames = []
#
#     # What direction is the enemy facing?
#     direction = "L"
#
#     # List of sprites we can bump against
#     level = None
#
#     enemy_hit = MovingPlatform.enemy_hit
#
#     stopped = None
#
#     # -- Methods
#     def __init__(self):
#         """ Constructor function """
#
#         # Call the parent's constructor
#         pygame.sprite.Sprite.__init__(self)
#
#         sprite_sheet = SpriteSheet(constants.character)
#         # Load all the right facing images into a list
#         width = 64
#         height = 64
#         walk_1 = sprite_sheet.get_image(0, 0, 465, 442)
#         walk_1 = pygame.transform.scale(walk_1, (width, height))
#         self.walking_frames_r.append(walk_1)
#         walk_2 = sprite_sheet.get_image(465, 0, 465, 442)
#         walk_2 = pygame.transform.scale(walk_2, (width, height))
#         self.walking_frames_r.append(walk_2)
#         walk_3 = sprite_sheet.get_image(930, 0, 465, 442)
#         walk_3 = pygame.transform.scale(walk_3, (width, height))
#         self.walking_frames_r.append(walk_3)
#         walk_4 = sprite_sheet.get_image(1395, 0, 465, 442)
#         walk_4 = pygame.transform.scale(walk_4, (width, height))
#         self.walking_frames_r.append(walk_4)
#         walk_5 = sprite_sheet.get_image(1860, 0, 465, 442)
#         walk_5 = pygame.transform.scale(walk_5, (width, height))
#         self.walking_frames_r.append(walk_5)
#         walk_6 = sprite_sheet.get_image(2325, 0, 465, 442)
#         walk_6 = pygame.transform.scale(walk_6, (width, height))
#         self.walking_frames_r.append(walk_6)
#         walk_7 = sprite_sheet.get_image(2790, 0, 465, 442)
#         walk_7 = pygame.transform.scale(walk_7, (width, height))
#         self.walking_frames_r.append(walk_7)
#         walk_8 = sprite_sheet.get_image(3255, 0, 465, 442)
#         walk_8 = pygame.transform.scale(walk_8, (width, height))
#         self.walking_frames_r.append(walk_8)
#         walk_9 = sprite_sheet.get_image(3720, 0, 465, 442)
#         walk_9 = pygame.transform.scale(walk_9, (width, height))
#         self.walking_frames_r.append(walk_9)
#
#         hit_1 = sprite_sheet.get_image(3720, 0, 465, 442)
#         hit_1 = pygame.transform.scale(hit_1, (width, height))
#         self.hit_frames.append(hit_1)
#
#         # flip right facing images
#         # image = pygame.image.load('character_blue.png')
#         # image = pygame.transform.scale(image, (width, height))
#         walk_1l = pygame.transform.flip(walk_1, True, False)
#         self.walking_frames_l.append(walk_1l)
#         # image = pygame.image.load('character_blue2.png')
#         # image = pygame.transform.scale(image, (width, height))
#         walk_2l = pygame.transform.flip(walk_2, True, False)
#         self.walking_frames_l.append(walk_2l)
#         walk_3l = pygame.transform.flip(walk_3, True, False)
#         self.walking_frames_l.append(walk_3l)
#         walk_4l = pygame.transform.flip(walk_4, True, False)
#         self.walking_frames_l.append(walk_4l)
#         walk_5l = pygame.transform.flip(walk_5, True, False)
#         self.walking_frames_l.append(walk_5l)
#         walk_6l = pygame.transform.flip(walk_6, True, False)
#         self.walking_frames_l.append(walk_6l)
#         walk_7l = pygame.transform.flip(walk_7, True, False)
#         self.walking_frames_l.append(walk_7l)
#         walk_8l = pygame.transform.flip(walk_8, True, False)
#         self.walking_frames_l.append(walk_8l)
#         walk_9l = pygame.transform.flip(walk_9, True, False)
#         self.walking_frames_l.append(walk_9l)
#
#
#         # Set the image the enemy starts with
#         self.image = self.walking_frames_r[0]
#
#         # Set a reference to the image rect.
#         self.rect = self.image.get_rect()
#
#     def update(self):
#         """ Move the enemy. """
#         # Gravity
#         self.calc_grav()
#
#         # Move left/right
#         self.rect.x += self.change_x
#         pos = self.rect.x + self.level.world_shift
#         if Enemy.direction == "R" and Enemy.enemy_hit != True:
#             frame = (pos // 30) % len(self.walking_frames_r)
#             self.image = self.walking_frames_r[frame]
#             # print(self.direction)
#         if Enemy.direction == "L":
#             frame = (pos // 30) % len(self.walking_frames_l)
#             self.image = self.walking_frames_l[frame]
#         if Enemy.direction == "T":
#             frame = (pos // 30) % len(self.walking_frames_t)
#             self.image = self.walking_frames_t[frame]
#
#         if Enemy.direction == "R" and Enemy.enemy_hit == True:
#             # frame = (pos // 30) % len(self.walking_frames_r)
#             self.image = self.hit_frames[0]
#         if Enemy.direction == "R" and MovingEnemy.enemy_hit == True:
#             frame = (pos // 30) % len(self.walking_frames_r)
#             self.image = self.walking_frames_r[frame]
#
#
#         # See if we hit anything
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:
#             # If we are moving right,
#             # set our right side to the left side of the item we hit
#             if self.change_x > 0:
#                 self.rect.right = block.rect.left
#             elif self.change_x < 0:
#                 # Otherwise if we are moving left, do the opposite.
#                 self.rect.left = block.rect.right
#
#         # Move up/down
#         self.rect.y += self.change_y
#
#         # Check and see if we hit anything
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:
#
#             # Reset our position based on the top/bottom of the object.
#             if self.change_y > 0:
#                 self.rect.bottom = block.rect.top
#             elif self.change_y < 0:
#                 self.rect.top = block.rect.bottom
#
#             # Stop our vertical movement
#             self.change_y = 0
#
#             if isinstance(block, MovingPlatform):
#                 self.rect.x += block.change_x
#
#     def calc_grav(self):
#         """ Calculate effect of gravity. """
#         if self.change_y == 0:
#             self.change_y = 1
#         else:
#             self.change_y += .35
#
#         # See if we are on the ground.
#         if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
#             self.change_y = 0
#             self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
#
#     def jump(self):
#         """ Called when user hits 'jump' button. """
#
#         # move down a bit and see if there is a platform below us.
#         # Move down 2 pixels because it doesn't work well if we only move down 1
#         # when working with a platform moving down.
#         self.rect.y += 2
#         platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         self.rect.y -= 2
#
#         # If it is ok to jump, set our speed upwards
#         if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
#             self.change_y = -10
#             constants.jump_sound.play()
#
#     # Enemy-controlled movement:
#     def go_left(self):
#         """ Called when the user hits the left arrow. """
#         self.change_x = -constants.speed
#         Enemy.direction = "L"
#         Enemy.stopped = False
#
#     def go_right(self):
#         """ Called when the user hits the right arrow. """
#         self.change_x = constants.speed
#         Enemy.direction = "R"
#         Enemy.stopped = False
#
#     def go_in(self):
#         Enemy.direction = "T"
#
#     def stop(self):
#         """ Called when the user lets off the keyboard. """
#         self.change_x = 0
#         Enemy.stopped = True
#
#     def god(self):
#         if Enemy.direction == "R":
#             self.change_x = 20
#             Enemy.direction = "R"
#         else:
#             self.change_x = -20
#             Enemy.direction = "L"
#
# class Enemy(pygame.sprite.Sprite):
#     '''
#     Spawn an enemy
#     '''
#     def __init__(self,x,y,img):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(img)
#         self.image.convert_alpha()
#         # self.image.set_colorkey(ALPHA)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.counter = 0  # counter variable
#
#     def move(self):
#         '''
#         enemy movement
#         '''
#         distance = 80
#         speed = 8
#
#         if self.counter >= 0 and self.counter <= distance:
#             self.rect.x += speed
#         elif self.counter >= distance and self.counter <= distance * 2:
#             self.rect.x -= speed
#         else:
#             self.counter = 0
#
#         self.counter += 1