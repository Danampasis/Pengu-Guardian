# Create text objects

from constants import *
import background
import levels
import constants

# from platform_scroller import game
customise = None
current_level = 0
player_color = ""

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


def main_menu():
    pygame.init()
    pygame.mixer.init()
    size = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    mouse = pygame.mouse.get_pos()
    intro = True
    global customise

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    # constants.select_sound.play()
                    constants.jump_sound.play()
                    intro = False
                    break
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro = False
                    customisation()
                    break



        backGround = background.Background('img/bg.png', [0, 0])
        screen.blit(backGround.image, backGround.rect)
        largeText = pygame.font.Font('Wonder_Boy_In_Monster_World.ttf', 60)
        TextSurf, TextRect = text_objects("Pengu Guardian", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 8))
        screen.blit(TextSurf, TextRect)

        # Display Character Icon in the menu

        img = pygame.image.load('img/menu character.png')
        img = pygame.transform.scale(img, (150 , 150))
        screen.blit(img, (80, 235))


        # Display Penguin Icon in the menu

        img = pygame.image.load('img/pengu1.png')
        img = pygame.transform.scale(img, (120, 120))
        screen.blit(img, (625, 270))


        # Display Menu Buttons

        # Play Button
        # button("GO!", 300, 200, 200, 50, GREEN, bright_green, game)
        pygame.draw.rect(screen, GREEN, (245, 200, 300, 50))
        smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
        textSurf, textRect = text_objects("N to Start", smallText)
        textRect.center = ((300 + (200 / 2)), (200 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # Customise Button
        pygame.draw.rect(screen, GREEN, (245, 275, 300, 50))
        smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
        textSurf, textRect = text_objects("? for Customise", smallText)
        textRect.center = ((300 + (200 / 2)), (275 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # Settings Button
        pygame.draw.rect(screen, GREEN, (245, 350, 300, 50))
        smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
        textSurf, textRect = text_objects("? for Settings", smallText)
        textRect.center = ((300 + (200 / 2)), (350 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # Quit
        pygame.draw.rect(screen, RED, (245, 425, 300, 50))
        smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
        textSurf, textRect = text_objects("Q to Quit!", smallText)
        textRect.center = ((300 + (200 / 2)), (425 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # print(mouse)

        # CHANGE COLOR IF MOUSE HOVERS ABOVE BUTTON

        # # if 245 + 300 > mouse[0] > 245 and 300 + 50 > mouse[1] > 200:
        # if 245 + 300 > mouse[0] > 245 and 300 + 50 > mouse[1] > 200:
        #     pygame.draw.rect(screen, bright_green, (150, 450, 100, 50))
        # else:
        #     pygame.draw.rect(screen, RED, (150, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)


def ending():
    pygame.init()
    size = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    mouse = pygame.mouse.get_pos()
    ending = True

    while ending:
        for event in pygame.event.get():
            print(event)
            print(mouse[0])
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    ending = False
                    break
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if 500 > mouse[0] > 300 and 276 > mouse[1] > 226:
            #         if click[0] == 1:
            #             quit()

        # button("GO!", 300, 200, 200, 50, GREEN, bright_green, quit())


        backGround = background.Background('img/bg.png', [0, 0])
        screen.blit(backGround.image, backGround.rect)
        largeText = pygame.font.Font('Wonder_Boy_In_Monster_World.ttf', 40)
        TextSurf, TextRect = text_objects("Thanks for playing", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 8))
        screen.blit(TextSurf, TextRect)

        # Display Character Icon in the menu

        img = pygame.image.load('img/boy_pixel_walk_green.png')
        img = pygame.transform.scale(img, (128, 128))
        screen.blit(img, (92, 250))


        # Display Penguin Icon in the menu

        img = pygame.image.load('img/penguin.png')
        img = pygame.transform.scale(img, (80, 80))
        screen.blit(img, (625, 300))

        # Quit
        pygame.draw.rect(screen, RED, (300, 425, 200, 50))
        smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
        textSurf, textRect = text_objects("Quit!", smallText)
        textRect.center = ((300 + (200 / 2)), (425 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # print(mouse)

        # CHANGE COLOR IF MOUSE HOVERS ABOVE BUTTON

        # if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        #     pygame.draw.rect(screen, bright_green, (150, 450, 100, 50))
        # else:
        #     pygame.draw.rect(screen, GREEN, (150, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)


def customisation():
    pygame.init()
    size = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    mouse = pygame.mouse.get_pos()
    customise = True
    global intro

    while customise:
        backGround = background.Background('img/bg.png', [0, 0])
        screen.blit(backGround.image, backGround.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    customise = False
                    intro = True
                    main_menu()
                    break
                if event.key == pygame.K_b:
                    player_color = "red"
                if event.key == pygame.K_r:
                    img_pengu = pygame.image.load('img/penguin.png')
                    img_pengu = pygame.transform.scale(img_pengu, (80, 80))
                    screen.blit(img_pengu, (625, 300))
                    pygame.display.flip()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if 500 > mouse[0] > 300 and 276 > mouse[1] > 226:
            #         if click[0] == 1:
            #             quit()

        # button("GO!", 300, 200, 200, 50, GREEN, bright_green, quit())


        backGround = background.Background('img/bg.png', [0, 0])
        screen.blit(backGround.image, backGround.rect)
        largeText = pygame.font.Font('Wonder_Boy_In_Monster_World.ttf', 40)
        TextSurf, TextRect = text_objects("Customisation", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 8))
        screen.blit(TextSurf, TextRect)

        # Display Character Icon in the menu

        img = pygame.image.load('img/boy_pixel_walk_green.png')
        img = pygame.transform.scale(img, (128, 128))
        screen.blit(img, (92, 250))


        # Display Penguin Icon in the menu

        # img = pygame.image.load('penguin.png')
        # img = pygame.transform.scale(img, (80, 80))
        # screen.blit(img_pengu, (625, 300))

        # Quit
        pygame.draw.rect(screen, GREEN, (300, 425, 200, 50))
        smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
        textSurf, textRect = text_objects("Quit!", smallText)
        textRect.center = ((300 + (200 / 2)), (425 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # print(mouse)

        # CHANGE COLOR IF MOUSE HOVERS ABOVE BUTTON

        # if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        #     pygame.draw.rect(screen, bright_green, (150, 450, 100, 50))
        # else:
        #     pygame.draw.rect(screen, GREEN, (150, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)



def level_intro():
    pygame.init()
    size = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    level_intro = True

    while level_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    level_intro = False
                    break



        # backGround = background.Background('bg.png', [0, 0])
        # screen.blit(backGround.image, backGround.rect)
        screen.fill(GREEN)
        largeText = pygame.font.Font('Wonder_Boy_In_Monster_World.ttf', 40)
        TextSurf, TextRect = text_objects("Level "+str(current_level+1), largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 8))
        screen.blit(TextSurf, TextRect)


        pygame.display.update()
        clock.tick(15)
        pygame.time.delay(500)
        break


def death():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.stop()
    size = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    dead = True
    global intro

    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # dead = False
                # intro = True
                # main_menu() # TODO implement method to start new game after player has died
                # break
                pygame.quit()
                quit()

        backGround = background.Background('img/bg.png', [0, 0])
        screen.blit(backGround.image, backGround.rect)
        largeText = pygame.font.Font('Wonder_Boy_In_Monster_World.ttf', 60)
        TextSurf, TextRect = text_objects("YOU DIED!!", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        screen.blit(TextSurf, TextRect)
        smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
        TextSurf, TextRect = text_objects("Press any key to quit", smallText)
        TextRect.center = ((SCREEN_WIDTH / 2), 400)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)


def help():
    pygame.init()
    pygame.joystick.init()
    j = pygame.joystick.Joystick(0)
    j.init()
    size = [SCREEN_WIDTH,SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    largeText = pygame.font.Font('Wonder_Boy_In_Monster_World.ttf', 25)
    smallText = pygame.font.Font("Wonder_Boy_In_Monster_World.ttf", 20)
    help = True

    while help:
        for event in pygame.event.get():
            backGround = background.Background('img/bg.png', [0, 0])
            screen.blit(backGround.image, backGround.rect)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    ending = False
                    break
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(8):
                    help = False
                    break
                if j.get_button(5):
                    pygame.draw.rect(screen, GREEN, (300, 375, 200, 50))
                    TextSurf, TextRect = text_objects("Shoot", smallText)
                    TextRect.center = ((SCREEN_WIDTH / 2), 400)
                    screen.blit(TextSurf, TextRect)
                if j.get_button(4):
                    pygame.draw.rect(screen, GREEN, (300, 375, 200, 50))
                    TextSurf, TextRect = text_objects("Reload", smallText)
                    TextRect.center = ((SCREEN_WIDTH / 2), 400)
                    screen.blit(TextSurf, TextRect)
                if j.get_button(2):
                    pygame.draw.rect(screen, GREEN, (300, 375, 200, 50))
                    TextSurf, TextRect = text_objects("JUMP", smallText)
                    TextRect.center = ((SCREEN_WIDTH / 2), 400)
                    screen.blit(TextSurf, TextRect)
                if j.get_button(0) or j.get_button(1) or j.get_button(3):
                    pygame.draw.rect(screen, RED, (300, 375, 200, 50))
                    TextSurf, TextRect = text_objects("Unassigned", smallText)
                    TextRect.center = ((SCREEN_WIDTH / 2), 400)
                    screen.blit(TextSurf, TextRect)
            if event.type == pygame.JOYAXISMOTION:
                lr = j.get_axis(0)
                ud = j.get_axis(1)
                if round(lr) >= 1:
                    pygame.draw.rect(screen, GREEN, (300, 375, 200, 50))
                    TextSurf, TextRect = text_objects("Go right", smallText)
                    TextRect.center = ((SCREEN_WIDTH / 2), 400)
                    screen.blit(TextSurf, TextRect)
                if round(lr) == -1:
                    pygame.draw.rect(screen, GREEN, (300, 375, 200, 50))
                    TextSurf, TextRect = text_objects("Go left", smallText)
                    TextRect.center = ((SCREEN_WIDTH / 2), 400)
                    screen.blit(TextSurf, TextRect)
                if round(ud) >= 1 or round(ud) == -1:
                    pygame.draw.rect(screen, RED, (300, 375, 200, 50))
                    TextSurf, TextRect = text_objects("Unassigned", smallText)
                    TextRect.center = ((SCREEN_WIDTH / 2), 400)
                    screen.blit(TextSurf, TextRect)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if 500 > mouse[0] > 300 and 276 > mouse[1] > 226:
            #         if click[0] == 1:
            #             quit()

        # button("GO!", 300, 200, 200, 50, GREEN, bright_green, quit())



        TextSurf, TextRect = text_objects("Press a button to see its function", largeText)
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 8))
        screen.blit(TextSurf, TextRect)

        # Display Character Icon in the menu

        img = pygame.image.load('img/controller.png')
        img = pygame.transform.scale(img, (300, 300))
        screen.blit(img, (250,100))

        # Quit
        # pygame.draw.rect(screen, RED, (300, 425, 200, 50)) #draws red rect
        textSurf, textRect = text_objects("Press select button to go back!", smallText)
        textRect.center = ((300 + (200 / 2)), (425 + (50 / 2)))
        screen.blit(textSurf, textRect)

        # print(mouse)

        # CHANGE COLOR IF MOUSE HOVERS ABOVE BUTTON

        # if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        #     pygame.draw.rect(screen, bright_green, (150, 450, 100, 50))
        # else:
        #     pygame.draw.rect(screen, GREEN, (150, 450, 100, 50))
        pygame.display.flip()
        clock.tick(15)