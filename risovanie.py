import pygame, model
from pygame import draw, image, transform, display

pygame.init()
pygame.mouse.set_visible(False)
okno = display.set_mode([1200, 800])

kubik = image.load("kartynky/kubik_ng.jpg").convert()
kubik = transform.scale(kubik, [38, 38])
fon = image.load("kartynky/fon_ng.jpg")
platforma = image.load("kartynky/platforma_ng.png")
ball = image.load("kartynky/ball.png")
ball = transform.scale(ball, [40, 40])


def risuet_kadr():
    # рисуем кадр
    okno.blit(fon, [0, 0])
    okno.blit(platforma, [model.plat.x, model.plat.y])
    m = [0, 0, 0]
    draw.rect(okno, m, model.plat, 1)
    # рисуем шарик
    okno.blit(ball, model.sharik)
    for ku in model.kubiki:
        okno.blit(kubik, ku)
    display.flip()
