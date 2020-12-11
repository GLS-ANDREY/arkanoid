import pygame, model
from pygame import key, event

key.set_repeat(20)


def obrabotka_sobitiy():
    # ОБРАБОТКА СОБЫТИЙ
    spisok_sobitiy = event.get()

    for sobitie in spisok_sobitiy:
        if sobitie.type == pygame.KEYDOWN:
            if sobitie.key == pygame.K_a:
                model.plat.x -= 10
            if sobitie.key == pygame.K_d:
                model.plat.x += 10
        if sobitie.type == pygame.QUIT:
            exit()
        if sobitie.type == pygame.MOUSEMOTION:
            pos_x = sobitie.pos[0]
            model.plat.centerx = pos_x
