import pygame, time
from pygame import key, display, event, draw, image, transform

pygame.init()
key.set_repeat(20)
okno = display.set_mode([1200, 800])

# ПОДГОТОВКА МОДЕЛИ
plat = pygame.Rect(600, 650, 275, 50)
sharik = pygame.Rect(225, 375, 40, 40)
speed_x = 7
speed_y = 7

# ПОДГОТОВКА К РИСОВАНИЮ
fon = image.load("kartynky/fon.jpg")
platforma = image.load("kartynky/platforma.jpg")
ball = image.load("kartynky/ball.png")
ball = transform.scale(ball, [40, 40])

while 10 == 10:
    time.sleep(1 / 60)

    # ОБРАБОТКА СОБЫТИЙ
    spisok_sobitiy = event.get()

    for sobitie in spisok_sobitiy:
        if sobitie.type == pygame.KEYDOWN:
            if sobitie.key == pygame.K_a:
                plat.x -= 10
            if sobitie.key == pygame.K_d:
                plat.x += 10
        if sobitie.type == pygame.QUIT:
            exit()

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
    if sharik.right > 1200:
        sharik.right = 1200
        speed_x = -7
    if sharik.left < 0:
        sharik.left = 0
        speed_x = 7
    sharik.y += speed_y
    if sharik.bottom > 800:
        sharik.bottom = 800
        speed_y = -7
    if sharik.top < 0:
        sharik.top = 0
        speed_y = 7

    volt = plat.colliderect(sharik)
    print(volt)
    if volt == 1:
        speed_y = -7
    # Рисуем кадр
    okno.blit(fon, [0, 0])
    okno.blit(platforma, [plat.x, plat.y], [0, 750, plat.w, plat.h])
    m = [0, 0, 0]
    draw.rect(okno, m, plat, 1)
    # рисуем шарик
    okno.blit(ball, sharik)
    display.flip()
