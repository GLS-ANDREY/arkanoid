import pygame, model, random, help
from pygame import draw, image, transform, display

pygame.init()
pygame.mouse.set_visible(False)
okno = display.set_mode([1200, 800])

kubik_2 = image.load("kartynky/kubik_ng.jpg").convert()
kubik_2 = transform.scale(kubik_2, [38, 38])
kubik = image.load("kartynky/kubik_ng.png").convert()
kubik = transform.scale(kubik, [38, 38])
fon = image.load("kartynky/fon_ng.jpg")
platforma = image.load("kartynky/platforma_ng.png")
ball = image.load("kartynky/sharik_ng.png")
ball = help.izmeni_kartinku(ball, 40, 40, [255, 255, 255],5 )


def risuet_kadr():
    # рисуем кадр
    okno.blit(fon, [0, 0])
    okno.blit(platforma, [model.plat.x, model.plat.y])
    m = [0, 0, 0]
    draw.rect(okno, m, model.plat, 1)
    # рисуем шарик
    okno.blit(ball, model.sharik)
    for ku in model.kubiki:
        kubik_random = random.randint(0, 1)
        if kubik_random == 1:
            okno.blit(kubik, ku)
        if kubik_random == 0:
            okno.blit(kubik_2, ku)
    display.flip()
