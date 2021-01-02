import pygame as pg
import math
import pygame_gui
import os
import sys
import random
from gases import start_game

pg.init()

pg.display.set_caption(" ")  # заголовок

size = width, height = 800, 600

screen = pg.display.set_mode(size)

pg.display.update()

run = True  # переменна, с помощью ее можно выходить из цикла

"""А вот тут будет волшебство)"""
clock = pg.time.Clock()

RED = (255, 0, 0)

changing_pos = False
BLACK = (0, 0, 0)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


# Немного теории, мы делаем идеальный газ, где молекулы не сталкиваются друг с другом


def fon():
    fon = pg.transform.scale(load_image('blue-snow.png'), (width, height))
    screen.blit(fon, (0, 0))



SPEED = 60
start_game()
while run:
    fon()
    time_delta = clock.tick(SPEED) / 1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                pass
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                pass
            if event.key == pg.K_UP:
                pass

    pg.display.flip()  # Обновление кадра
pg.quit()
