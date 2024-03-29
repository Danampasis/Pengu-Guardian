import pygame

import constants
import platforms
import enemylast
import screens
import power_ups
import heart
import penguins


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = pygame.sprite.Group()
    item_list = pygame.sprite.Group()
    pengu_list = pygame.sprite.Group()

    # Background image
    background = None

    # Level Music
    music: str = None
    music_on = None




    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit_right = -1000
    level_limit_left = 0

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        # self.enemy_list = pygame.sprite.Group()
        self.item_list = pygame.sprite.Group()
        self.pengu_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        Level.enemy_list.update()
        self.item_list.update()
        self.pengu_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0)) # TODO optimise background shift blitting


        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        Level.enemy_list.draw(screen)
        self.item_list.draw(screen)
        self.pengu_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in Level.enemy_list:
            enemy.rect.x += shift_x

        for item in self.item_list:
            item.rect.x += shift_x

        for item in self.pengu_list:
            item.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("img/level_test_bg.png").convert_alpha()  # TODO optimise background loading
        # self.background = pygame.transform.scale(self.background, (4200,constants.SCREEN_HEIGHT)) # TODO scale background images to adaptable screen size from settings
        # self.background.set_colorkey(constants.WHITE)
        self.level_limit_right = 12000
        self.level_limit_left = 0
        self.weapons = True
        self.music_on = constants.music
        self.music = 'sfx/Grasslands Theme.mp3'

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.STONE_PLATFORM_LEFT, 1870, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1940, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 2010, 280],
                  [platforms.STONE_PLATFORM_LEFT, 2600, 450],
                  [platforms.STONE_PLATFORM_MIDDLE, 2670, 450],
                  [platforms.STONE_PLATFORM_RIGHT, 2740, 450],
                  [platforms.STONE_PLATFORM_LEFT, 2550, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 2620, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 2690, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 2760, 150],
                  [platforms.STONE_PLATFORM_RIGHT, 2830, 150],
                  [platforms.STONE, 2820, 80],
                  [platforms.STONE, 2820, 10],
                  [platforms.GRASS_LEFT, 3600, 500],
                  [platforms.GRASS_MIDDLE, 3670, 500],
                  [platforms.GRASS_RIGHT, 3740, 500],
                  [platforms.GRASS_LEFT, 3900, 400],
                  [platforms.GRASS_MIDDLE, 3970, 400],
                  [platforms.GRASS_MIDDLE, 4040, 400],
                  [platforms.GRASS_MIDDLE, 4110, 400],
                  [platforms.GRASS_MIDDLE, 4180, 400],
                  [platforms.GRASS_RIGHT, 4250, 400],
                  [platforms.STONE_PLATFORM_LEFT, 4400, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 4470, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 4540, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 4610, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 4680, 400],
                  [platforms.GRASS_LEFT, 5500, 500],
                  [platforms.GRASS_MIDDLE, 5570, 500],
                  [platforms.GRASS_RIGHT, 5640, 500],
                  [platforms.GRASS_LEFT, 5800, 400],
                  [platforms.GRASS_MIDDLE, 5870, 400],
                  [platforms.GRASS_RIGHT, 5940, 400],
                  [platforms.GRASS_LEFT, 6000, 500],
                  [platforms.GRASS_MIDDLE, 6070, 500],
                  [platforms.GRASS_RIGHT, 6140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 6120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 6190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 6260, 280],
                  [platforms.STONE_PLATFORM_LEFT, 6870, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 6940, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 7010, 280],
                  [platforms.STONE_PLATFORM_LEFT, 7600, 450],
                  [platforms.STONE_PLATFORM_MIDDLE, 7670, 450],
                  [platforms.STONE_PLATFORM_RIGHT, 7740, 450],
                  [platforms.STONE_PLATFORM_LEFT, 8550, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 8620, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 8690, 150],
                  [platforms.STONE_PLATFORM_MIDDLE, 8760, 150],
                  [platforms.STONE_PLATFORM_RIGHT, 8830, 150],
                  [platforms.STONE, 8820, 80],
                  [platforms.STONE, 8820, 10],
                  [platforms.GRASS_LEFT, 9600, 500],
                  [platforms.GRASS_MIDDLE, 9670, 500],
                  [platforms.GRASS_RIGHT, 9740, 500],
                  [platforms.GRASS_LEFT, 9900, 400],
                  [platforms.GRASS_MIDDLE, 9970, 400],
                  [platforms.GRASS_MIDDLE, 10040, 400],
                  [platforms.GRASS_MIDDLE, 10110, 400],
                  [platforms.GRASS_MIDDLE, 10180, 400],
                  [platforms.GRASS_RIGHT, 10250, 400],
                  [platforms.STONE_PLATFORM_LEFT, 10400, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 10470, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 10540, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 10610, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 10680, 400]

                  # [platforms.LAVA, 400, 585]
                  ]

        # items = [ [platforms.TORCH_1,300,300],
        #           [platforms.TORCH_2,300,300],
        #           [platforms.DOOR_MID,2806,550],
        #           [platforms.DOOR_TOP,2806,500]]

        coin_list = [ [power_ups.WORM,1950,80],
                      [power_ups.WORM, 10110, 250]]

        heart_list = [ [heart.WORM,2760,100]]

        mobs = [ [enemylast.WORM, 550, 437, 500, 640, 2],
                    [enemylast.WORM, 1400, 535, 1250, 1800, 3],
                    [enemylast.WORM, 1900, 535, 1850, 2000, 3],
                    [enemylast.WORM, 2500, 535, 2400, 2700, 3],
                    [enemylast.WORM, 4100, 335, 3970, 4250, 3]]

        pengus = [[penguins.WORM, 4800,535,4500,5300,3],
                  [penguins.WORM, 11000, 535, 10740, 11990, 3]]

        # bad_items = [platforms.LAVA_TOP, 200, 1350]

        for item in coin_list:                    # TODO Add usable items to game
            block = power_ups.Coin(item[0])
            block.rect.x = item[1]
            block.rect.y = item[2]
            block.player = self.player
            self.item_list.add(block)

        for item in heart_list:  # TODO Add usable items to game
            block = heart.Heart(item[0])
            block.rect.x = item[1]
            block.rect.y = item[2]
            block.player = self.player
            self.item_list.add(block)


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for enemy in mobs:
            block = enemylast.MovingEnemy(enemy[0])
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.boundary_left = enemy[3]
            block.boundary_right = enemy[4]
            block.change_x = enemy[5]
            block.player = self.player
            block.level = self
            self.enemy_list.add(block)

        for penguin in pengus:
            block = penguins.MovingPenguin(penguin[0])
            block.rect.x = penguin[1]
            block.rect.y = penguin[2]
            block.boundary_left = penguin[3]
            block.boundary_right = penguin[4]
            block.change_x = penguin[5]
            block.player = self.player
            block.level = self
            self.pengu_list.add(block)


        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 2250
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 400
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 6350
        block.rect.y = 280
        block.boundary_left = 6350
        block.boundary_right = 6600
        block.change_x = 5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 7250
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 400
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # block = enemylast.MovingEnemy(enemylast.TORCH_2)
        # block.rect.x = 500
        # block.rect.y = 280
        # block.boundary_left = 310
        # block.boundary_right = 700
        # block.change_x = 3
        # block.player = self.player
        # block.level = self
        # self.enemy_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
    def __init__(self, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("img/background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit_right = 4000
        self.level_limit_left = 0
        self.weapons = True
        self.music_on = constants.music
        self.music = 'sfx/Overhead Map - Village.mp3'

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_03(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("img/iceberg.png")
        # self.background.set_colorkey(constants.WHITE)
        self.level_limit_right = 3000
        self.level_limit_left = 0
        self.weapons = False
        self.music_on = constants.music
        self.music = 'sfx/Grasslands Theme.mp3'

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.STONE_PLATFORM_LEFT, 1870, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1940, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 2010, 280],
                  ]

        pengus = [[penguins.WORM, 940, 535, 840, 1300, 3]]


        for penguin in pengus:
            block = penguins.MovingPenguin(penguin[0])
            block.rect.x = penguin[1]
            block.rect.y = penguin[2]
            block.boundary_left = penguin[3]
            block.boundary_right = penguin[4]
            block.change_x = penguin[5]
            block.player = self.player
            block.level = self
            self.pengu_list.add(block)


        # Go through the array above and add platforms
        # for platform in level:
        #     block = platforms.Platform(platform[0])
        #     block.rect.x = platform[1]
        #     block.rect.y = platform[2]
        #     block.player = self.player
        #     self.platform_list.add(block)
        #     # pygame.mixer.music.load('Grasslands Theme.mp3')
        #     # pygame.mixer.music.play(-1)

        # Add a custom moving platform
        # block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        # block.rect.x = 1350
        # block.rect.y = 280
        # block.boundary_left = 1350
        # block.boundary_right = 1600
        # block.change_x = 5
        # block.player = self.player
        # block.level = self
        # self.platform_list.add(block)

class Level_04(Level):
    """ Definition for level 3. """

    def __init__(self, player):
        """ Create level 3. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("img/level4_bg.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit_right = 3600
        self.level_limit_left = 0
        self.weapons = False
        self.music = 'sfx/Credits_edit.ogg'


class Level_TEST(Level):
    """ Definition for level TEST. """

    def __init__(self, player):
        """ Create level TEST. """
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("img/background_03.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit_right = 20000
        self.level_limit_left = 0
        self.weapons = True
        self.music_on = False
        self.music = 'sfx/Credits_edit.ogg'

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.STONE_PLATFORM_LEFT, 1870, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1940, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 2010, 280],
                  [platforms.STONE_PLATFORM_MIDDLE,2200, 130],
                  [platforms.STONE_PLATFORM_LEFT, 2400, 130],
                  [platforms.STONE_PLATFORM_MIDDLE, 2470, 130],
                  [platforms.STONE_PLATFORM_MIDDLE, 2540, 130],
                  [platforms.STONE_PLATFORM_MIDDLE, 2610, 130],
                  [platforms.STONE_PLATFORM_MIDDLE, 2680, 130],
                  [platforms.STONE_PLATFORM_MIDDLE, 2750, 130],
                  [platforms.STONE_PLATFORM_RIGHT, 2820, 130],
                  [platforms.STONE, 2813, 60],
                  [platforms.STONE, 2813, 0]
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            # pygame.mixer.music.load('Grasslands Theme.mp3')
            # pygame.mixer.music.play(-1)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 5
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

