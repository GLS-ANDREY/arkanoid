import pygame, random

# ПОДГОТОВКА МОДЕЛИ
plat = pygame.Rect(325, 650, 275, 50)
plat.centerx = 600
sharik = pygame.Rect(225, 375, 40, 40)
speed_x = 7
speed_y = 7
kubiki = []
t = [*range(0, 1200, 40)]

kubik_rect = pygame.Rect(600, 400, 40, 40)
kubiki.append(kubik_rect)

# for otstup_y in [0,40]:
#
#     for paladin in t:
#         kubik_rect = pygame.Rect(paladin, otstup_y, 40, 40)
#         kubiki.append(kubik_rect)


def dvizh():
    global speed_x, speed_y
    # ДВИЖЕНИЕ

    if 0 > plat.y:
        plat.y = 0
    if plat.bottom > 800:
        plat.bottom = 700
    if plat.x < 0:
        plat.x = 0
    if plat.right > 1200:
        plat.right = 1200

    sharik.x += speed_x
    if sharik.left < 0:
        sharik.left = 0
        speed_x = -speed_x
    if sharik.right > 1200:
        sharik.right = 1200
        speed_x = -speed_x

    volt = sharik.collidelistall(kubiki)

    volt.sort(reverse=True)
    for nomer in volt:
        print(nomer)
        print(kubiki[nomer])
    #    del kubiki[nomer]

    #sharik.y += speed_y
    if sharik.bottom > 800:
        sharik.bottom = 800
        #print("                                                                                              GAME_OVER")
        #exit()
        speed_y = -7
    if sharik.top < 0:
        sharik.top = 0
        speed_y = 7

    volt = plat.colliderect(sharik)
    if volt == 1:
        speed_y = -7
        sharik.bottom = plat.top
        speed_x = random.randint(-15, 15)
