import pygame, model
from pygame import draw, image, transform, display

pygame.init()
pygame.mouse.set_visible(False)
okno = display.set_mode([1200, 800])

kubik = image.load("kartynky/kubik.png")
kubik = transform.scale(kubik, [40, 40])
fon = image.load("kartynky/fon.jpg")
platforma = image.load("kartynky/platforma.jpg")
ball = image.load("kartynky/ball.png")
ball = transform.scale(ball, [40, 40])


def risuet_kadr():
    # рисуем кадр
    okno.blit(fon, [0, 0])
    okno.blit(platforma, [model.plat.x, model.plat.y], [0, 750, model.plat.w, model.plat.h])
    m = [0, 0, 0]
    draw.rect(okno, m, model.plat, 1)
    # рисуем шарик
    okno.blit(ball, model.sharik)
    for ku in model.kubiki:
        okno.blit(kubik, ku)
    display.flip()
